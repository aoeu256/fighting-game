from ika import Video, RGB, Random
#from outline import Lines
from math import cos, sin, atan2, pi

class SysObj(object):
    def __init__(self, area, x, y, p=None, o=None, t=30):
        self.p, self.o = p, o
        self.x, self.y, self.t = x, y, t
        self.maxt = t
        self.dt = lambda: self.maxt - self.t
        self.drange = lambda x: self.dt()*x/self.maxt
        self.rrange = lambda x: self.t*x/self.maxt
        self.area = area
        self.rx, self.ry = lambda: self.x - self.area.zoomx1, lambda: self.y - self.area.zoomy1
        self.im = None # Maybe it should become a parameter*
        self.frame = lambda: self.drange(self.p.framelen[self.name])
        self.rangeim = lambda: self.p.pic['%s-%02d' % (self.name, self.frame())]
    def tick(self, area):
        self.area = area
        self.t -= 1
        self.draw()
    def draw(self): pass
    
class Collider(SysObj): # Sys Objects that support collisions
    def __init__(self, area, x, y, p, o, t, name, ranged=False, hitplayer=True, die=True):
        SysObj.__init__(self, area, x, y, p, o, t)
        self.name, self.hitplayer, self.die = name, hitplayer, die
        self.at = self.p.cat()
        print self.at
        self.facing = self.p.facing
        self.getim = lambda: '%s-%02d' % (self.name, self.frame()) if ranged else name 
        self.getlines = lambda: self.p.selfbox[self.getim()]
        self.getpic = lambda: self.p.pic[self.getim()]
        self.cx = lambda: -self.getpic().width/2
        self.cy = lambda: -self.getpic().height/2
        self.width = lambda: self.getpic().width
    def strike(self, x, y):
        return FireballStrike(self.area, x, y, self.p, self.o)
    def blit(self, tint=RGB(255,255,255,255)):
        self.getpic().TintBlit(self.rx(), self.ry(), tint)
    def collide5(self): # The collison box with the additional properties
        o = self.o
        return o, o.width(), o.selfbox1(), o.x+o.cx(), o.y+o.cy()
    def hit(self):
        o, owide, olines, ox, oy = self.collide5()        
        if olines is not None:
            print o.name, olines
            c = self.area.collide((o, owide, olines, ox, oy), (self, self.width(), self.getlines(), self.x, self.y))            
            if c is not None:
                x, y = c
                if self.die:
                    self.t = 0
                print c, self.hitplayer, self.p.movet, self.name
                if self.hitplayer and self.area.resolveHit(self.at, (x, y), self.o, self.p, False) or not self.hitplayer:                    
                    self.area.objects.append(self.strike(self.x, self.y))

class Fireball(Collider):
    glow = [RGB(0,255,255), RGB(0,0,255)]
    def __init__(self, area, x, y, p, o, dx, name):
        Collider.__init__(self, area, x, y, p, o, 600, name)
        self.dx = dx
    def draw(self):
        self.x += self.dx
        self.blit(Fireball.glow[self.t%2])
        self.hit()

class Bubble(Collider):
    def __init__(self, area, x, y, p, o, dx):
        Collider.__init__(self, area, x, y, p, o, 600, 'bubble', hitplayer=False)
        self.dx = dx
    def strike(self, x, y):
        return BubblePop(self.area, x, y, self.p, self.o)
    def collide5(self):
        p = self.p
        return p, p.width(), p.hitbox1(), p.x+p.cx(), p.y+p.cy()
    def draw(self):
        self.x += self.dx
        self.blit()
        self.hit()

class BubblePop(Collider):
    def __init__(self, area, x, y, p, o):
        Collider.__init__(self, area, x, y, p, o, 60, 'bubblepop', ranged=True, die=False)
        self.alreadyHit = False
    def draw(self):
        self.rangeim().Blit(self.rx(), self.ry())        
        if self.t == 30 and not self.alreadyHit:
            self.hit()
            self.alreadyHit = True
            
