"""frame(n) is deterministic; only explicit proof ranges are supported.

Not a gameplay recreation. Menu/hand/lake relationships are author staging.
No lyric text, external assets, music or old narrative patches are loaded.
"""
from PIL import Image, ImageDraw
from . import dr_ui as ui

FPS = 24
W, H = 1280, 720
RANGES = ((4344,4654),(4929,5086))


def smooth(u):
    u = max(0, min(1, u))
    return u*u*(3-2*u)


def phase(n):
    if not isinstance(n, int) or isinstance(n, bool) or not any(a <= n < b for a,b in RANGES):
        raise ValueError(f"Unsupported proof frame {n}; ranges {RANGES} are half-open")
    if n < 4519:
        left = "Stop" if n < 4442 else "Proceed"
        a = 1 if n < 4436 or n >= 4448 else ((4442-n)/6 if n < 4442 else (n-4442)/6)
        selector = 93+174*smooth((n-4448)/12)
        return {"mode":"choice", "left":left, "left_alpha":a, "right":"Proceed", "heart_x":selector,
                "body_offset":12*smooth((n-4344)/175), "hand_reach":-8*smooth((n-4489)/6), "input_alpha":1,
                "meaning":"position remains selectable; Stop leaves a response trace before both texts converge"}
    if n < 4654:
        return {"mode":"halt", "body_offset":12, "input_alpha":1-smooth((n-4519)/12),
                "branch_alpha":smooth((n-4531)/12), "continue_alpha":smooth((n-4574)/27),
                "confirmation":n >= 4574,
                "confirm_width":150-55*smooth((n-4574)/27) if n < 4601 else 150-65*smooth((n-4601)/20),
                "meaning":"cessation offers authored continuation while consequences remain"}
    if n < 4970:
        return {"mode":"collapse", "height":1 if n < 4962 else (4969-n)/7}
    if n < 4982:
        return {"mode":"black"}
    if n < 5004:
        return {"mode":"chapter", "alpha":smooth((n-4982)/12)}
    return {"mode":"question", "alpha":smooth((n-5004)/12),
            "question_alpha":smooth((n-5051)/6), "connection":smooth((n-5016)/12)}


def choice_frame(n, state):
    image = ui.base(n, state["body_offset"],state["hand_reach"])
    d = ImageDraw.Draw(image)
    # One input SOUL; the close-up hand and the world-body are the same Kris.
    d.rectangle((50,389,350,542), outline=ui.WHITE, width=2)
    ui.text(d, (72,408), state["left"], 29, ui.colour(ui.WHITE,state["left_alpha"]))
    ui.text(d, (216,408), state["right"], 29)
    hx = state["heart_x"]
    d.line((hx,508,hx,567,573,567,622,435), fill=(92,34,55), width=2)
    ui.heart(d, (hx,483), scale=2)
    # Small Stop residue, not an additional choice or a fake gameplay message.
    if n >= 4418:
        d.line((87,534,110,534), fill=(115,121,135), width=2)
    return image


def halt_frame(n, state):
    image = ui.base(n, state["body_offset"],-8)
    d = ImageDraw.Draw(image)
    ui.heart(d, (267,483), scale=2)
    if state["confirmation"]:
        white = smooth((n-4574)/80)
        ui.heart(d,(267,483),scale=1.6,fill=tuple(round(ui.RED[i]*(1-white)+ui.ICE[i]*white) for i in range(3)))
    c = ui.colour(ui.GREY, state["branch_alpha"])
    d.line((267,513,267,565,689,565,744,538), fill=c, width=2)
    d.line((689,565,923,565,983,538), fill=c, width=2)
    # Author diagram: neither represents an extra canonical in-game menu.
    d.rectangle((734,503,837,540), outline=c, width=1)
    d.rectangle((969,503,1072,540), outline=c, width=1)
    d.line((784,520,812,520,804,514), fill=c, width=2)
    d.line((812,520,804,526), fill=c, width=2)
    d.line((1003,513,1003,530), fill=c, width=2)
    d.line((1012,513,1012,530), fill=c, width=2)
    # The full menu fades while the SOUL and body persist.
    if state["input_alpha"] > 0:
        d.rectangle((50,389,350,542), outline=ui.colour(ui.WHITE,state["input_alpha"]), width=2)
    if state["confirmation"]:
        half = state["confirm_width"]
        d.rectangle((200-half,389,200+half,542),outline=ui.WHITE,width=2)
        ui.text(d,(200,429),"Proceed",29,anchor="mm")
    if state["continue_alpha"] > 0:
        d.rectangle((730,499,841,544), outline=ui.colour(ui.WHITE,state["continue_alpha"]), width=1)
    # A retained witness/relationship shadow prevents a visual "everything reset".
    d.polygon([(520,410),(537,383),(557,389),(569,424),(558,479),(529,479)], fill=ui.colour((35,39,53),state["branch_alpha"]))
    return image


def ending_frame(n, state):
    image = Image.new("RGB",(W,H),(0,0,0))
    d = ImageDraw.Draw(image)
    if state["mode"] == "black":
        return image
    if state["mode"] == "collapse":
        world = ui.base(n,12)
        height = max(1, round(548*state["height"]))
        if n < 4962:
            return world
        # The world's image collapses; it is not crossfaded to a replacement shot.
        strip = world.crop((24,56,1256,604)).resize((1232,height), Image.Resampling.NEAREST)
        image.paste(strip,(24,330-height//2))
        return image
    if state["mode"] == "chapter":
        ui.text(d,(640,319),"Insert Chapter 7",31,ui.colour(ui.WHITE,state["alpha"]),anchor="mm")
        ui.text(d,(640,367),"Side B",31,ui.colour(ui.WHITE,state["alpha"]),anchor="mm")
        return image
    a = state["alpha"]
    # Incomplete outer frame: no assertion that either participant is omnipotent.
    c = ui.colour((79,89,109),a)
    d.line((368,268,368,430,912,430,912,290), fill=c, width=1)
    d.line((368,268,861,268),fill=c,width=1)
    ui.hand(d,(558,337),scale=1.45,fill=ui.colour(ui.ICE,a))
    ui.heart(d,(738,354),scale=3,fill=ui.colour(ui.RED,a))
    p = state["connection"]
    d.line((612,365,612+42*p,365),fill=ui.colour(ui.GREY,a),width=2)
    d.line((698,365,698-42*p,365),fill=ui.colour(ui.GREY,a),width=2)
    if state["question_alpha"]:
        ui.text(d,(640,510),"Who executes whom?",35,ui.colour(ui.WHITE,state["question_alpha"]),anchor="mm")
    return image


def frame(n):
    state = phase(n)
    if state["mode"] == "choice":
        return choice_frame(n,state)
    if state["mode"] == "halt":
        return halt_frame(n,state)
    return ending_frame(n,state)
