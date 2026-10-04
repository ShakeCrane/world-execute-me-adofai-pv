"""Render sparse stills and silent short ranges; verify shuffled-order replay."""
from pathlib import Path
import argparse
import hashlib
import json
import platform
import random
import sys
import PIL
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from film.deltarune_poc import renderer as r
from film.deltarune_poc import dr_ui as ui

STILLS = [4344,4418,4430,4436,4439,4442,4445,4448,4454,4460,4495,4518,
          4519,4531,4543,4573,4574,4601,4653,4929,4962,4969,4970,4981,
          4982,4994,5004,5016,5028,5051,5057,5085]
STILLS = sorted(set(STILLS) | set(range(4430,4461)) | set(range(4519,4544)) |
                set(range(4962,4982)) | set(range(5004,5017)))


def digest(image):
    return hashlib.sha256(image.tobytes()).hexdigest()


def contact_sheet(out, frames, filename):
    cols, thumbw, thumbh, caption = 3, 426, 240, 34
    rows = (len(frames)+cols-1)//cols
    sheet = Image.new("RGB",(cols*thumbw,rows*(thumbh+caption)),(18,22,30))
    d = ImageDraw.Draw(sheet)
    for i,n in enumerate(frames):
        x, y = i%cols*thumbw, i//cols*(thumbh+caption)
        shot = " / ".join(s["id"] for s in PLAN["shots"] if s["start_frame"] <= n < s["end_frame"])
        image = Image.open(out/f"{n:05d}.png").resize((thumbw,thumbh),Image.Resampling.LANCZOS)
        sheet.paste(image,(x,y))
        ui.text(d,(x+10,y+thumbh+6),f"{shot}  f{n}  {n/24:.3f}s",18,(192,205,223))
    sheet.save(out/filename)


def animation(out, start, end, filename):
    frames = [r.frame(n).resize((640,360),Image.Resampling.LANCZOS) for n in range(start,end,2)]
    # Exact selected-frame timing, ms rounded cumulatively (not constant 83ms).
    durations = [round((min(end,start+2*(i+1))-start)*1000/24)-round(i*2*1000/24) for i in range(len(frames))]
    frames[0].save(out/filename,save_all=True,append_images=frames[1:],duration=durations,loop=0,lossless=True,method=3)


PLAN = json.loads((ROOT / "data/deltarune_shot_plan.json").read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stills-only",action="store_true")
    args = parser.parse_args()
    out = ROOT/"out/deltarune_poc"
    out.mkdir(parents=True,exist_ok=True)
    records, failures = [], []
    first = {}
    for n in STILLS:
        image = r.frame(n)
        if image.mode != "RGB" or image.size != (1280,720):
            failures.append(f"Invalid image format at {n}")
        image.save(out/f"{n:05d}.png")
        first[n] = digest(image)
        shot = next(s for s in PLAN["shots"] if s["start_frame"] <= n < s["end_frame"])
        records.append({"frame":n,"seconds":n/24,"shot":shot["id"],"mode":r.phase(n)["mode"],
                        "file":f"out/deltarune_poc/{n:05d}.png","pixel_sha256":first[n],
                        "png_sha256":hashlib.sha256((out/f"{n:05d}.png").read_bytes()).hexdigest()})
    shuffled = STILLS.copy()
    random.Random(20261001).shuffle(shuffled)
    for n in shuffled:
        if digest(r.frame(n)) != first[n]:
            failures.append(f"Order dependent frame: {n}")
    for n in range(4970,4982):
        if r.frame(n).getbbox() is not None:
            failures.append(f"Hard cut not pure black: {n}")
    # Out-of-range calls cannot silently return old DSH imagery or filler.
    rejected = [0,4343,4654,4928,5086,-1,4430.5,True]
    for n in rejected:
        try:
            r.frame(n)
            failures.append(f"Unsupported input accepted: {n}")
        except ValueError:
            pass
    # Selector changes sides while body progression is independent and limited.
    if r.phase(4448)["heart_x"] == r.phase(4460)["heart_x"]:
        failures.append("Selector does not move across converged options")
    if abs(r.phase(4460)["body_offset"]-r.phase(4448)["body_offset"]) > 2:
        failures.append("Body motion incorrectly follows selector displacement")
    if r.frame(4969).getbbox() is None or r.frame(5085).getbbox() is None:
        failures.append("Pre-cut/final image wrongly black")
    contact_sheet(out,[4344,4418,4439,4445,4454,4460,4495,4519,4543],"menu_contact.png")
    contact_sheet(out,[4929,4969,4970,4982,4994,5016,5028,5057,5085],"ending_contact.png")
    if not args.stills_only:
        animation(out,4344,4654,"menu_preview.webp")
        animation(out,4929,5086,"ending_preview.webp")
    sources = [Path(__file__),*sorted((ROOT/"film/deltarune_poc").glob("*.py")),
               ROOT/"film/tui_pv_world_execute_20260926/tuikit.py"]
    report = {"checked_on":"2026-10-01","technical_passed":not failures,"errors":failures,
              "supported_ranges":list(r.RANGES),"supported_frame_count":sum(b-a for a,b in r.RANGES),
              "stills":records,"resolution":[1280,720],"fps":24,"shuffle_replays":len(shuffled),
              "hard_cut_black_frames_checked":12,"unsupported_inputs_rejected":len(rejected),
              "renderer_sources":{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
              "plan_sha256":hashlib.sha256((ROOT/"data/deltarune_shot_plan.json").read_bytes()).hexdigest(),
              "runtime":{"python":platform.python_version(),"Pillow":PIL.__version__,"font_path":str(ui.FONT_FILE),
                         "font_sha256":hashlib.sha256(ui.FONT_FILE.read_bytes()).hexdigest()},
              "silent_preview":not args.stills_only,"preview_resolution":[640,360],"preview_fps":12,
              "visual_review":"See docs/deltarune/08_POC_REVIEW.md; runtime checks do not confirm visual success",
              "limitations":["No audio listening QA","Original geometric study, not exact gameplay reconstruction",
                              "Only listed proof ranges render; other shots planned","Game visual R01–03 and final art pending"]}
    (ROOT/"data/deltarune/poc_validation.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"technical_passed":not failures,"errors":failures,"stills":len(records),
                      "supported_frame_count":report["supported_frame_count"],"output":str(out)},ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)


if __name__ == "__main__":
    main()
