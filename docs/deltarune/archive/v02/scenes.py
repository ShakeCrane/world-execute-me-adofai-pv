"""v02 authored blocking: every scene owns a different action/camera intention.

These are geometric director studies, not original-game continuous footage.
Chapter thematic cuts and branch compression are identified in the shot plan.
"""
import math
from PIL import Image, ImageDraw
from .stage import Stage,at,lerp,point,mix,INK,WHITE,RED,ICE,GREEN,GOLD


def control_world(n,camera=0,kx=355,sx=610,khand=None,shand=None,plug_shift=0):
    s=Stage(n,"dark",camera=camera)
    s.room(False)
    s.tv()
    kh={"left":(kx+25,429),"right":(kx+76,427)} if khand is None else {"right":khand}
    sk=s.actor("kris",kx,550,1.15,pose="hold",hands=kh)
    ss=s.actor("susie",sx,550,1.3,hands=shand)
    # The plug exists in world space, not as a sidebar "refusal" glyph.
    s.line([(835,503),(718,590),(565,495)],(122,138,149),3)
    s.line([(565-plug_shift,495),(458,465),(kx+70,433)],(93,115,133),3)
    s.box((552-plug_shift,487,570-plug_shift,503),fill=(160,178,189),outline=INK,width=2)
    s.box((570,487,586,503),fill=(67,87,106),outline=INK,width=2)
    s.box((kx+16,416,kx+80,443),fill=(70,89,111),outline=INK,width=2)
    return s,sk,ss


def tv_intro(n,shot):
    s,_,_=control_world(n)
    hx=lerp(955,918,at(n,1145,1190))
    s.actor("hero",hx,449,.7,pose="walk",step=n/13)
    s.line([(840,442),(1210,442)],(73,99,111),2)
    s.input(target=(hx,365),pulse=.45+.4*math.sin(n/14)**2)
    return s.finish()


def sword_pressure(n,shot):
    push=at(n,3412,3500)
    s,_,_=control_world(n,camera=45*push)
    # Directional attempt and retreat, rather than unexplained random glitch.
    x=952-22*math.sin((n-3323)/21)
    s.actor("hero",x,446,.75,pose="walk",step=n/9)
    s.poly([(870,442),(878,412),(889,442)],(133,158,163))
    s.line([(891,335),(891,443)],(87,112,126),3)
    s.input(target=(x,355),pulse=.5+.45*math.sin(n/10)**2)
    return s.finish()


def target_shift(n,shot):
    s,_,_=control_world(n)
    hx=lerp(970,935,at(n,3821,3902))
    s.actor("hero",hx,445,.72,pose="walk",step=n/11)
    s.input(target=point((430,414),(hx,357),at(n,3821,3880)))
    return s.finish()


def screen_exit(n,shot):
    cam=220*at(n,3902,3962)
    hx=lerp(935,680,at(n,3902,3962))
    fy=lerp(445,550,at(n,3902,3938))
    scale=lerp(.72,1.05,at(n,3902,3938))
    kx=355-24*at(n,3926,3942)
    s,_,_=control_world(n,camera=cam,kx=kx)
    body=s.actor("hero",hx,fy,scale,pose="walk",step=n/9,lean=-3)
    # Carrier is drawn AFTER the bezel; it can cross the physical plane.
    s.input(target=body["chest"])
    s.line([(hx-5,fy-70),(hx-53,fy-120)],(195,215,224),5)
    return s.finish()


def protect(n,shot):
    pull=at(n,4012,4030)
    sx=610-110*pull
    kx=lerp(331,490,at(n,4000,4012))-100*pull
    cam=220*(1-pull)
    grip=point((407,427),(544,456),at(n,4000,4012))
    if n>=4012:
        grip=(sx-66,456)
    dis=at(n,4052,4064)
    susie_hand=point((sx+69,459),(565,495),at(n,4040,4052))
    if n>=4052:
        susie_hand=(565-40*dis,495)
    s,_,_=control_world(n,cam,kx,sx,khand=grip,shand={"right":susie_hand},plug_shift=40*dis)
    hero_alpha=1-dis
    s.actor("hero",680,550,1.05,pose="hold",alpha=hero_alpha)
    # Wind-up identifies the OLD Susie position, then the stroke lands there
    # after the characters have moved. No red gore or "freedom" celebration.
    wind=at(n,3988,4000)
    s.line([(677,463),(650-40*wind,390+60*wind)],mix(INK,WHITE,hero_alpha),5)
    if 3988<=n<4030:
        s.line([(603,549),(617,549)],(171,151,133),2)
    if 4030<=n<4040:
        hit=at(n,4030,4039)
        s.line([(676,454),(610,lerp(436,552,hit))],(238,225,200),7)
        s.line([(598,554),(622,554)],(238,225,200),3)
    # Input stays on HERO through the protective body action. Only unplugging
    # breaks the last segment; the source SOUL survives the disconnection.
    if dis<.999:
        s.input(target=(680,427))
    else:
        s.input()
    return s.finish()


