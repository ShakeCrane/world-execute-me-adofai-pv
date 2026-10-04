"""Lyric-driven geometric blocking v03. Original shapes, not final art.
Every registered scene has a full-frame world/action; no DSH frame fallback.
"""
import math
from PIL import Image,ImageDraw
from .stage import Stage,at,lerp,point,mix,INK,WHITE,RED,ICE,GREEN,GOLD,W,H
from . import scenes as old


def vessel_parts(s,n,complete=False,xcenter=640):
    u=1 if complete else at(n,130,156)
    selected=(145,156,170)
    def parts(x,k,alpha=1):
        c=mix(INK,selected,alpha)
        hy=lerp(190,310,u); by=lerp(363,365,u); ly=lerp(590,465,u)
        # Deliberately blank face, no Kris hair or green stripe.
        s.ellipse((x-32*k,hy-16*k,x+32*k,hy+38*k),c,INK,2)
        s.poly([(x-35*k,by),(x+35*k,by),(x+42*k,by+100*k),(x-38*k,by+100*k)],c,INK,2)
        s.poly([(x-31*k,ly),(x-3*k,ly),(x-10*k,ly+89*k),(x-39*k,ly+89*k)],c,INK,2)
        s.poly([(x+3*k,ly),(x+31*k,ly),(x+39*k,ly+89*k),(x+10*k,ly+89*k)],c,INK,2)
    if not complete:
        parts(365,.75,1-u);parts(915,.86,1-u)
    parts(xcenter,1)
    if not complete and n<130:
        for yy,label in [(100,'HEAD'),(333,'TORSO'),(555,'LEGS')]:s.text((122,yy),label,19,(139,153,169))
    if not complete:
        s.heart(point((98,112),(640,590),at(n,93,130)),2.5)


def power_protection(n,shot):
    s=Stage(n,'dark');p=at(n,1,43)
    s.line([(98,112),(lerp(98,480,p),112)],mix(INK,RED,p),3)
    s.heart((98,112),1.7+at(n,1,20))
    q=at(n,43,93)
    for x,dx in [(425,1),(855,-1)]:
        for y,dy in [(245,1),(614,-1)]:
            s.line([(x,y+dy*lerp(0,30,q)),(x,y),(x+dx*lerp(0,42,q),y)],mix(INK,(127,151,165),q),3)
    return s.finish()


def pieces(n,shot):
    s=Stage(n,'dark');vessel_parts(s,n);return s.finish()


def parameters(n,shot):
    s=Stage(n,'dark');vessel_parts(s,n,True,455)
    for i,(label,val) in enumerate([('NAME','VESSEL'),('TRAIT','...')]):
        y=335+i*95;a=at(n,177+i*20,197+i*20)
        s.box((778,y-32,1118,y+34),fill=INK,outline=mix(INK,WHITE,a),width=2)
        s.text((835,y),label,20,mix(INK,WHITE,a))
        s.text((1020,y),val,22,mix(INK,WHITE,a))
    s.heart((752,545),2.6)
    return s.finish()


def discard(n,shot):
    image=parameters(242,shot)
    # Brief fade belongs to the discard action, never a long screenshot filler.
    fade=1-at(n,243,251)
    return Image.blend(Image.new('RGB',(W,H),(7,11,19)),image,fade)


def arrival(n,shot):
    s=Stage(n,'room');s.room(True)
    body=s.actor('kris',880-120*at(n,306,385),560,1.6,hands={'right':(969-120*at(n,306,385),433)})
    s.heart(body['chest'],2.5)
    if 306<=n<343:
        a=1-at(n,331,343)
        s.line([(101,151),(202,151),(202,178)],mix(INK,(114,141,157),a),2)
        s.text((144,177),'SAVE',16,mix(INK,(114,141,157),a))
    s.input(heart=False,pulse=at(n,306,343),target=body['chest'] if n>=306 else None)
    return s.finish()


