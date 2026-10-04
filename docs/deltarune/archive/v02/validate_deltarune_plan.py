"""Check coverage, independent timing anchors, evidence and baseline integrity."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def validate():
    plan = json.loads((ROOT / "data/deltarune_shot_plan.json").read_text(encoding="utf-8"))
    timing = json.loads((ROOT / plan["timing_source"]).read_text(encoding="utf-8"))
    canon = (ROOT / plan["evidence_register"]).read_text(encoding="utf-8")
    evidence = set(re.findall(r"\| (E\d{2}) \|", canon))
    required = "id title section start_time end_time start_frame end_frame song_cue chapter route canon_evidence narrative_purpose player_state kris_state other_character_state story_state camera layout foreground background ui_elements text character soul transition_in transition_out colour motion effects original_repo_components_reused new_code_required assets_required unresolved_question technical_implementation shot_budget scene movement_intention transition_intention".split()
    errors, observed, cursor, ids = [], [], 0, set()
    for shot in plan["shots"]:
        sid = shot["id"]
        if sid in ids:
            errors.append(f"Duplicate {sid}")
        ids.add(sid)
        for field in required:
            if field not in shot or shot[field] in (None, "", []):
                errors.append(f"{sid}: missing {field}")
        a, b = shot["start_frame"], shot["end_frame"]
        if not isinstance(a, int) or not isinstance(b, int) or a != cursor or b <= a:
            errors.append(f"{sid}: gap/overlap/invalid range {a}:{b}, expected {cursor}")
        cursor = b
        if shot["start_time"] != a / plan["fps"] or shot["end_time"] != b / plan["fps"]:
            errors.append(f"{sid}: inconsistent time/frame")
        for ref in shot["canon_evidence"]:
            if ref not in evidence:
                errors.append(f"{sid}: unresolved evidence {ref}")
        expected = [(w["line_id"], w["word_index"], round(w["start"] * plan["fps"]))
                    for w in timing["skeleton"]["words"] if a <= round(w["start"] * plan["fps"]) < b]
        actual = [(w["line_id"], w["word_index"], w["frame"]) for w in shot["song_cue"]["word_onsets"]]
        if actual != expected:
            errors.append(f"{sid}: word onset mismatch")
        observed.extend(actual)
        for frame in shot["validation_frames"]:
            if not a <= frame < b:
                errors.append(f"{sid}: QA frame outside shot")
        for component in shot["original_repo_components_reused"]:
            path = component.split(":", 1)[0]
            if not (ROOT / path).is_file():
                errors.append(f"{sid}: reused path missing {path}")
        technical = shot["technical_implementation"]
        if technical["new_section_path_planned"] != f"film/deltarune_poc/scenes.py:{shot['scene']}":
            errors.append(f"{sid}: section routing mismatch")
        if shot["shot_budget"] not in {"HERO","SUPPORT","BREATH","TRANSITION"}:
            errors.append(f"{sid}: invalid production budget")
        if set(shot["evidence_usage"]) != set(shot["canon_evidence"]):
            errors.append(f"{sid}: unused or undocumented merged evidence")
        proof = technical["proof_renderer"]
        if proof and not (ROOT/proof).exists():
            errors.append(f"{sid}: declared proof renderer missing")
    if cursor != plan["frame_count"] or cursor != round(plan["nominal_duration_seconds"] * plan["fps"]):
        errors.append("End frame != nominal duration frame count")
    expected_all = [(w["line_id"], w["word_index"], round(w["start"] * plan["fps"])) for w in timing["skeleton"]["words"]]
    if observed != expected_all:
        errors.append("Full word timeline lost, duplicated or reordered")
    by_id = {s["id"]: s for s in plan["shots"]}
    for event in plan["frame_events"]:
        at = event["start"]
        for a, b, desc in event["steps"]:
            if a != at or b <= a or not desc:
                errors.append(f"{event['id']}: discontinuous event step")
            at = b
        if at != event["end"]:
            errors.append(f"{event['id']}: event coverage mismatch")
        linked = [by_id[s] for s in event["shots"]]
        if not min(s["start_frame"] for s in linked) <= event["start"] < event["end"] <= max(s["end_frame"] for s in linked):
            errors.append(f"{event['id']}: event outside associated shots")
    # v02 deliberately merges the 6+6 into a single continuous shot, while all
    # 12 original onsets remain performance events (not new edit boundaries).
    execution = by_id[plan["execution_shot"]]
    for anchor in plan["execution_pulse_anchors"]:
        line = anchor["line_id"]
        expected = round(min(w["start"] for w in timing["skeleton"]["words"] if w["line_id"]==line)*24)
        if anchor["frame"] != expected or not execution["start_frame"] <= expected < execution["end_frame"]:
            errors.append(f"Execution line {line}: shifted/lost anchor")
    if [a["line_id"] for a in plan["execution_pulse_anchors"]] != list(range(67,79)):
        errors.append("Execution count != twelve")
    hero_count = sum(s["shot_budget"]=="HERO" for s in plan["shots"])
    if not 8 <= hero_count <= 15:
        errors.append(f"Hero budget outside director target: {hero_count}")
    reviewed = json.loads((ROOT/"data/deltarune/director_review.json").read_text(encoding="utf-8"))["reviewed_shots"]
    legacy = {old:s["id"] for s in plan["shots"] for old in s["legacy_source_shots"]}
    if len(legacy) != sum(len(s["legacy_source_shots"]) for s in plan["shots"]):
        errors.append("A legacy shot was assigned twice")
    for review in reviewed:
        if legacy.get(review["old_id"]) != review["target"]:
            errors.append(f"Director review/source drift at {review['old_id']}")
    baseline = json.loads((ROOT / "data/deltarune/baseline_inventory.json").read_text(encoding="utf-8"))
    for original in baseline["files"]:
        if hashlib.sha256((ROOT / original["path"]).read_bytes().replace(b"\r\n", b"\n")).hexdigest() != original["lf_sha256"]:
            errors.append(f"Original code changed: {original['path']}")
    # Scan new deliverables against local restored lyrics if available. Do not
    # print any lyric content. Exact lines >=4 words catch accidental copying.
    lyric_source = ROOT / "input/lyrics.lrc"
    privacy = "local lyrics unavailable; scan skipped"
    if lyric_source.exists():
        def normalise(s):
            return " ".join(re.findall(r"[a-z]+", s.lower()))
        lines = [normalise(re.sub(r"\[[^\]]*\]", "", line)) for line in lyric_source.read_text(encoding="utf-8").splitlines()]
        lines = [s for s in lines if len(s.split()) >= 4]
        files = [*sorted((ROOT / "docs/deltarune").glob("*.md")), ROOT / "data/deltarune_shot_plan.json"]
        for p in files:
            text = normalise(p.read_text(encoding="utf-8"))
            if any(line in text for line in lines):
                errors.append(f"Potential lyric line copied: {p.relative_to(ROOT)}")
        privacy = f"scanned {len(files)} new text deliverables against local lyrics without outputting lyrics"
    poc_path = ROOT/"data/deltarune/poc_validation_v02.json"
    poc_current = None
    if poc_path.exists():
        poc = json.loads(poc_path.read_text(encoding="utf-8"))
        poc_current = poc["plan_sha256"] == hashlib.sha256((ROOT/"data/deltarune_shot_plan.json").read_bytes()).hexdigest()
        poc_current = poc_current and all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest() == sha for p,sha in poc["renderer_sources"].items())
        if not poc_current:
            errors.append("PoC manifest stale; regenerate proof after plan/renderer change")
    report = {"passed": not errors, "errors": errors, "frame_count": cursor, "shots": len(ids),
              "critical_events": len(plan["frame_events"]), "word_anchors": len(observed),
              "sung_lines": len({w[0] for w in observed}), "evidence_ids": len(evidence),
              "baseline_files_checked": len(baseline["files"]), "baseline_comparison": "LF-normalized content; Git checkout CRLF ignored", "lyric_privacy": privacy,
              "poc_manifest_current":poc_current,
              "design_version":plan["design_version"],"production_budget":dict(Counter(s["shot_budget"] for s in plan["shots"])),
              "legacy_shots_reviewed":len(reviewed),"deleted_legacy_shots":sum(r["target"] is None for r in reviewed),
              "agency_frame_distribution": dict(Counter({k: sum(s["end_frame"]-s["start_frame"] for s in plan["shots"] if s["agency_preset"] == k) for k in sorted({s["agency_preset"] for s in plan["shots"]})})),
              "note": "Agency presets are director categories, not quantitative canon; mixed routes cannot be counted as pure normal/weird.",
              "plan_sha256": hashlib.sha256((ROOT / "data/deltarune_shot_plan.json").read_bytes()).hexdigest()}
    (ROOT / "data/deltarune/plan_validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    return report


if __name__ == "__main__":
    result = validate()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["passed"] else 1)
