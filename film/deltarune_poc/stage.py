"""Authored geometric actors/space; original fan-art blocking, no game pixels.

Camera and poses are explicit functions of frame. Helpers never keep prev-frame
state. Cached gradient backgrounds are copied, never drawn into the cache.
"""
import math
from functools import lru_cache
from PIL import Image, ImageDraw
from . import dr_ui

W,H=1280,720
INK=(10,16,28)
WHITE=(231,233,242)
RED=(240,68,98)
ICE=(199,228,236)
GREEN=(117,165,139)
GOLD=(213,190,138)


def smooth(u):
    u=max(0,min(1,u))
    return u*u*(3-2*u)


def at(n,a,b):
    return smooth((n-a)/(b-a))


def lerp(a,b,u):
    return a+(b-a)*u


def mix(a,b,u):
    return tuple(round(lerp(x,y,u)) for x,y in zip(a,b))


def point(a,b,u):
    return (lerp(a[0],b[0],u),lerp(a[1],b[1],u))


PALETTES={
 "dark":((10,16,31),(25,39,59)),
 "warm":((25,30,43),(74,60,55)),
 "room":((25,23,44),(40,45,59)),
 "cold":((14,28,43),(43,57,69)),
 "lake":((16,32,49),(35,54,66)),
 "black":((0,0,0),(0,0,0))
}


@lru_cache(16)
def gradient(name):
    a,b=PALETTES[name]
    image=Image.new("RGB",(W,H))
    d=ImageDraw.Draw(image)
    for y in range(H):
        d.line((0,y,W,y),fill=mix(a,b,y/H))
    return image