help_path=old.help_path
refusal=old.refusal
welcome=old.welcome
party_breath=old.party_breath
shared_rhythm=old.shared_rhythm
screen_exit=old.screen_exit
protect=old.protect
bed_drag=old.bed_drag
cease_input=old.cease_input
continue_input=old.continue_input
crt_reveal=old.crt_reveal
hand_aftermath=old.hand_aftermath
final_pulse=old.final_pulse
chapter_cut=old.chapter_cut
unresolved=old.unresolved


def math_points(n,shot):
    s=Stage(n,'warm');s.floor(warm=True)
    x=600+30*at(n,715,803)
    wrist=point((687,445),(789,384),at(n,840,890))
    body=s.actor('kris',x,560,1.55,hands={'right':wrist})
    for i in range(9):
        xx=382+i*58
        s.ellipse((xx-3,577-3,xx+3,577+3),mix(INK,GOLD,at(n,715+i*5,760+i*5)))
    if n>=803:
        a=at(n,803,840)
        pts=[(625+math.cos(i/44*math.pi*1.8)*150,563+math.sin(i/44*math.pi*1.8)*32) for i in range(45)]
        s.line(pts,mix(INK,GOLD,a),2)
        # Dotted prediction ends at x=720; the whole person's hand passes it.
        for yy in range(400,550,12):s.line([(720,yy),(720,yy+5)],(102,112,113),1)
    s.heart(body['chest'],2)
    return s.finish()


def math_wave(n,shot):
    s=Stage(n,'warm');s.floor(warm=True)
    x=630+48*at(n,890,980)
    wrist=(x+100,424-20*at(n,980,1014))
    body=s.actor('kris',x,560,1.55,pose='walk' if n<980 else 'hold',step=n/15,hands={'right':wrist})
    pts=[(x,601+12*math.sin(x/45+n/22)) for x in range(143,1048,6)]
    s.line(pts,(109,133,139),2)
    for i in range(4):
        xx=410+i*155
        s.line([(xx-25,575),(xx+25,584)],(167,152,126),2)
    reach=at(n,1014,1066)
    s.line([(1022,576),(1060,lerp(576,519,reach))],GOLD,2)
    s.line([(1060,490),(1060,644)],(124,142,145),3)
    s.heart(body['chest'],2)
    return s.finish()


def mode_switch(n,shot):
    p=at(n,1066,1145);camera=22*math.sin(at(n,1145,1192)*math.pi)*(1-at(n,1192,1235))
    s=Stage(n,'warm',camera=camera);s.road()
    edge=1110-940*p
    s.poly([(edge,0),(W,0),(W,H),(edge-70,H)],(19,35,57))
    body=s.actor('kris',585+40*p,560,1.5,pose='walk',step=n/20)
    s.actor('susie',877,560,1.2,pose='walk',step=n/19)
    s.heart(body['chest'],2)
    if 1145<=n<1235:
        width=160*math.sin(at(n,1145,1235)*math.pi)
        s.box((0,0,width,H),fill=(7,12,21));s.box((W-width,0,W,H),fill=(7,12,21))
    return s.finish()


def curiosity(n,shot):
    s=Stage(n,'warm',camera=35*math.sin((n-1417)/75));s.road()
    for j,p in enumerate([1417,1484,1540]):
        a=at(n,p,p+35)
        pts=[(490,590),(530+j*78,489),(855+j*80,401)]
        s.line(pts,mix(INK,(149,147,122),a*.5),2)
    walk=at(n,1417,1513)
    body=s.actor('kris',490+90*math.sin(walk*math.pi),560,1.4,pose='walk',step=n/16)
    s.actor('susie',899,560,1.3,pose='rest',hands={'left':(830,450)})
    s.heart(body['chest'],2)
    s.input(heart=False,pulse=.3+.4*math.sin(n/19)**2)
    return s.finish()


def first_execute(n,shot):
    s=Stage(n,'warm');s.road()
    s.poly([(675,534),(719,534),(813,H),(584,H)],(14,24,34))
    up=at(n,1637,1667)
    # Board pivots from a waiting angle to span the small gap.
    y=lerp(606,526,up)
    s.poly([(616,534),(780,y),(791,y+18),(622,551)],(162,133,91),INK,3)
    wrist=(630,546-20*up)
    body=s.actor('kris',527,560,1.4,hands={'right':wrist})
    sx=lerp(923,615,at(n,1667,1718))
    s.actor('susie',sx,560,1.3,pose='walk' if 1667<=n<1718 else 'rest',step=n/13)
    s.heart(body['chest'],2)
    s.input(heart=False,pulse=1-at(n,1637,1667))
    if n>=1683:
        s.line([(95,590),(95,400),(1220,400),(1220,586)],mix(INK,(109,134,130),at(n,1683,1774)*.7),2)
    return s.finish()