def separation(n,shot):
    s=Stage(n,"room")
    s.room(True)
    chest=(620,359.4)
    if n<2650:
        heart=chest
        wrist=point((676,441),chest,at(n,2644,2650))
    elif n<2662:
        heart=point(chest,(548,373),at(n,2650,2662)); wrist=(heart[0]+4,heart[1]+13)
    elif n<2674:
        heart=point((548,373),(520,384),at(n,2662,2674)); wrist=(heart[0]+4,heart[1]+13)
    else:
        heart=point((520,384),(350,450),at(n,2674,2693)); wrist=(heart[0]+4,heart[1]+13)
    s.cage(alpha=at(n,2674,2693))
    s.actor("kris",620,560,1.7,pose="hold",hands={"left":wrist})
    s.heart(heart,3)
    if n<2662:
        s.line([(93,112),(141,112),heart],mix(INK,RED,.65*(1-at(n,2650,2662))),2)
    return s.finish()


def private_space(s,body_alpha=1,noelle_alpha=1,gesture=0):
    s.room(True)
    s.box((709,170,740,586),fill=(38,35,48),outline=(102,94,92),width=3)
    s.box((1170,170,1195,588),fill=(38,35,48))
    s.line([(740,174),(1174,174)],(100,91,93),7)
    s.actor("kris",840,520,1.15,pose="hold",hands={"right":(919,403+gesture)},alpha=body_alpha)
    s.actor("noelle",1030,520,1.05,hands={"left":(936,402)},alpha=noelle_alpha)
    s.line([(178,428),(450,428),(450,452),(700,452)],(106,124,140),5)
    s.line([(178,474),(451,474),(451,498),(700,498)],(106,124,140),5)
    for x in range(190,451,27):
        s.line([(x,428),(x,474)],(73,91,111),2)


def isolated(n,shot):
    match=at(n,2784,2838)
    z=1-.2*at(n,2693,2728)
    s=Stage(n,"room",zoom=z)
    if n<2784:
        s.room(True)
        s.cage()
        hx=350+18*math.sin((n-2693)/11)*at(n,2693,2705)
        kx=620+240*at(n,2728,2784)
        s.actor("kris",kx,560,1.7,pose="walk" if n>=2728 else "hold",step=(n-2728)/10)
        s.heart((hx,450),3)
    else:
        # Explicit thematic match to Ch4; no assertion that a birdcage opens
        # into this vent in the actual game. The SOUL remains the visual anchor.
        private_space(s,noelle_alpha=match)
        s.cage(alpha=1-at(n,2784,2808))
        s.heart((lerp(350,430,match),450),3)
    return s.finish()


def private(n,shot):
    s=Stage(n,"room",zoom=.8)
    private_space(s,gesture=4*math.sin(n/21))
    s.heart((430,450),3)
    return s.finish()


def reentry(n,shot):
    s=Stage(n,"room",zoom=.8)
    private_space(s)
    menu_op=at(n,2928,2940)
    s.box((697,350,751,470),fill=INK,outline=mix(INK,WHITE,menu_op),width=2)
    if menu_op>0:
        s.text((724,374),"Proceed",16,mix(INK,WHITE,menu_op))
    if n<2940:
        heart=(430,450)
    elif n<2972:
        heart=point((430,450),(724,428),at(n,2940,2972))
    else:
        heart=point((724,428),(840,384.3),at(n,2972,2996))
    s.heart(heart,3)
    if n>=2996:
        s.line([(93,112),(141,112),heart],mix(INK,RED,at(n,2996,3014)*.65),2)
    return s.finish()