class Stage:
    def __init__(self,n,palette="dark",camera=0,zoom=1):
        self.n=n
        self.image=gradient(palette).copy()
        self.d=ImageDraw.Draw(self.image)
        self.camera=camera
        self.zoom=zoom

    def p(self,xy):
        x,y=xy
        return (round((x-640)*self.zoom+640-self.camera),round((y-420)*self.zoom+420))

    def poly(self,points,fill,outline=None,width=1):
        pts=[self.p(p) for p in points]
        self.d.polygon(pts,fill=fill)
        if outline:
            self.d.line(pts+[pts[0]],fill=outline,width=max(1,round(width*self.zoom)))

    def line(self,points,fill=WHITE,width=2):
        self.d.line([self.p(p) for p in points],fill=fill,width=max(1,round(width*self.zoom)),joint="curve")

    def box(self,box,fill=None,outline=None,width=1):
        x1,y1,x2,y2=box
        self.d.rectangle((*self.p((x1,y1)),*self.p((x2,y2))),fill=fill,outline=outline,width=max(1,round(width*self.zoom)))

    def ellipse(self,box,fill,outline=None,width=1):
        x1,y1,x2,y2=box
        self.d.ellipse((*self.p((x1,y1)),*self.p((x2,y2))),fill=fill,outline=outline,width=max(1,round(width*self.zoom)))

    def text(self,xy,s,size=28,fill=WHITE,anchor="mm"):
        self.d.text(self.p(xy),s,font=dr_ui.font(dr_ui.MONO,max(1,round(size*self.zoom))),fill=fill,anchor=anchor)

    def heart(self,xy,scale=2,white=0):
        fill=mix(RED,ICE,white)
        points=[(-6,-3),(-6,-6),(-3,-8),(0,-5),(3,-8),(6,-6),(6,-3),(0,4)]
        x,y=xy
        self.poly([(x+a*scale,y+b*scale) for a,b in points],RED)
        if white:
            self.poly([(x+a*scale*.78,y+b*scale*.78) for a,b in points],fill)

    def hand(self,xy,scale=1,angle=0,fill=ICE,open=True):
        pts=[(-25,7),(-8,0),(3,-13),(9,-14),(11,-9),(4,1),(22,-2),(29,1),(28,6),
             (19,8),(28,9),(30,14),(17,17),(25,19),(24,24),(9,26),(-5,23),(-25,22)]
        if not open:
            pts=[(-25,7),(-5,3),(10,-1),(21,4),(23,16),(12,25),(-5,24),(-25,22)]
        c,s=math.cos(angle),math.sin(angle)
        x,y=xy
        self.poly([(x+(a*c-b*s)*scale,y+(a*s+b*c)*scale) for a,b in pts],fill,INK,2)

    def arm(self,shoulder,wrist,colour,scale=1,bend=1,skin=ICE):
        # Two visible limb segments with a controllable elbow, never a detached
        # static hand glyph. This is blocking, not final anatomical animation.
        dx,dy=wrist[0]-shoulder[0],wrist[1]-shoulder[1]
        length=max(1,math.hypot(dx,dy))
        elbow=((shoulder[0]+wrist[0])/2-dy/length*15*scale*bend,
               (shoulder[1]+wrist[1])/2+dx/length*15*scale*bend)
        self.line([shoulder,elbow,wrist],INK,19*scale)
        self.line([shoulder,elbow],colour,14*scale)
        self.line([elbow,wrist],skin,11*scale)
        self.hand(wrist,.45*scale,math.atan2(dy,dx)*.25,skin)

    def actor(self,who,x,floor,scale=1,pose="rest",step=0,hands=None,alpha=1,lean=0):
        # Distinct silhouettes, colours and world-space hands. All figures are
        # new shapes; DELTARUNE character references remain fan-work material.
        if alpha<=.004:
            return {"chest":(x,floor-118*scale),"left":(x-51*scale,floor-72*scale),"right":(x+53*scale,floor-70*scale)}
        props={
          "kris":(GREEN,(33,34,49),(189,176,143),GOLD),
          "susie":((102,58,110),(69,38,88),(170,117,178),(147,100,137)),
          "noelle":((161,132,104),(204,185,136),(221,201,170),(202,172,133)),
          "ralsei":((83,153,111),(219,221,206),(219,221,206),(229,155,171)),
          "hero":((205,211,211),(163,183,192),(214,225,228),(97,121,142)),
          "vessel":((101,110,127),(116,123,142),(136,143,155),(120,129,145))
        }
        shirt,hair,skin,stripe=props[who]
        dim=lambda c:mix(INK,c,alpha)
        shirt,hair,skin,stripe=map(dim,(shirt,hair,skin,stripe))
        crouch=pose in {"crouch","bed","down"}
        shift=45 if crouch else 0
        head_y=-172+shift
        torso_y=-147+shift
        # Local point transform includes an authored lean, not stateful physics.
        q=lambda a,b:(x+(a+lean*(-b/180))*scale,floor+b*scale)
        stride=math.sin(step)*10 if pose=="walk" else 0
        self.poly([q(-24,-45),q(-4,-43),q(-10+stride,-2),q(-36+stride,0)],dim((28,38,53)),INK,2)
        self.poly([q(4,-43),q(25,-43),q(36-stride,0),q(9-stride,-2)],dim((28,38,53)),INK,2)
        self.line([q(-36+stride,0),q(-9+stride,0)],dim((15,24,35)),8*scale)
        self.line([q(9-stride,0),q(38-stride,0)],dim((15,24,35)),8*scale)
        left=q(-29,torso_y+15)
        right=q(29,torso_y+15)
        wl=q(-51,-72+shift)
        wr=q(53,-70+shift)
        if pose=="walk":
            wl=q(-53,-76+math.cos(step)*10)
            wr=q(53,-76-math.cos(step)*10)
        if pose in {"hold","piano"}:
            wl=q(-13,-112+shift)
            wr=q(45,-99+shift)
        if hands:
            wl=hands.get("left",wl)
            wr=hands.get("right",wr)
        self.arm(left,wl,shirt,scale,bend=-1,skin=skin)
        self.arm(right,wr,shirt,scale,bend=1,skin=skin)
        self.poly([q(-29,torso_y),q(29,torso_y),q(39,-49+shift*.2),q(22,-36),q(-23,-36),q(-38,-49+shift*.2)],shirt,INK,2)
        self.poly([q(-32,-112+shift),q(33,-112+shift),q(35,-96+shift),q(-34,-96+shift)],stripe)
        self.poly([q(-21,head_y),q(20,head_y),q(26,head_y+26),q(12,head_y+42),q(-20,head_y+37)],skin,INK,2)
        if who=="kris":
            self.poly([q(-36,head_y-9),q(-22,head_y-30),q(9,head_y-34),q(34,head_y-16),q(31,head_y+25),q(15,head_y+13),q(0,head_y+19),q(-12,head_y+9),q(-33,head_y+29)],hair,INK,2)
        elif who=="susie":
            self.poly([q(-39,head_y-14),q(-11,head_y-34),q(33,head_y-19),q(41,head_y+35),q(25,head_y+42),q(15,head_y+8),q(-2,head_y+17),q(-23,head_y+10),q(-35,head_y+59)],hair,INK,2)
            self.poly([q(20,head_y+22),q(38,head_y+24),q(24,head_y+32)],skin)
            self.poly([q(25,head_y+26),q(29,head_y+27),q(27,head_y+32)],WHITE)
        elif who=="noelle":
            self.poly([q(-29,head_y-12),q(0,head_y-31),q(28,head_y-7),q(36,head_y+59),q(25,head_y+57),q(13,head_y+3),q(-2,head_y+10),q(-17,head_y+2),q(-25,head_y+54)],hair,INK,2)
            for sign in (-1,1):
                self.line([q(sign*18,head_y-16),q(sign*26,head_y-44),q(sign*23,head_y-61)],skin,4*scale)
                self.line([q(sign*25,head_y-42),q(sign*39,head_y-50)],skin,3*scale)
        elif who=="ralsei":
            self.poly([q(-39,head_y-8),q(5,head_y-78),q(36,head_y-8)],shirt,INK,2)
            self.line([q(-15,head_y+14),q(15,head_y+14)],INK,2*scale)
        elif who=="hero":
            self.poly([q(-31,head_y-13),q(4,head_y-33),q(32,head_y-12),q(32,head_y+10),q(-31,head_y+10)],hair,INK,2)
            self.poly([q(-30,torso_y),q(-63,-39),q(-32,-45)],dim((118,145,166)),INK,2)
            self.line([q(18,head_y+16),q(29,head_y+16)],dim((46,65,86)),3*scale)
        else:
            self.ellipse((*q(-29,head_y-16),*q(29,head_y+37)),skin,INK,2)
        return {"chest":q(0,-118+shift),"left":wl,"right":wr,"head":q(0,head_y)}

    def input(self,xy=(98,112),target=None,pulse=1,heart=True):
        # The input source is screen anchored, unlike its world-space target.
        # The camera may follow the wrong actor without deleting our reference.
        x=(xy[0]+self.camera-640)/self.zoom+640
        y=(xy[1]-420)/self.zoom+420
        for i in range(3):
            self.line([(x-25-i*16,y-2),(x-15-i*16,y-2)],mix(INK,RED,pulse*.5),2)
        if heart:
            self.heart((x,y),2.5)
        if target:
            tx,ty=target
            self.line([(x+22,y),(x+68,y),(tx,ty)],mix(INK,RED,.58),2)
            self.ellipse((tx-4,ty-4,tx+4,ty+4),RED)

    def floor(self,y=550,warm=False):
        self.poly([(0,y),(W,y-20),(W,H),(0,H)],(35,39,49) if warm else (17,29,45))
        self.line([(0,y),(W,y-20)],(91,87,89) if warm else (54,69,86),2)
        for i in range(8):
            x=i*190-70
            self.line([(640+(x-640)*.15,y),(x,H)],(40,46,59),1)

    def room(self,warm=False):
        self.box((55,120,1260,570),fill=(30,29,45) if warm else (23,29,47))
        self.box((875,145,1120,385),fill=(142,123,93) if warm else (63,91,112),outline=(20,27,43),width=10)
        self.line([(997,150),(997,380)],(33,37,54),6)
        self.line([(880,265),(1115,265)],(33,37,54),6)
        self.poly([(880,385),(1118,385),(774,600),(423,600)],(59,53,57) if warm else (36,49,64))
        self.floor(560,warm)

    def road(self,warm=True):
        self.poly([(0,440),(210,380),(410,425),(650,358),(900,410),(1120,360),(W,410),(W,H),(0,H)],(34,46,50))
        self.poly([(0,540),(W,505),(W,H),(0,H)],(43,46,52))
        self.poly([(510,505),(695,505),(1095,H),(200,H)],(67,62,60) if warm else (41,55,66))
        for x,h in [(90,150),(210,105),(1100,132),(1180,192)]:
            self.box((x,440-h,x+60,500),fill=(27,38,48))
            self.box((x+17,456-h,x+29,471-h),fill=(151,131,94) if warm else (86,119,135))

    def water(self,level=420):
        self.poly([(0,level-30),(210,level-65),(445,level-28),(650,level-49),(900,level-15),(W,level-35),(W,H),(0,H)],(18,33,48))
        self.poly([(0,level),(W,level-9),(W,H),(0,H)],(25,46,61))
        for i in range(13):
            y=level+15+i*20
            for j in range(5):
                x=43+j*259+18*math.sin(self.n/70+i*.7+j)
                self.line([(x,y),(x+90+14*math.sin(i),y)],(51,76,87),1)
        self.line([(0,level),(W,level-9)],(84,112,123),2)

    def choice(self,center=(640,455),left="Stop",right="Proceed",selector=0,left_alpha=1,alpha=1,width=410):
        x,y=center
        if alpha<=0:
            return (x-width*.25+width*.5*selector,y+38)
        before=self.image.copy() if alpha<1 else None
        self.box((x-width/2,y-62,x+width/2,y+70),fill=INK,outline=mix(INK,WHITE,alpha),width=2)
        if left:
            self.text((x-width*.25,y-20),left,27,mix(INK,WHITE,left_alpha*alpha))
        if right:
            self.text((x+width*.25,y-20),right,27,mix(INK,WHITE,alpha))
        if before is not None:
            self.image=Image.blend(before,self.image,alpha)
            self.d=ImageDraw.Draw(self.image)
        return (x-width*.25+width*.5*selector,y+38)

    def cage(self,x=350,y=450,alpha=1):
        col=mix((23,29,47),(123,139,153),alpha)
        self.line([(x-78,y+65),(x-78,y-45),(x-48,y-90),(x+48,y-90),(x+78,y-45),(x+78,y+65),(x-78,y+65)],col,3)
        for off in [-52,-26,0,26,52]:
            self.line([(x+off,y-50),(x+off,y+65)],col,2)

    def tv(self,x=795,y=190,w=445,h=315):
        self.poly([(x+12,y-12),(x+w-6,y-16),(x+w+28,y+14),(x+w+28,y+h+10),(x+w-18,y+h+33),(x-9,y+h+20),(x-12,y+14)],(56,68,80),INK,4)
        self.box((x+10,y+10,x+w-39,y+h-26),fill=(13,30,43),outline=(105,131,140),width=3)
        self.poly([(x+70,y+h+33),(x+w-65,y+h+33),(x+w-36,y+h+66),(x+42,y+h+66)],(28,36,48))
        self.line([(x+85,y+h+67),(x+68,y+h+131)],(30,37,48),12)
        self.line([(x+w-80,y+h+67),(x+w-64,y+h+131)],(30,37,48),12)
        for yy in (y+h-65,y+h-105):
            self.ellipse((x+w-25,yy,x+w-6,yy+19),(133,141,151),INK,2)
        for yy in range(y+36,y+90,7):
            self.line([(x+w-27,yy),(x+w-7,yy)],(91,107,121),2)

    def finish(self):
        return self.image