def table_world(n):
    s=Stage(n,'warm');s.room(True)
    body=s.actor('kris',440+140*at(n,1774,1865),550,1.5,hands={'right':(lerp(531,670,at(n,1774,1865)),467)})
    s.actor('susie',923,550,1.35,hands={'left':(lerp(854,725,at(n,1865,1902)),469)})
    s.poly([(514,501),(886,488),(965,568),(510,593)],(119,99,77),INK,3)
    s.line([(556,587),(540,699)],(66,60,56),13);s.line([(914,567),(938,699)],(66,60,56),13)
    s.heart(body['chest'],1.8)
    return s


def giving(n,shot):
    s=table_world(n)
    x=lerp(551,715,at(n,1774,1865));x=lerp(x,771,at(n,1865,1902))
    s.ellipse((x-34,474,x+28,495),(112,75,128),INK,2)
    s.poly([(x+24,475),(x+34,469),(x+33,480)],GREEN)
    s.ellipse((x+15,499,x+49,532),(186,83,83),INK,2)
    s.line([(x+31,499),(x+39,491)],GREEN,3)
    return s.finish()


def cat_care(n,shot):
    s=Stage(n,'warm');s.floor(warm=True)
    wrist=(618,526+4*math.sin(n/13))
    body=s.actor('kris',523,594,1.35,hands={'right':wrist})
    s.actor('susie',1010,560,.95,pose='rest')
    cx=lerp(739,681,at(n,1951,1991));cy=572-4*math.sin(n/13)
    s.ellipse((cx-66,cy-34,cx+49,cy+22),(172,151,116),INK,3)
    s.ellipse((cx-88,cy-52,cx-28,cy+7),(183,161,124),INK,2)
    s.poly([(cx-84,cy-39),(cx-83,cy-67),(cx-64,cy-46)],(183,161,124),INK,2)
    s.poly([(cx-51,cy-49),(cx-34,cy-65),(cx-32,cy-31)],(183,161,124),INK,2)
    for xx in [cx-17,cx+5,cx+26]:s.line([(xx,cy-20),(xx-3,cy+4)],(107,96,77),3)
    s.line([(cx+36,cy-7),(cx+69,cy-11),(cx+74,cy-35)],(172,151,116),9)
    s.heart(body['chest'],1.8)
    return s.finish()


def dependency(n,shot):
    s=Stage(n,'room');s.room(True)
    a=at(n,2080,2125)
    body=s.actor('kris',760,560,1.65,hands={'left':point((674,445),(623,420),a)})
    s.line([(98,112),(151,112),(516,403)],(134,91,108),2)
    s.line([(516,403),body['left']],mix(INK,GOLD,a),3)
    s.heart((516,403),2.4)
    if a:s.ellipse((body['left'][0]-6,body['left'][1]-6,body['left'][0]+6,body['left'][1]+6),mix(INK,GOLD,a))
    return s.finish()


def role_switch(n,shot):
    s=Stage(n,'warm');s.road();p=at(n,2125,2382)
    edge=1040-910*at(n,2125,2205)
    s.poly([(edge,0),(W,0),(W,H),(edge-70,H)],(19,35,57))
    kx=580+65*p;body=s.actor('kris',kx,560,1.5,hands={'right':(kx+100,434-12*math.sin(n/27))})
    s.actor('susie',930-100*at(n,2295,2382),560,1.15,hands={'left':(860-100*at(n,2295,2382),446)})
    s.heart(body['chest'],2)
    s.input(heart=False,pulse=.2+.3*math.sin(n/21)**2)
    return s.finish()


