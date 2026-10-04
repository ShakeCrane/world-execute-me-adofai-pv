"""Integer-frame v02 DR entry. No legacy ALL/patch stack or hidden state."""
from bisect import bisect_right
from pathlib import Path
import json
from PIL import Image
from . import scenes

ROOT=Path(__file__).resolve().parents[2]
PLAN=json.loads((ROOT/"data/deltarune_shot_plan.json").read_text(encoding="utf-8"))
FPS=24
W,H=1280,720
STARTS=[s["start_frame"] for s in PLAN["shots"]]


def shot_at(n):
    if not isinstance(n,int) or isinstance(n,bool) or not 0<=n<5086:
        raise ValueError(f"Invalid DR integer frame: {n}")
    return PLAN["shots"][bisect_right(STARTS,n)-1]


def frame(n):
    shot=shot_at(n)
    fn=scenes.SCENES.get(shot["scene"])
    if fn is None:
        raise NotImplementedError(f"Blocking not yet implemented: {shot['id']} {shot['scene']}")
    if n==0:
        return Image.new("RGB",(W,H),(0,0,0))
    image=fn(n,shot)
    if image.mode!="RGB" or image.size!=(W,H):
        raise ValueError(f"Invalid renderer result at {n}")
    return image