def blank_reply(n,shot):
    s=Stage(n,"cold")
    s.floor()
    s.actor("kris",425,550,1.3,pose="hold")
    s.actor("susie",799,550,1.4,pose="rest")
    for i in range(10):
        x=92+i*124
        yy=95+(n*4+i*51)%432
        s.line([(x,yy),(x-7,yy+20)],(77,94,106),1)
    for i in range(4):
        xx=435+i*127
        s.box((xx,581,xx+105,626),fill=INK,outline=(93,112,130),width=1)
    heart=point((98,112),(461,611),at(n,4072,4100))
    if n>=4100:
        heart=point((461,611),(588,611),at(n,4100,4130))
    s.heart(heart,2.4)
    return s.finish()


def vessel(n,shot):
    s=Stage(n,"dark")
    a=at(n,8,93)
    s.actor("vessel",640,560,1.3,alpha=a,hands={"left":point((445,570),(584,458),a),"right":point((850,570),(713,458),a)})
    if n<8:
        s.ellipse((637-n*.7,326-n*.7,643+n*.7,332+n*.7),RED)
    else:
        s.heart(point((640,330),(550,645),at(n,8,93)),2.7)
    if n>=93:
        s.text((640,638),"ACCEPT",27)
    # Four inviting corners, never a complete explanatory rectangle.
    c=mix(INK,(110,137,148),a)
    for x,sign in [(445,1),(835,-1)]:
        s.line([(x,290),(x,268),(x+sign*22,268)],c,2)
    return s.finish()


def arrival(n,shot):
    s=Stage(n,"room")
    s.room(True)
    s.actor("vessel",640,560,1.3,alpha=1-at(n,130,142))
    alpha=at(n,142,156)
    hand=(726,432-10*at(n,243,306))
    s.actor("kris",640,560,1.6,alpha=alpha,hands={"right":hand})
    s.heart(point((550,645),(640,371.2),at(n,130,177)),2.7)
    if 156<=n<243:
        s.text((640,643),"KRIS",24,mix(INK,(160,166,181),at(n,156,177)))
    return s.finish()


def help_path(n,shot):
    s=Stage(n,"warm")
    s.road()
    s.poly([(566,535),(626,533),(685,H),(480,H)],(11,20,33))
    if n<385:
        kx=lerp(430,570,at(n,306,385)); fy=550
    else:
        p=at(n,385,432); kx=lerp(570,720,p); fy=550-36*math.sin(p*math.pi)
    sx=850+65*at(n,385,476)
    body=s.actor("kris",kx,fy,1.3,pose="walk",step=(n-306)/12)
    s.actor("susie",sx,550,1.4,pose="walk",step=(n-330)/14)
    s.heart(body["chest"],2.4)
    s.input(heart=False,pulse=.8 if n<385 else .25)
    return s.finish()


def refusal(n,shot):
    s=Stage(n,"warm")
    s.road()
    body=s.actor("kris",720,550,1.3,pose="hold")
    sx=915+165*at(n,500,535)
    s.actor("susie",sx,550,1.4,pose="walk" if n<535 else "rest",step=n/8,lean=9*at(n,476,500))
    s.heart(body["chest"],2.4)
    s.input(heart=False,pulse=1-at(n,476,500))
    return s.finish()


def welcome(n,shot):
    s=Stage(n,"warm")
    s.road()
    sx=lerp(1080,860,at(n,567,615))
    respond=at(n,615,655)
    kh=point((789,459),(823,404),respond)
    sh=point((sx-72,449),(834,405),respond)
    body=s.actor("kris",720,550,1.3,hands={"right":kh})
    s.actor("susie",sx,550,1.4,pose="walk" if n<615 else "rest",step=n/14,hands={"left":sh})
    s.heart(body["chest"],2)
    return s.finish()


def body_projection(n,shot):
    s=Stage(n,"warm")
    s.floor(warm=True)
    s.poly([(250,150),(350,128),(944,H),(691,H)],(53,58,68))
    body=s.actor("kris",600,560,1.55,pose="hold",hands={"right":(693,435)})
    for i in range(28):
        theta=i/28*math.pi*2+(n-715)/160
        r=85+35*at(n,715,803)
        x=600+math.cos(theta)*r*2
        y=574+math.sin(theta)*r*.32
        s.ellipse((x-2,y-2,x+2,y+2),mix((54,60,76),GOLD,.55))
    s.heart(body["chest"],2)
    return s.finish()