def absence(n,shot):
    if n<2693:return old.separation(n,shot)
    s=Stage(n,'room',zoom=1-.2*at(n,2693,2728));s.room(True);s.cage()
    hx=350+18*math.sin((n-2693)/11)*at(n,2693,2705)
    kx=535+325*at(n,2728,2784)
    s.actor('kris',kx,560,1.7,pose='walk' if 2728<=n<2784 else 'hold',step=(n-2728)/10)
    s.heart((hx,450),3)
    return s.finish()


def branches(s,n,prune=False):
    s.road(False)
    for i,path in enumerate([[(541,601),(340,435),(181,327)],[(541,601),(665,459),(928,307)],[(541,601),(916,509),(1150,481)]]):
        a=1-.77*at(n,2885+i*16,2960+i*16) if prune and i!=1 else 1
        s.line(path,mix((30,43,54),(175,177,139),a),5)
        if i!=1 and prune:
            s.line([(path[-1][0]-22,path[-1][1]-22),(path[-1][0]+22,path[-1][1]+22)],mix(INK,(121,137,140),1-a),3)


def pruning(n,shot):
    s=Stage(n,'cold');branches(s,n,True)
    p=at(n,2972,3014)
    body=s.actor('kris',541+95*p,594-89*p,1.3,pose='walk',step=n/15)
    s.input(xy=point((350,450),(98,112),at(n,2838,2885)),target=(928,307),pulse=.35+.3*math.sin(n/19)**2)
    return s.finish()


def illegal_attempt(n,shot):
    s=Stage(n,'cold');branches(s,n,True)
    wrist=point((741,430),(686,452),at(n,3014,3093))
    body=s.actor('kris',636,560,1.5,hands={'right':wrist})
    s.line([(1050,268),(1050,571)],(155,172,177),6)
    for y in [315,370,425,480]:s.line([(1050,y),(1074,y-18)],(155,172,177),3)
    tx=lerp(950,1049,at(n,3093,3149));tx=lerp(tx,935,at(n,3149,3232))
    s.input(target=(tx,398),pulse=.4+.5*math.sin(n/12)**2)
    s.line([body['right'],(775,413)],mix(RED,INK,at(n,3014,3093)),2)
    return s.finish()


def threshold(n,shot):
    s=Stage(n,'cold',camera=50*at(n,3232,3549));s.road(False)
    for i,x in enumerate([190,360,970]):
        alpha=1-at(n,3340+i*22,3420+i*22)
        s.box((x,250,x+83,480),fill=(19,30,46),outline=mix(INK,(110,137,142),alpha),width=3)
    p=at(n,3232,3549)
    body=s.actor('kris',527+204*p,570,1.5,pose='walk',step=n/(20-10*p))
    s.line([(460,595),(820,574),(934,352)],(149,151,132),4)
    s.input(target=(934,352),pulse=.2+.7*math.sin(n/(18-8*p))**2)
    return s.finish()


def execution_state(n,plan):
    anchors=plan['execution_pulse_anchors'];index=max(i for i,a in enumerate(anchors) if n>=a['frame']);a=anchors[index]
    return index,a,at(n,a['frame'],min(a['frame']+12,3820))