class UndergroundBall(Collider):
    glow = [RGB(0,255,255), RGB(0,0,255)]
    def __init__(self, area, x, y, p, o, name):
        Collider.__init__(self, area, x, y, p, o, 600, name)
        self.dx, self.dy = 0, -8
        self.t = 200
        self.y = 880
    def draw(self):
        o = self.o
        if self.t == 85:
            ang = atan2(o.y+o.h2()-self.y, o.x-self.x)
            self.dx, self.dy = int(cos(ang)*10), int(sin(ang)*10)
        cx = -self.width()/2 if self.p.facing == -1 else 0
        if self.t > 100:
            im = self.p.getpic('tele-04')
            im.Blit(self.rx()+cx-im.width/2, 860-self.area.zoomy1)
        if self.t < 150:
            self.y += self.dy
            self.x += self.dx
            self.blit(Fireball.glow[self.t%2])
            self.hit()

class FireballStrike(SysObj):
    glow = [RGB(0,0,255,255), RGB(0,128,255,255)]
    def __init__(self, *args):
        SysObj.__init__(self, *args)
    def draw(self):
        t = self.maxt - self.t
        Video.DrawEllipse(self.x, self.y, self.t+2, self.t+2, RGB(255,0,255,t*255/self.maxt), 1)
        self.o.tintcolor = FireballStrike.glow[(t/4)%2]
        if self.t == 0:
            self.o.tintcolor = RGB(255,255,255,255)

class Pixel:
    def __init__(self, x, y, dx, dy):
        self.x, self.y, self.dx, self.dy = x, y, dx, dy

class BlackHole(SysObj):
    def __init__(self, *args):
        self.pixels = []
        SysObj.__init__(self, t=120, *args)
    def draw(self):
        Video.DrawEllipse(self.rx(), self.ry(), self.dt(), self.dt(), RGB(32,0,128,self.rrange(255)), 1)
        angle = Random(0,50)*pi/25
        cx,cy = cos(angle), sin(angle)
        x, y = self.rx() + cx*50, self.ry()+cy*50
        dx, dy = -cx, -cy
        #print 'angle=%f, cx,cy=%s, x,y=%s, dx,dy=%s' % ( angle/pi, (cx,cy), (x,y), (dx, dy)) 
        self.pixels.append(Pixel(x, y, dx, dy))
        for p in self.pixels:
            p.x += p.dx
            p.y += p.dy            
            Video.DrawPixel(int(p.x), int(p.y), RGB(255,255,255))
        self.pixels = [p for p in self.pixels if abs(self.x-p.x)>2 and abs(self.y-p.y)>2]
        #print self.x, self.o.x, cmp(self.x, self.o.x)
        self.o.dx += cmp(self.x, self.o.x)

class LightStrike(SysObj):
    def __init__(self, area, x, y, p, o, t, name, frames):
        SysObj.__init__(self, area, x, y, p, o, t)
        self.name, self.frames = name, frames
    def draw(self):
        pic = self.area.strikim['%s-%02d' % (self.name,(self.maxt-self.t)*self.frames/self.maxt)]
        w, h = pic.width, pic.height
        pic.TintBlit(self.x-w/2, self.y-h/2, RGB(255,255,255,self.t*255/self.maxt))
        #pic.Blit(self.x-w/2, self.y-h/2)

class DashCircle(SysObj):
    def __init__(self, *args):
        SysObj.__init__(self, t=20, *args)
    def draw(self):
        t = self.maxt-self.t
        Video.DrawEllipse(self.x, self.y, t, t, RGB(0,0,255,t*255/self.maxt))
        
class CollisionTester(SysObj):
    colortoggle = True
    cols = {True:(RGB(0,0,255), RGB(255,0,0)), False:(RGB(0,255,255,128), RGB(255,255,0,128))}
    def __init__(self, area, x, y, lines):
        CollisionTester.colortoggle = not CollisionTester.colortoggle         
        self.vlines, self.hlines = lines
        self.vc, self.hc = CollisionTester.cols[CollisionTester.colortoggle]
        SysObj.__init__(self, area, x, y, t=300)
    def draw(self):
        for y, (x1, x2) in self.hlines.iteritems():
            Video.DrawLine(x1+self.rx(), y+self.ry(), x2+self.rx(), y+self.ry(), self.hc)
        for x, (y1, y2) in self.vlines.iteritems():
            Video.DrawLine(x+self.rx(), y1+self.ry(), x+self.rx(), y2+self.ry(), self.vc)        