def keyboard(s,highlight=0):
    s.poly([(420,540),(805,497),(1010,642),(533,710)],(163,161,150),INK,4)
    for i in range(13):
        t=i/12
        a=point((420,540),(805,497),t)
        b=point((533,710),(1010,642),t)
        s.line([a,b],INK,2)
        if i<12 and i%3!=0:
            s.poly([a,(a[0]+20,a[1]-2),(lerp(a[0],b[0],.6)+20,lerp(a[1],b[1],.6)),point(a,b,.6)],(24,31,42))
    t=(highlight%12)/12
    x,y=point((420,540),(805,497),t)
    s.line([(x+9,y+1),(x+62,y+68)],(201,194,148),4)


def organ_intro(n,shot):
    s=Stage(n,"warm")
    s.room(True)
    body=s.actor("kris",600,550,1.35,pose="piano",hands={"left":(565,552-6*math.sin(n/9)**2),"right":(727,526-6*math.cos(n/11)**2)})
    keyboard(s,(n//24)%12)
    s.heart(body["chest"],2)
    return s.finish()


def party_breath(n,shot):
    s=Stage(n,"warm",camera=25*at(n,1235,1417))
    s.road()
    walk=n<1322
    progress=50*at(n,1235,1322)
    body=s.actor("kris",430+progress,565+math.sin(n/19),1.3,pose="walk" if walk else "rest",step=n/16)
    s.actor("susie",700+progress,565,1.35,pose="walk" if walk else "rest",step=n/18)
    s.actor("ralsei",980+progress,565,.95,pose="walk" if walk else "rest",step=n/20)
    s.heart(body["chest"],1.6)
    return s.finish()


def puppet(s,x,y,fall=0):
    # Original shorthand for the strings/fall mirror: angular mechanism, long
    # nose and two different lens colours; it never replaces Kris as subject.
    s.poly([(x-70,y+5),(x-176,y-61),(x-133,y-67),(x-57,y-17)],(104,137,151),INK,2)
    s.poly([(x+57,y-15),(x+139,y-67),(x+178,y-56),(x+68,y+6)],(104,137,151),INK,2)
    s.poly([(x-35,y-10),(x+35,y-10),(x+55,y+65),(x-36,y+76)],(156,174,142),INK,3)
    s.poly([(x-37,y-61),(x+12,y-83),(x+42,y-59),(x+22,y-8),(x-33,y-17)],(221,222,207),INK,2)
    s.poly([(x+20,y-53),(x+81,y-39),(x+27,y-29)],(221,222,207),INK,2)
    s.box((x-27,y-52,x-6,y-38),fill=(213,145,171))
    s.box((x+2,y-52,x+23,y-38),fill=(216,210,132))
    s.line([(x-4,y+66),(x-20,y+110)],(89,123,126),8)
    s.line([(x+30,y+66),(x+59,y+107)],(89,123,126),8)


def last_wire(n,shot):
    s=Stage(n,"dark")
    s.floor()
    body=s.actor("kris",390,560,1.55,pose="hold",hands={"right":point((472,451),(520,426),at(n,1513,1578))})
    puppet(s,875,340)
    s.line([(875,93),(875,257)],(150,187,158),3)
    if n>=1578:
        s.ellipse((867,249,883,265),GOLD)
    s.heart((515,412),2.7)
    return s.finish()


def wire_fall(n,shot):
    s=Stage(n,"dark")
    s.floor()
    dy=140*at(n,1591,1637)
    puppet(s,875,340+dy)
    s.line([(875,93),(875+10*math.sin(n/18),225)],(115,151,135),2)
    s.actor("kris",390,560,1.55,pose="hold",hands={"right":(520,426)})
    s.heart((515,412),2.7)
    return s.finish()


def organ_care(n,shot):
    s=Stage(n,"warm",camera=-70)
    s.room(True)
    body=s.actor("kris",540,550,1.55,pose="piano",hands={"left":(525,548-5*math.sin(n/14)),"right":(690,525-5*math.cos(n/14))},lean=2*math.sin(n/22))
    keyboard(s,(n//36)%12)
    s.heart(body["chest"],1.8)
    return s.finish()


def friend_breath(n,shot):
    s=Stage(n,"warm")
    s.road()
    body=s.actor("kris",500+22*at(n,1951,1991),560,1.4,pose="walk" if n<1991 else "rest",step=n/18)
    s.actor("susie",837,560,1.4,hands={"left":(752,407-13*at(n,1991,2043))})
    s.heart(body["chest"],1.8)
    return s.finish()


def save_identity(n,shot):
    s=Stage(n,"warm")
    s.road()
    body=s.actor("kris",530,560,1.6,pose="hold")
    s.heart(body["chest"],1.8)
    c=mix(INK,WHITE,at(n,2043,2080))
    s.box((770,300,1090,440),fill=INK,outline=c,width=2)
    s.text((930,330),"SAVE",23,c)
    s.text((930,389),"KRIS" if n<2080 else "CREATOR",31,c)
    return s.finish()


def light_dark(n,shot):
    s=Stage(n,"room")
    s.room(True)
    p=at(n,2205,2382)
    edge=1050-920*p
    s.poly([(edge,0),(W,0),(W,H),(edge-90,H)],(19,35,57))
    body=s.actor("kris",530+115*p,560,1.6,pose="walk",step=n/20,hands={"right":(edge,315)})
    s.heart(body["chest"],2)
    return s.finish()


def shared_rhythm(n,shot):
    s=Stage(n,"warm")
    s.room(True)
    p=at(n,2485,2530)
    hands={"right":point((730,449),(679,434),p)}
    body=s.actor("kris",620,560,1.7,pose="hold",hands=hands)
    s.actor("susie",940,560,1.1,hands={"left":point((884,480),(837,436),p)},alpha=1-at(n,2530,2571)*.7)
    s.heart(body["chest"],3)
    return s.finish()


def route_gates(n,shot):
    s=Stage(n,"cold")
    s.poly([(130,630),(390,610),(570,390),(980,340),(1130,152),(891,142),(790,277),(462,331)],(56,68,73))
    p=at(n,3014,3093)
    x=lerp(777,495,p); y=lerp(363,500,p)
    body=s.actor("kris",x,y,.9,pose="walk",step=n/11)
    for xx,yy in [(840,270),(659,353),(435,520)]:
        s.line([(xx-30,yy-25),(xx+30,yy+25)],(140,163,167),7)
    s.heart(body["chest"],2.4)
    return s.finish()


def lock_recoil(n,shot):
    if n<3149:
        s=Stage(n,"cold",zoom=1.2)
        s.floor()
        p=at(n,3093,3117)
        left=point((620,441),(738,437),p)
        s.actor("kris",545,560,1.4,hands={"right":left})
        s.actor("noelle",915,560,1.3,hands={"left":(753,438)})
        s.heart((515,395),2.5)
        crack=at(n,3117,3149)
        if crack:
            s.line([(738,437),(749,426),(744,417),(760,411)],mix(INK,RED,crack),3)
            s.line([(749,426),(760,432),(770,421)],mix(INK,RED,crack),2)
    else:
        s=Stage(n,"room")
        s.room(False)
        hx,hy=point((620,394),(460,490),at(n,3149,3185))
        s.box((390,445,520,569),fill=(52,62,76),outline=(106,119,130),width=3)
        jolt=5*math.sin((n-3185)*2)*(1-at(n,3185,3209)) if n>=3185 else 0
        s.actor("kris",620+jolt,560,1.4,pose="hold",hands={"left":(hx+9,hy+12)})
        if 3185<=n<3209:
            s.line([(598,536),(534+jolt,555),(501+jolt,565)],(159,171,173),12)
        s.heart((hx+jolt,hy),3)
    return s.finish()


def down_command(n,shot):
    s=Stage(n,"cold")
    s.floor()
    s.actor("kris",448,556,1.7,pose="down",lean=28)
    s.actor("noelle",965,548,1.15,hands={"right":(1038,381-12*at(n,3270,3323))})
    s.input(target=(993,391),pulse=.4+.5*math.sin(n/9)**2)
    for i in range(3):
        s.poly([(799+i*88,536),(832+i*88,513),(861+i*88,539),(860+i*88,568),(796+i*88,566)],(61,87,108),INK,2)
    return s.finish()


PULSES=[3549,3569,3594,3618,3640,3662,3682,3705,3727,3749,3773,3795]


def execution(n,shot):
    count=sum(n>=p for p in PULSES)
    push=at(n,3682,3821)
    s=Stage(n,"cold",zoom=1+push*.13,camera=push*35)
    s.floor()
    for i,p in enumerate(PULSES):
        if n>=p:
            grow=at(n,p,p+12)
            x=140+i*89
            h=(55+i*9)*grow
            s.poly([(x,550),(x+12,550-h),(x+35,537-h),(x+43,550),(x+30,581)],mix((26,47,67),(107,146,163),.45+i*.015),INK,2)
    kh=(545+count*2,407-7*math.sin(n/11))
    s.actor("kris",458,554,1.5,hands={"right":kh})
    s.actor("noelle",924,554,1.25,hands={"left":(818-count*2,393-4*math.sin(n/14))})
    last=max((p for p in PULSES if p<=n),default=3549)
    strength=1-at(n,last,last+12)
    s.input(target=kh,pulse=.2+.8*strength)
    s.line([kh,(688,413),(797,413)],mix(INK,ICE,strength*.6),2)
    return s.finish()


def bed_drag(n,shot):
    s=Stage(n,"room",zoom=1.18,camera=105)
    s.room(False)
    s.poly([(289,278),(722,283),(835,452),(256,472)],(64,73,88),INK,4)
    s.poly([(280,313),(714,317),(814,445),(264,453)],(141,150,159),INK,3)
    lift=9*at(n,4164,4259)
    body=s.actor("kris",640,609-lift,1.6,pose="bed",hands={"left":(516,600-lift),"right":(727,598-lift)},lean=-13)
    s.heart(body["chest"],2.4)
    s.input(heart=False,pulse=.15+.85*math.sin((n-4164)/7)**2)
    return s.finish()


def lake_space(n,zoom=1,camera=0,hand_shift=0,body_step=0,noelle_alpha=1):
    s=Stage(n,"lake",zoom=zoom,camera=camera)
    s.water(420+6*at(n,4574,4654))
    lead=at(n,4259,4319)
    nx=lerp(990,875,lead)
    wrist=point((929,484),(770,392),lead)
    wrist=point(wrist,(670+hand_shift,421),at(n,4319,4344))
    khand=point((547,444),(641+body_step,425),at(n,4319,4344))
    s.actor("noelle",nx,560,1.2,hands={"left":wrist},alpha=noelle_alpha)
    body=s.actor("kris",460+body_step,560,1.65,hands={"right":khand},lean=-2*math.sin(n/23))
    # World leaves cold residue rather than wiping the action's consequences.
    s.line([(1061,573),(1088,552),(1102,563),(1120,550),(1142,570)],(94,126,144),2)
    s.line([(377,563),(574,560)],(79,110,124),2)
    return s,body,wrist


def noelle_lead(n,shot):
    step=18*at(n,4344,4430)
    s,body,wrist=lake_space(n,body_step=step)
    if n<4319:
        heart=body["chest"]
        s.line([wrist,(770,225),(99,112)],(132,158,164),2)
    elif n<4344:
        # The same visual SOUL changes interface position, not a new extraction
        # caused by Noelle; the plan labels this as authored UI/world staging.
        s.choice((720,490),alpha=at(n,4319,4344))
        heart=point(body["chest"],(617.5,528),at(n,4319,4344))
    else:
        heart=s.choice((720,490))
        s.line([(597,556),(616,556)],(136,159,170),2)
    s.heart(heart,2.8)
    return s.finish()


def converged_choice(n,shot):
    s,_,_=lake_space(n,zoom=1.4,camera=70,body_step=18)
    left="Stop" if n<4442 else "Proceed"
    alpha=1 if n<4436 or n>=4448 else (1-at(n,4436,4442) if n<4442 else at(n,4442,4448))
    cursor=at(n,4448,4460)
    heart=s.choice((720,490),left=left,left_alpha=alpha,selector=cursor)
    s.heart(heart,2.8)
    s.line([(597,556),(616,556)],(136,159,170),2)
    return s.finish()


def cease_input(n,shot):
    z=lerp(1.4,1,at(n,4519,4531))
    cam=70*(1-at(n,4519,4531))
    s,_,_=lake_space(n,z,cam,body_step=18,noelle_alpha=1-.35*at(n,4531,4543))
    a=1-at(n,4519,4531)
    if a>0:
        s.choice((720,490),left="Proceed",selector=1,alpha=a)
    s.heart((822.5,528),2.8)
    # An echo of the already-established caring character, not new pause UI.
    s.actor("susie",237,568,.93,alpha=.36*at(n,4531,4543),hands={"right":(304,437)})
    return s.finish()


def continue_input(n,shot):
    hand=18*at(n,4574,4601)
    s,_,_=lake_space(n,hand_shift=hand,body_step=18)
    s.actor("susie",237,568,.93,alpha=.25,hands={"right":(304,437)})
    width=410-170*at(n,4574,4601) if n<4601 else 410-190*at(n,4601,4621)
    c=(720-hand,490)
    s.choice(c,left=None,right=None,width=width)
    s.text((c[0],470),"Proceed",27)
    heart=point((822.5,528),(720-hand,528),at(n,4574,4601))
    s.heart(heart,2.8,white=.8*at(n,4574,4654))
    return s.finish()


def crt_reveal(n,shot):
    u=at(n,4654,4814)
    # The image is authored for this time, never a static screenshot filler.
    image=continue_input(n,shot)
    out=Stage(n,"room")
    out.room(False)
    w=round(lerp(1280,940,u)); h=round(w*720/1280)
    x=round(lerp(0,170,u)); y=round(lerp(0,48,u))
    out.poly([(x-32,y-25),(x+w+20,y-25),(x+w+58,y+10),(x+w+58,y+h+55),(x+w+18,y+h+78),(x-35,y+h+55),(x-35,y)],(57,71,84),INK,5)
    out.poly([(x+100,y+h+76),(x+w-75,y+h+76),(x+w-15,y+h+108),(x+55,y+h+108)],(31,42,55),INK,3)
    out.line([(x+165,y+h+109),(x+146,H)],(18,27,38),17)
    out.line([(x+w-127,y+h+109),(x+w-112,H)],(18,27,38),17)
    out.image.paste(image.resize((w,h),Image.Resampling.BICUBIC),(x,y))
    d=ImageDraw.Draw(out.image)
    for yy in [y+h+12,y+h+42]:
        d.ellipse((x+w-50,yy,x+w-26,yy+24),fill=(128,148,160),outline=INK,width=3)
    plug=at(n,4734,4814)
    out.line([(x-27,y+h+29),(128,652),(88,652)],mix(INK,(155,179,187),plug),3)
    out.box((65,640,89,665),fill=mix(INK,(138,161,177),plug),outline=INK,width=2)
    return out.finish()


def portrait(n,palette="lake",alpha=1):
    s=Stage(n,palette)
    if palette!="black":
        s.water(463)
    hand_x=600+30*at(n,4863,4895)
    cuff=mix((0,0,0),GREEN,alpha)
    skin=mix((0,0,0),(189,176,143),alpha)
    s.poly([(158,399),(444,400),(hand_x-60,390),(hand_x-56,447),(451,493),(166,492)],cuff,INK,3)
    s.line([(252,403),(247,489)],mix((0,0,0),GOLD,alpha),15)
    s.hand((hand_x,405),2.6,angle=-.11,fill=skin)
    if alpha>0:
        s.heart((755,417),4.2,white=0)
    return s


def hand_aftermath(n,shot):
    return portrait(n).finish()


def final_pulse(n,shot):
    s=portrait(n)
    if n<4935:
        s.ellipse((687,414,701,428),mix(INK,GOLD,1-at(n,4929,4935)))
    image=s.finish()
    if n>=4962:
        h=max(1,round(720*(4969-n)/7))
        out=Image.new("RGB",(1280,720),(0,0,0))
        out.paste(image.resize((1280,h),Image.Resampling.NEAREST),(0,360-h//2))
        return out
    return image


def chapter_cut(n,shot):
    s=Stage(n,"black")
    if n>=4994:
        a=at(n,4994,5002)*(1-at(n,5026,5030))
        s.text((640,331),"Insert Chapter 7",32,mix((0,0,0),WHITE,a))
        s.text((640,379),"Side B",32,mix((0,0,0),WHITE,a))
    return s.finish()


def unresolved(n,shot):
    a=at(n,5030,5048)
    s=portrait(n,"black",a*.8)
    if n>=5051:
        s.text((640,565),"Who executes whom?",35,mix((0,0,0),WHITE,at(n,5051,5057)))
    return s.finish()


SCENES={name:globals()[name] for name in [
 "vessel","arrival","help_path","refusal","welcome","body_projection","organ_intro","tv_intro","party_breath",
 "last_wire","wire_fall","organ_care","friend_breath","save_identity","light_dark","shared_rhythm","separation",
 "isolated","private","reentry","route_gates","lock_recoil","down_command","sword_pressure","execution",
 "target_shift","screen_exit","protect","blank_reply","bed_drag","noelle_lead","converged_choice","cease_input",
 "continue_input","crt_reveal","hand_aftermath","final_pulse","chapter_cut","unresolved"]}