def execution_chain(n,shot):
    from .renderer import PLAN
    i,a,u=execution_state(n,PLAN)
    s=Stage(n,'cold');s.floor();kx=455
    kh=(543,435);pose='hold'
    if i==2:pose='down'
    if i==7:kh=point(kh,(635,452),u)
    if i==9:kx-=14*u;kh=(535,459)
    body=s.actor('kris',kx,580,1.5,pose=pose,hands={'right':kh})
    target=body['chest'];heart=(98,112)
    if i<=4 or i>=10:
        nx=937+20*u if i==1 else 937
        wrist=(nx-77,455+22*u) if i==1 else (nx-94,435)
        if i==10:wrist=point(wrist,(765,280),u)
        s.actor('noelle',nx,580,1.25,hands={'left':wrist})
        if i in [0,1]:s.line([kh,wrist],RED,2)
        if i==2:target=wrist
        if i==3:
            # One frozen silhouette, not twelve bodies or a death assertion.
            x=1114;y=510
            s.poly([(x-40,y+65),(x-48,y-111),(x-13,y-133),(x+43,y-104),(x+49,y+65)],mix((31,50,69),ICE,u*.75),INK,3)
            s.poly([(x+9,y-103),(x+49,y-89),(x+13,y-75)],(108,138,155))
        if i==4:
            for x in [715,1020]:s.line([(x,610),(x+40,630)],(127,149,160),8)
        if i==11:
            selector=at(n,a['frame']+5,a['frame']+13)
            h=s.choice((973,485),left='Stop' if u<.6 else 'Proceed',width=326,selector=selector)
            heart=h;target=None
            s.line([(809,553),(1139-110*u,553)],(155,174,178),3)
            s.input(heart=False,pulse=1-u)
    elif i in [5,6]:
        s.tv(796,220,403,300)
        hx=970 if i==5 else lerp(970,747,u)
        hb=s.actor('hero',hx,482,.9,pose='walk',step=n/8);target=hb['chest']
    elif i==7:
        s.actor('susie',735-67*u,580,1.1,hands={'left':(644-67*u,458)})
        hb=s.actor('hero',1000,580,.95);target=hb['chest']
    elif i in [8,9]:
        s.line([(275,405),(398,405),(398,483),(707,483)],(99,125,144),4)
        s.line([(275,445),(365,445),(365,518),(707,518)],(99,125,144),4)
        heart=(350,425) if i==8 else point((350,425),body['chest'],u)
        target=None
    if i==10:s.line([(765,280),(770,191),(122,112)],(171,152,133),2)
    if heart==(98,112):s.input(target=target,pulse=1-u*.7)
    else:s.heart(heart,2.7)
    # Cold path trace remains after the freeze; no celebration or blood.
    if i>3:s.line([(1120,651),(1080,623),(1110,606)],(89,120,139),2)
    return s.finish()


def count_interfaces(n,shot):
    s,_,_=old.control_world(n)
    hx=lerp(970,935,at(n,3821,3902));body=s.actor('hero',hx,445,.72,pose='walk',step=n/11)
    for j,y in enumerate([73,112,151]):
        a=at(n,3821+j*14,3840+j*14)*(1-at(n,3880,3902))
        s.line([(35,y),(115,y),(165,112)],mix(INK,RED,a*.6),2)
    s.input(target=body['chest'])
    return s.finish()


def reentry(n,shot):
    # Relocate the same Ch4 mechanism to the lyric's have-back cue.
    virtual=2928+(n-4072)*86/92
    return old.reentry(virtual,shot)


def love_training(n,shot):
    s,body,wrist=old.lake_space(n,body_step=18*at(n,4344,4430))
    if n<4319:
        heart=body['chest'];s.line([wrist,(770,225),(99,112)],(132,158,164),2)
        # Warm contact residue recalls the earlier willing hands, not a literal
        # romance statement or proof that Noelle is freely consenting.
        s.line([body['right'],wrist],mix(INK,GOLD,at(n,4259,4319)*.6),2)
    elif n<4344:
        s.choice((720,490),alpha=at(n,4319,4344));heart=point(body['chest'],(617.5,528),at(n,4319,4344))
    else:
        heart=s.choice((720,490));s.line([(597,556),(616,556)],(136,159,170),2)
    s.heart(heart,2.8)
    return s.finish()


def love_algebra(n,shot):
    image=old.converged_choice(n,shot)
    if 4480<=n<4488:
        # Eight frames of an authorial UT text echo, never love's definition.
        d=ImageDraw.Draw(image);from .dr_ui import font,MONO
        d.text((1100,655),'LV',font=font(MONO,16),fill=(82,94,109))
    return image


SCENES={name:globals()[name] for name in [
'power_protection','pieces','parameters','discard','arrival','help_path','refusal','welcome','math_points','math_wave','mode_switch','party_breath','curiosity','first_execute','giving','cat_care','dependency','role_switch','shared_rhythm','absence','pruning','illegal_attempt','threshold','execution_chain','count_interfaces','screen_exit','protect','reentry','bed_drag','love_training','love_algebra','cease_input','continue_input','crt_reveal','hand_aftermath','final_pulse','chapter_cut','unresolved']}
