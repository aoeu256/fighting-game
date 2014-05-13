from player import Player
from attack import Extend, Pre, BehindTeleport, FarLeftTeleport, FarRightTeleport 
from ika import RGB
import sysobj

class genjuro(Player):
    def __init__(self, **args):
        def NancyBall(p, o, a):            
            a.objects.append(sysobj.UndergroundBall(a, o.x, o.y, p, o, name='ball'))

        at = [Pre(name='m', dmg=60, hit=33, alen=50),
              Pre(name='[4]6s', imgname='m', dmg=30, hit=20, alen=20, funcs={10:NancyBall})
        ]
        dic = {RGB(192,74,77):RGB(60,119,152), RGB(143,76,82):RGB(65,92,107),
        RGB(60,119,152):RGB(192,74,77), RGB(65,92,107):RGB(143,76,82)}
        Player.__init__(self, name='genjuro', at=at, p1colors=dic, **args)
        self.drawstatef['intro'] = lambda: 'stand'
        self.drawstatef['stand'] = lambda: 'stand'
        self.drawstatef['crouch'] = lambda: 'crouch'from player import Player
from attack import * 
from ika import RGB

class kit(Player):
	def __init__(self, **args):
		at = [Pre(name='w', dmg=30, hit=30, alen=30)
			]
		dic = {RGB(192,74,77):RGB(60,119,152), RGB(143,76,82):RGB(65,92,107),
		RGB(60,119,152):RGB(192,74,77), RGB(65,92,107):RGB(143,76,82)}			
		Player.__init__(self, at=at, name='kit', p1colors=dic, **args)
		#stdatks = ['w','m','s','2w','2m','2s','8w','8m','8s']
from player import Player
from attack import Extend, Pre, BehindTeleport, FarLeftTeleport, FarRightTeleport, Air, Spawn 
from ika import RGB
import sysobj

class kyo(Player):
    def __init__(self, **args):
        def LiFire(p, o, a):
            Spawn(p, o, a, name='fireball', dx=8*p.facing)
        def LiHole(p, o, a):
            a.objects.append(sysobj.BlackHole(a, p.edge(), p.y, p, o))
        def mkBubble(p, o, a):
            a.objects.append(sysobj.Bubble(a, p.edge(), p.y, p, o, dx=1*p.facing))

        at = [Pre(name='s', dmg=60, hit=10, alen=40),
              Pre(name='2s',dmg=60, hit=10, alen=40),
              Pre(name='22m', imgname='2s', hit=40, ghit=40, alen=20, funcs={20:mkBubble}),
              Pre(name='236s', imgname='2s', hit=40, ghit=40, alen=40, funcs={35:LiFire}),
              Pre(name='623m', imgname='2s', hit=40, ghit=40, alen=20, funcs={10:LiHole}),
              Air(name='8s', dmg=60, hit=12, alen=25)
        ]
        dic = {RGB(192,74,77):RGB(60,119,152), RGB(143,76,82):RGB(65,92,107),
        RGB(60,119,152):RGB(192,74,77), RGB(65,92,107):RGB(143,76,82)}
        Player.__init__(self, name='kyo', at=at, p1colors=dic, **args)from player import Player
from attack import *
from ika import RGB
from sysobj import Fireball, BlackHole, Bubble

class li(Player):
	def __init__(self, **args):
		def LiFire(p, o, a):
			Spawn(p, o, a, name='fireball', dx=8*p.facing)
		def LiHole(p, o, a):
			a.objects.append(BlackHole(a, p.edge(), p.y, p, o))
		def mkBubble(p, o, a):
			a.objects.append(Bubble(a, p.edge(), p.y, p, o, dx=1*p.facing))
		at = [Pre(name='w', dmg=100, hit=31, alen=20, push=(-1,0), move=(1,0)),
			  Pre(name='s', dmg=350, hit=60, alen=60, push=(-1,0), move=(1,0)),
			  Pre(name='236w', dmg=175, hit=35, imgname='w', alen=60, funcs={47:LiFire}),
			  Pre(name='236s', dmg=300, hit=35, imgname='s', alen=20, funcs={15:mkBubble}),
			  Pre(name='m', imgname='w', alen=30, funcs={17:LiHole})
			  ]
		dic = {RGB(192,74,77):RGB(60,119,152), RGB(143,76,82):RGB(65,92,107),
		RGB(60,119,152):RGB(192,74,77), RGB(65,92,107):RGB(143,76,82)}
		Player.__init__(self, name='li', at=at, p1colors=dic, **args)
	def specials(self):
		return self.complexcommands(['236', '214'], 30) and (self.cat() is None or not self.cat().super)	
	def draw(self, x,y,t=None):
		Player.draw(self, x,y,t)
		if self.state in ('block', 'ghit'):
			Video.DrawEllipse(x, y, 8, 8, RGB(0,255,0,128), 1)from player import Player
from attack import Extend, Pre, BehindTeleport, FarLeftTeleport, FarRightTeleport 
from ika import RGB
import sysobj

class nancy(Player):
	def __init__(self, **args):
		def makeTeleport(key, func, len=40):
			return Pre(name='22%s'%key, imgname='tele', alen=len,funcs={len/2:func})
		def NancyBall(p, o, a):			
			a.objects.append(sysobj.UndergroundBall(a, o.x, o.y, p, o, name='ball'))
		at = [Extend(49, 47, 120, name='w', imgname='m', dmg=20, hit=33, alen=26),
			  Extend(49, 47, 250, name='m', imgname='m', dmg=40, hit=35, alen=31),
			  Extend(49, 47, 400, name='s', imgname='m', dmg=80, hit=39, alen=35),
			  Pre(name='236m', dmg=50, hit=20, alen=90, push=(-1,0), cycle=5, cycleframe=4),
			  Extend(37, 37, 600, name='41236S', imgname='236236m', dmg=350, alen=60, super=True, barcost=5001),
			  makeTeleport('m', BehindTeleport, len=30),
			  makeTeleport('w', FarLeftTeleport, len=70),
			  makeTeleport('s', FarRightTeleport, len=70),
			  Pre(name='[4]6m', imgname='tele', alen=30, dmg=100, holdback=60, funcs={15:NancyBall})
		]
		dic = {RGB(192,74,77):RGB(60,119,152), RGB(143,76,82):RGB(65,92,107),
		RGB(60,119,152):RGB(192,74,77), RGB(65,92,107):RGB(143,76,82)}
		Player.__init__(self, name='nancy', at=at, p1colors=dic, **args)
#	def intro(self, t):
#		self.state = 'intro'
		from outline import Outline, Lines
from os import *
from ika import *
from zoomblit import ZoomImage
import cPickle, load
from screens import control
from attack import *
import sysobj

class DummyPlayer: # Used in loading the players...
    def __init__(self, area, pname):
        self.area, self.pname = area, pname
        self.controls = control.Control(self, area=area)
    def save(self, name, data): # Save character specific data
        outf = file(self.outlinefol+name,'w')
        cPickle.dump(data, outf)
    def load(self, name):
        return cPickle.load(file(self.outlinefol+name))
class Player(DummyPlayer):
    directions = set('12346789')
    buttons = set('wms')
    diags = {'2':'123', '8':'789', '4':'147', '6':'369'}
    def LoadData(self, sameplayer=False):
        def MakeOutline(source, name):
            lines = Lines(Canvas(source))
            self.save(name+k, lines)
            return lines
        yield
        for im in listdir(self.imfol):            
            k = im[:-4]

            if self.samechar and self.pname == 'p2':
                try:
                    self.pic[k]= ZoomImage(self.reversefol+'p1'+im)
                except RuntimeError: # Morph character colors                    
                    pic = Canvas(self.imfol+im)
                    for x in range(pic.width):
                        for y in range(pic.height):
                            b = pic.GetPixel(x, y)
                            try: pic.SetPixel(x, y, self.p1colors[b])
                            except KeyError: pass
                    pic.Save(self.reversefol+'p1'+im)
                    self.pic[k] = ZoomImage(pic)
            else:
                try: # Check for cached information
                    self.pic[k] = ZoomImage(self.imfol+im)
                    #yield
                    self.selfbox[k] = self.load('self'+k)
                except (RuntimeError, IOError): # If not make the other images                     
                    print 'making lines for ', k
                    self.selfbox[k] = MakeOutline(self.imfol+im, 'self')
                if path.isfile(self.hitfolsrc+im):
                    if path.isfile(self.outlinefol+'hit'+k):
                        self.hitbox[k] = self.load('hit'+k)
                    else:
                        print 'making hit lines for ', k
                        self.hitbox[k] = MakeOutline(self.hitfolsrc+im, 'hit')
            #yield
        try:
            self.center = self.load('center')
            for k in self.pic:
                if k not in self.center:
                    self.center[k] = (self.pic[k].width/2,0)
        except IOError:
            self.center = dict((k, (v.width/2,0)) for k, v in self.pic.iteritems())
            self.save('center', self.center)
        self.framelen = {}
        for k in self.pic.keys(): # Determine framlen for the attacks
            if '-' in k:
                frame, value = k.split('-')
                value = int(value)
                if self.framelen.get(frame, -1) < value:
                    self.framelen[frame] = value
        for i in self.at.values(): i.load(self)
        self.getpic = lambda name: self.pic[name]
        self.getselfbox = lambda name: self.selfbox[name]
        self.gethitbox = lambda name: self.hitbox[name]
    def __init__(self, name, area, at, pname, p1colors, samechar):        
        self.name, self.area, self.pname, self.p1colors = name, area, pname, p1colors
        self.samechar = samechar
        def fun(i):
            i.p = self
            return i
        self.at = dict((i.name,fun(i)) for i in at)
        self.controls = control.Control(self, area=area)
        for k, v in self.area.fols.iteritems():
            self.__dict__[k] = '%s%s/' % (v, self.name)
        self.next = '' # The next attack*
        self.facing = 1
        self.totalframes = len(listdir(self.imfol))
        self.state = 'stand'
        self.tintcolor = RGB(255,255,255,255)
        self.pic = {}
        self.hitbox = {-1:{}, 1:{}}
        self.hp = self.bar = 100
        self.t = self.movet = self.wins = 0
        self.holddown, self.holddback = 0, 0 # Hold back or down*
        self.replay = []
        self.dy = self.dx = 0    # Character's current speed
        self.selfbox = {-1:{}, 1:{}}
        self.hitbox = {-1:{}, 1:{}}
        self.combo = 0
        self.attackpushing = False
        self.auxdraw = {'dash':self.drawdash, 'airdash':self.drawairdash}
        self.airdint = (-20,32)        
        self.loader = self.LoadData(samechar)
        #self.loader.next()
        self.forw = lambda: self.right if self.facing==1 else self.left
        self.back = lambda: self.left  if self.facing==1 else self.right
        self.width = lambda: self.pic[self.drawstate()].width
        self.height = lambda: self.pic[self.drawstate()].height
        self.w2, self.h2 = lambda: self.width()/2, lambda: self.height()/2
        self.dedge = lambda: self.w2()*self.facing
        self.edge = lambda: self.x + self.dedge()
        self.bedge = lambda: self.x - self.dedge()
        self.alreadyHit = False
        self.cy = lambda: 180-self.pic[self.drawstate()].height
        self.swidth = lambda: self.pic['stand'].width/2
        self.sheight = lambda: self.pic['stand'].height
        self.sw2 = lambda: self.swidth()/2
        self.sh2 = lambda: self.pic['stand'].height/2        
        self.sdedge =  lambda: self.sw2()*self.facing
        self.sedge = lambda: self.x+self.sdedge()
        self.rx, self.ry = lambda: self.x-self.area.zoomx1, lambda: self.y-self.area.zoomy1
        self.hy = lambda: self.y + self.sh2()     
        self.lastcomb = '' 
        self.jumpspeed = -32
        self.weight = 2
        self.walkspeed, self.dashspeed = 2, 4
        self.backspeed = (10, -12)
        self.maxspeed = 20
        self.airdspeed = 14
        self.airdleng = 20
        self.throwdist = 100
        self.throwdisp = [(20,20) for i in range(20)]
        self.throwstun = self.throwdmg = 50
        self.changestate('stand')
        self.ndash = 0
        self.njump =  0
        self.maxdash = 1
        self.maxjump = 2
        self.holdback, self.holddown = 0, 0
        self.refresh = 0
        self.lastcomb = ''
        self.holdt = 0    
        self.maxwalk = 4
        self.cycle = lambda n: n - abs(n - self.t % (n*2))        
        self.picrange = lambda name, n, max: '%s-%02d' % (name, n*self.framelen[name]/max)
        self.drawstatef = {
            'hit': lambda: 'hit-00',
            'thrown': lambda: 'hit-00',
            'throwstun': lambda: 'hit-00',
            'ghit': lambda: 'block',
            'intro': lambda: self.picrange('intro', self.area.maxmodet - self.area.modet, self.area.maxmodet),  
            'dash': lambda: self.picrange('dash', self.cycle(15), 14),
            'crouch': lambda: 'crouch-02',
            'air': self.drawair,
            'stand': self.drawstand
        }
    def drawstand(self):
        if not self.forwp and not self.backp:
            return 'stand' if self.t % 16 < 8 else 'stand-00'
        elif self.forwp or self.backp:
            return self.picrange('walk', self.cycle(15), 14)
    def drawair(self):
        if self.dx == 0:
            xtext = ''
        elif self.dx >= self.facing:
            xtext = 'forw'
        else:
            xtext = 'back'
        if self.dy < 0:
            jumpt = abs((self.jumpspeed - self.dy)/self.weight)
            maxjumpt = abs(self.jumpspeed/self.weight)
            if xtext != '': xtext = 'forw'
            return self.picrange('jump'+xtext, jumpt, maxjumpt)
        else:
            return self.picrange('fall'+xtext, self.cycle(15), 14)
    def drawstate(self):
        if self.state[0] == 'A':
            return self.cat().drawstate(self)
        try:
            return self.drawstatef[self.state]()
        except KeyError:
            return self.state if self.state in self.pic else 'stand'        
    def cx(self):
        cen = self.center[self.drawstate()][0]
        cx = cen-self.width() if self.facing == -1 else -cen
        return cx
    def cat(self): # CURRENT ATTACK
        if self.state[0] == 'A':
            return self.at[self.state[1:]]
        return None
    def draw1(self): #Drawn before...
        pass
    
    def intro(self):
        self.state = 'intro'
    
    def draw_shadow(self, x1, y1): #@UnusedVariable
        ds = self.drawstate()
        pic = self.pic[ds]        
        tilt = self.facing*25
        x = x1+self.cx()
        x2 = x1+self.cx()+pic.width
        c = RGB(255,255,255,196 - (900-self.y)*128/900)
        ydiff = (680 - self.y) / 8
        ys2 = (860+pic.height/2)-self.area.zoomy1+ydiff
        ys1 = 860-self.area.zoomy1 + ydiff
        pic.TintDistortBlit((x-tilt, ys2, c), (x2-tilt, ys2, c), (x2, ys1, c), (x, ys1, c))        
        
    def draw(self, x1, y1, tint = None):
        ds = self.drawstate()
        pic = self.pic[ds]
        #half = pic.height/2
        #c1, c2, cy = (0, half, self.cy()+half) if not drawtop else (half, half, self.cy())
        #x = x1 + self.cx()
        
        y = y1 + self.cy()
        self.draw1()
        tint2 = self.tintcolor if tint is None else tint
        try: self.auxdraw[self.state](x1, y)
        except KeyError: pass        
        pic.ZoomBlit(x1+self.cx(), y1+self.cy(), self.facing, tint2)
        if self.state[0] == 'A':
            self.cat().draw(x1, y, self)

    def drawdash(self, x, y):
        for i in range(3):
            self.pic[self.drawstate()].TintBlit(self.cx()+x-self.dx*(i+1), y, RGB(0,128,255,128-i*128/3))
    def drawairdash(self, x, y):
        for i in range(3):            
            self.pic[self.drawstate()].TintBlit(self.cx()+x-self.dx*(i+1), y, RGB(0,255,255,128-i*128/3))     
    def selfbox1(self):
        if self.drawstate() not in self.selfbox:
            return None
        return self.selfbox[self.drawstate()]
    def hitbox1(self):
        if self.cat() is None or self.cat().hitbox(self) is None:
            return None
        return self.cat().hitbox(self)
    def changestate(self, state, movet = None): # Just in case        
        if state != self.state:
            self.t = 0
        self.state = state
        if movet is not None:
            self.movet = movet
    def keycheck(self, keys, frame = 10):
        letgo = []
        i = 0
        ind = len(self.replay)-frame
        if keys == self.lastcomb:
            ind = max(self.mark, len(self.replay)-frame)
#            print 'ind=%d, mark=%d, len=%d, diff=%d' % (ind, self.mark, len(self.replay), len(self.replay)-self.mark) 
        if any(doub in keys for doub in ['66', '44', '22', '88']):
            keys = [''.join([Player.diags.get(k,k) for k in l]) for l in keys]
        for n, h in enumerate(self.replay[ind:]): # Sample h: 2W, keystring[i] == 'W'                        
            cond = any(o in keys[i] for o in h)
            lcond = any(o in keys[i] for o in letgo)
            #lcond = keys[i] == o
            if letgo and not cond:
                letgo = []
            elif cond and not lcond:
                #letgo = ''.join([Player.diags.get(k,k) for k in keys[i]])
                letgo = keys[i] 
                i += 1
                if i == len(keys):
                    self.mark = ind + n
                    self.lastcomb = keys
                    return True
        return False
    def movex(self, base, d):
        if self.rightp:
            return base + d * 1
        if self.leftp:
            return base + d * -1
        return base
    def complexcommands(self, combs, len):
        for i in 'wms':
            for comb in combs:
                combi = comb + i
                if combi in self.at and self.at[combi].barcost<self.bar and self.keycheck(comb+i, len) and not self.next:
                    self.next = comb+i
                    self.area.changebar(self, self.at[combi].barcost)
                    return True
        return False
    def supers(self):
        return self.complexcommands(['236236', '236214'], 60)        
    def specials(self):
        return self.complexcommands(['236', '214', '22'], 30) and (self.cat() is None or not self.cat().super)
    def normals(self):    
        if self.y == 680:
            self.checkfor('2' if self.b['2'] else '')
        else:
            self.checkfor('8')
    def checkfor(self, n):
        for i in 'wms':
            at = n+i
            if at in self.at and self.b[i]:
                if not self.next: self.next = at
    def holds(self):
        for i in 'wms':
            leftright = '[4]6%s'%i
            downup = '[2]8%s'%i
            assoc1, assoc2 = ('holdback', leftright, self.b['6']), ('holddown',downup, self.b['8'])            
            for prop, name, dire in (assoc1, assoc2):                
                if name in self.at:
                    if self.__dict__[prop] > self.at[name].__dict__[prop] and dire and self.b[i]:
                        if not self.next: self.next = name
    def throw(self, o):        
        if abs(self.x-o.x)<self.throwdist and self.y == o.y == 680 and o.state != 'throwstun':
            if self.b['s']:
                if self.b['6']: 
                    self.dothrow(o)
                elif self.b['4']:
                    self.facing *= -1;
                    o.facing *= -1
                    self.dothrow(o)
    def dothrow(self, o):
        leng = len(self.throwdisp)
        self.changestate('throw', leng*2)
        o.changestate('thrown', leng)
        self.area.changehp(o, -self.throwdmg)
    def dash(self):
        if self.state == 'dash':
            if not self.forwp:
                self.changestate('stand')
        else:
            ff, bb = self.keycheck('66',7), self.keycheck('44', 7)
            bf = bb or ff
            #if self.state != 'airdash':
            #   print self.state
            if self.state == 'stand':
                if ff: self.changestate('dash')
                if bb:
                    self.changestate('back')
                    self.dx, self.dy = self.backspeed[0]*-self.facing, self.backspeed[1]                    
            elif self.state == 'air' and bf and self.airdint[0]<self.dy<self.airdint[1]:
                if self.ndash < self.maxdash:
                    self.ndash += 1
                    self.changestate('airdash', self.airdleng)
                    self.dx = self.airdspeed*self.facing*(1 if ff else -1)
                    self.dy = 0
    def tick(self, b):
        self.t += 1
        self.b = b
        if self.state == 'thrown':
            t = self.movet-1
            self.x, self.y = b.x+b.throwdisp[t][0]*b.facing, b.y-b.throwdisp[t][1]
        elif self.state == 'airdash' and self.movet % 5 == 0:
            self.area.objects.append(
                sysobj.DashCircle(self.area, self.rx(), self.ry()+self.h2()+Random(-self.h2(),self.h2()), self, b))
        self.replay.append([])        
        self.downp, self.leftp, self.rightp =  self.down.Position(), self.left.Position(), self.right.Position()
        self.upp = self.up.Pressed()
        self.b = {}
        self.backp, self.forwp = (self.leftp, self.rightp) if self.facing==1 else (self.rightp, self.leftp)
        updown = self.upp or self.downp
        backforw = self.backp or self.forwp
        
        for d in ('back','down'):
            if self.__dict__[d+'p']:
                self.__dict__['hold'+d] += 1
                if self.holdt != 49:
                    self.__dict__['hold'+d] = 0
                self.holdt = 50
            else:
                if self.holdt == 0:
                    self.__dict__['hold'+d] = 0
                else:
                    self.holdt -= 1
        self.b = {'7':self.backp and self.upp, '8':self.upp and not backforw, '9':self.upp and self.forwp,
               '4':self.backp and not updown, '6':self.forwp and not updown,
                   '1':self.backp and self.downp, '2':self.downp and not backforw, '3':self.forwp and self.downp,
                   'w':self.W.Pressed(), 'm':self.M.Pressed(), 's':self.S.Pressed()}
        for k in '12346789':
            if self.b[k]:
                self.replay[-1] = [k]       
                break
        for k in 'wms':
            if self.b[k]:
                self.replay[-1].append(k)
        if self.state not in ['ghit', 'hit', 'airdash'] and self.y < 680:
            self.dy += self.weight # Gravity
        if self.state[0] == 'A':            
            funcs = self.cat().funcs              
            if self.movet in funcs:
                funcs[self.movet](self, b, self.area)
        if b.hitable():
            for k, st in (('4','block'), ('1','crouchblock'), ('7','airblock')):
                if self.b[k]: self.changestate(st)
        else:
            if self.state == 'stand':
                b.combo = 0
            if self.movet == 0:
                self.alreadyHit = False
                if b.state not in ['hit', 'ghit']:
                    self.next = ''
                if self.state == 'thrown':
                    self.changestate('throwstun', b.throwstun)
                    self.dx, self.dy = -self.facing*8, -16
                else:
                    #diagr, diagl = self.keycheck('6', 2), self.keycheck('4', 2)
                    if self.upp and self.njump < self.maxjump:
                        self.njump += 1
                        self.dy = self.jumpspeed          
                        if any([self.rightp, self.leftp]):
                            f = 1 if self.rightp else -1
#                            print self.state, self.dashspeed*2*f, self.walkspeed*2*f
                            self.dx = self.dashspeed*3*f if self.state=='dash' else self.walkspeed*3*f
                        else:
                            self.dx = 0
                        if self.y < 680:
                            self.facing = 1 if self.x < b.x else -1
                    elif self.y == 680:
                        self.njump = self.ndash = 0                        
                        if self.state != 'crouch':
                            self.dx = self.movex(self.dx, self.dashspeed if self.state == 'dash' else self.walkspeed)
                        if self.state != 'dash':
                            self.changestate('crouch' if self.downp else 'stand')
                            self.facing = 1 if self.x < b.x else -1
                    elif self.y < 680 and self.state != 'back': # in the air
                        self.changestate('air')
            else:
                self.movet -= 1
            self.dash()
            self.checkattacks(b)
        if self.next and self.state in ['crouch', 'stand', 'dash', 'air']:
            self.changestate('A%s' % self.next)
            if self.cat().super:
                self.area.dosuper(self)
            self.movet = self.at[self.next].alen
            self.next = ''
    def checkattacks(self, b):
        if not any([self.supers(), self.holds(), self.specials(), self.throw(b)]):
            self.normals()
    def hitable(self): # Does the character have a hitbox
        return self.hitbox1() is not Nonefrom ika import *
from screen import Screen

class Config(Screen):
    def __init__(self, **args):
        self.choices = ['RETURN', 'P1 CONTROLS', 'P2 CONTROLS', 'MUSIC VOLUME', 'SFX VOLUME', 'AI DIFFICULTY', 
                        'SHOW HITBOXES', 'NUMBER OF ROUNDS', 'TIMER']
        self.extra = {}
        self.extra['MUSIC VOLUME'] = self.extra['SFX VOLUME'] = [0, 25, 50, 75 ,100]
        self.extra['NUMBER OF ROUNDS'] = [1, 3, 5]
        self.extra['SHOW HITBOXES'] = ['YES', 'NO']
        self.extra['AI DIFFICULTY'] = ['GIANCARLO', 'VERY EASY', 'EASY', 'NORMAL', 'HARD', 'VERY HARD']
        self.extra['TIMER'] = [20, 30, 45, 99]
        self.config = {}
        self.config['MUSIC VOLUME'] = 2
        self.config['SHOW HITBOXES'] = 0
        self.config['SFX VOLUME'] = 2
        self.config['NUMBER OF ROUNDS'] = 2
        self.config['AI DIFFICULTY'] = 3
        self.config['TIMER'] = 2
        self.volume = 50
        self.nrounds = 2
        keycond = lambda: not self.done
        Screen.__init__(self, 'system/title', keycond=keycond, **args)
        self.f = self.area.font['metal']
        self.incx = 0
        self.x, self.y = 8, 8
        self.choice = 0
        self.setting = lambda configname: self.extra[configname][self.config[configname]]
    def main(self):
        #raise 'wtf'
        coi = self.choices[self.choice]
        self.scrollbg()
        Video.DrawRect(0,0,640,480,RGB(0,255,0,128))
        for y, i in enumerate(self.choices):
            f = self.area.font['menuwhite'] if self.choice == y else self.area.font['menugray']
            if i not in ('RETURN', 'P1 CONTROLS', 'P2 CONTROLS'):
                print i, self.config[i], self.extra[i]
            text = '%s %-8s' % (i, self.setting(i) if i in self.config else '')
            f.CenterXPrint(self.y + y*f.h, text)
        if self.up(): self.choice = (self.choice-1)%len(self.choices)
        if self.down(): self.choice = (self.choice+1)%len(self.choices)
        if self.right(): self.config[coi] = (self.config[coi]+1)%len(self.extra[coi])
        if self.left(): self.config[coi] = (self.config[coi]-1)%len(self.extra[coi])
    def do(self):
        self.done = False
        Screen.do(self)
        areavars2conf = {'nrounds':'NUMBER OF ROUNDS', 'maxt':'TIMER', 'ailevel':'AI DIFFICULTY', 
                    'musicvol':'MUSIC VOLUME', 'sfxvol':'SFX VOLUME'}
        for k, v in areavars2conf:
            self.area.__dict__[k] = self.setting(v)
#===============================================================================
#        self.area.nrounds = self.setting('NUMBER OF ROUNDS')
#        self.maxt = self.setting('TIMER')
#        self.ailevel = self.setting('AI DIFFICULTY')
#        self.showhitbox = self.setting('SHOW HITBOXES')
#        self.musicvol = self.setting('MUSIC VOLUME')
#        self.sfxvol =  self.setting('SFX VOLUME')
#===============================================================================from ika import *
from screen import Screen

class AxButton:
	def __init__(self, ax, n):
		self.ax, self.n = ax, n
		self.previous = False
	def Position(self):
		return self.ax.Position() == self.n
	def Pressed(self):
		if self.ax.Position() != self.previous:
			self.previous = None
		if self.ax.Position() != self.previous and self.ax.Position() == self.n:
			self.previous = self.ax.Position()
			return True
		return False
class Control(Screen):
	wx2ika = {';':'SEMICOLON'}
	def __init__(self, p, **args):
		self.keys = set(['BACKSPACE', 'TAB', 'CLEAR', 'RETURN', 'PAUSE', 'ESCAPE', 'SPACE', 'EXCLAIM', 'QUOTEDBL', 'HASH', 'DOLLAR', 'AMPERSAND', 'QUOTE', 'LEFTPAREN', 'RIGHTPAREN', 'ASTERISK', 'PLUS', 'COMMA', 'MINUS', 'PERIOD', 'SLASH', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'COLON', 'SEMICOLON', 'LESS', 'EQUALS', 'GREATER', 'QUESTION', 'AT', 'LEFTBRACKET', 'BACKSLASH', 'RIGHTBRACKET', 'CARET', 'UNDERSCORE', 'BACKQUOTE', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'DELETE', 'KP0', 'KP1', 'KP2', 'KP3', 'KP4', 'KP5', 'KP6', 'KP7', 'KP8', 'KP9', 'KP_PERIOD', 'KP_DIVIDE', 'KP_MULTIPLY', 'KP_MINUS', 'KP_PLUS', 'KP_ENTER', 'KP_EQUALS', 'UP', 'DOWN', 'RIGHT', 'LEFT', 'INSERT', 'HOME', 'END', 'PAGEUP', 'PAGEDOWN', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'NUMLOCK', 'CAPSLOCK', 'SCROLLOCK', 'RSHIFT', 'LSHIFT', 'RCTRL', 'LCTRL', 'RALT', 'LALT', 'RMETA', 'LMETA', 'LSUPER', 'RSUPER', 'MODE'])
		self.choices = ['up', 'right', 'down', 'left', 'W', 'M', 'S', 'start']
		self.choice = 0
		cond = lambda: not Input.keyboard['ESCAPE'].Position() and self.choice < len(self.choices)
		Screen.__init__(self, 'system/control', keycond=cond, stdcontrols=False, **args)
		self.p = p
		self.jaxposnames = {(0,-1):'LEFT', (0,1):'RIGHT', (1,-1):'UP', (1,1):'DOWN'}
		self.name2jaxpos = dict((v,k) for k, v in self.jaxposnames.iteritems())
		self.axbs = set()
		self.key2name = dict( (Input.keyboard[i],i) for i in self.keys)
		try:
			loaded = self.area.load('%scontrols' % self.p.pname)
			for k, v in loaded.iteritems():
				uk, uv = k.encode('ascii'), v.encode('ascii').upper()
				uv = Control.wx2ika.get(uv, uv)
				uk = uk.upper() if uk.lower() in 'wms' else uk.lower()
				def loadkey(b):
					self.p.__dict__[uk] = b
				if uv in self.keys:
					loadkey(Input.keyboard[uv])
				else:
					#print k, v
					#print uv[1:].split('-')
					jn, bn = uv[1:].split('-')
					jn = int(jn)
					if bn in self.name2jaxpos:
						axn, pos = self.name2jaxpos[bn]
						axb = AxButton(Input.joysticks[jn].axes[axn], pos)
						loadkey(axb)
					else:
						bn = int(bn)
						loadkey(Input.joysticks[jn].buttons[bn])
		except (IOError, IndexError):
			k = Input.keyboard
			dic = {'p1':'WASDERF1', 'p2':'IJKLHUY2'}
			(self.p.up, self.p.left, self.p.down,  self.p.right, self.p.W, self.p.M, self.p.S, self.p.start) = \
			 tuple(k[i] for i in dic[self.p.pname])
			# Perhaps put a warning
	def main(self):
 		cc = self.choices[self.choice]
		self.scrollbg()
		Video.DrawRect(0,0,640,480, RGB(0,0,255,128), 1)
		self.f.Print(400,0,'Configuring controls for %s' % (self.p.pname))
		#Video.DrawRect(20, 20+self.choice*32, 200,40+self.choice*32,RGB(0,255,0),1)
		for y, i in enumerate(self.choices):
			if y == self.choice:
				f = self.area.font['menuwhite']
			else:
				f = self.area.font['menugray']
			f.CenterXPrint(25+y*32,'PRESS A KEY FOR %8s.  CURRENTLY %8s.' % (i.upper(), self.key2name[self.p.__dict__[i]].upper()))
		
		def setkey(i):
				self.p.__dict__[cc] = i
				self.choice += 1
		for i in self.keys:
			if Input.keyboard[i].Pressed() and i != 'ESCAPE':
				setkey(Input.keyboard[i])				
		for jn, j in enumerate(Input.joysticks):			
			for y, ax in enumerate(j.axes):
				self.f.Print(8,400+y*16,'%s - %s '%(ax.Position(),ax.Pressed()))
				for n in [-1, 1]:					
					if ax.Position()== n and (ax,n) not in self.axbs:
						self.axbs.add( (ax,n) )
						axb = AxButton(ax, n)
						self.key2name[axb] = 'J%d-%s' % (jn, self.jaxposnames[y,n])
						setkey(axb)
			for bn, b in enumerate(j.buttons):
				self.key2name[b] = 'J%d-%d' % (jn, bn)
				if b.Pressed():
					setkey(b)
	def do(self):
		Screen.do(self)
		self.area.save('%scontrols' % self.p.pname, dict((i, self.key2name[self.p.__dict__[i]]) for i in self.choices) )
		#self.p.save('cnames',  self.key2name)from ika import RGB, Input, Video
from screen import Screen

class Edit(Screen):
	def __init__(self, p, frame = 'stand', **args):
		cond = lambda: not Input.keyboard['ESCAPE'].Pressed()
		self.c = [RGB(255,0,0), RGB(0,255,0), RGB(0,0,255)]
		self.text = {'A':'hitbox(x1, y1)', 'S':'Set hitbox', 'D':'center', 'F':'frame'}
		self.mode = 'D'
		self.config = dict((i,(0,0)) for i in self.text)
		self.p = p
		self.frame = frame
		Screen.__init__(self, keycond=cond, mouse=True, **args)
		self.config['D'] = self.p.center[self.frame]
		self.frames = [k for k in p.pic.keys()]
	def main(self):
		c = self.c[self.t%3]
		if self.frame in self.p.pic:
			self.p.pic[self.frame].Blit(0, 0)
		(x1, y1), (x2, y2) = self.config['A'], self.config['S']
		Video.DrawRect(x1, y1, x2, y2, RGB(255,255,255))
		x, y = self.config['D']
		Video.DrawPixel(x, y, c)
		Video.DrawEllipse(x, y, 2+(self.t%6), 2+((self.t+3)%6), c)
		if self.mode == 'F':
			Video.DrawRect(379,0,620,16,RGB(0,255,0))
		self.f.Print(380, 1, self.frame)
		if '-' in self.frame and self.mode != 'F':
			k, n = self.frame.split('-')
			n = int(n)
			l = self.p.framelen[k]
			self.f.Print(490,0, '%s/%s' % (n,l) )			
			def common(o):
				self.frame = '%s-%02d' % (k,(n+o)%(l+1))
				self.config['D'] = self.p.center[self.frame]
			if Input.left.Pressed(): common(-1)
			if Input.right.Pressed(): common(1)		
		if self.mode != 'F':
			self.f.Print(420, 0, '%3d/%3d' % (self.frames.index(self.frame), len(self.frames)))
			if Input.mouse.left.Pressed():
				self.config[self.mode] = (int(self.mx), int(self.my))
				if self.mode == 'D':
					self.p.center[self.frame] = self.config['D']
			for i, (k, v) in enumerate(self.text.iteritems()):
				modearrow = '>' if self.mode == k else ' '
				self.f.Print(321, 16+i*16, '%sPress %s to %s: %s' % (modearrow, k, v, self.config[k]))
				if Input.keyboard[k].Pressed() and self.mode != 'F':
					self.mode = k
		else:
			for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ2346789':
				if Input.keyboard[letter].Pressed():
					self.frame += letter.lower()
			if Input.keyboard['BACKSPACE'].Pressed() and len(self.frame) > 0:
				self.frame = self.frame[:-1]
			if Input.keyboard['RETURN'].Pressed():
				def common():
					self.mode = 'D'
					self.config['D'] = self.p.center[self.frame]
				if self.frame in self.p.pic:
					common()					
				elif self.frame in self.p.framelen:
					self.frame = '%s-00' % (self.frame)
					common()
				else:
					self.frame = 'ERR'
	def do(self):
		Screen.do(self)
		self.p.save('center', self.p.center)from ika import *
from screen import Screen

class Menu(Screen):
	def __init__(self, choices, f=None, f2=None, keycond=None, **args):
		'''		
		@param choices:
		@param f:
		@param keycond:
		'''
		if keycond is None:
			keycond = lambda: not self.done
		self.choices = choices
		self.done = False
		Screen.__init__(self, keycond=keycond, **args)
		self.choice = 0
		if f is not None:			
			self.f, self.f2 = f, f2
		else:
			self.f, self.f2 = self.area.font['menuwhite'], self.area.font['menugray']
		self.t = 0
		self.h = self.f.h
		self.len = len(self.choices)
		dx, dy = max(self.f.width(i) for i in choices)/2, self.len*self.h/2
		self.x, self.y = 320 - dx, 240 - dy
		self.x2, self.y2 = 320 + dx, 240 + dy
		self.imagegrab = None
	def main(self):
		self.t+=1
		if self.imagegrab is not None:
			self.imagegrab.Blit(0,0)
		Video.DrawRect(self.x, self.y, self.x2, self.y2, RGB(0,0,255,128), 1)
		w = self.f.width(self.choices[self.choice])
		Video.DrawRect(320-w/2, self.y+self.choice*self.h, 
					   320+w/2, self.y+self.h+self.choice*self.h, RGB(0,255,0,128), 1)
		for y, i in enumerate(self.choices):
			f = self.f if y == self.choice else self.f2
			f.CenterXPrint(self.y+y*self.h, i)
		def move():
			pass
		if self.p.up.Pressed():   self.choice = (self.choice-1)%self.len
		if self.p.down.Pressed(): self.choice = (self.choice+1)%self.len
		if any(i.Pressed() for i in (self.p.W, self.p.M, self.p.S, self.p.start)):
			self.done = True
	def do(self, p, img=None):
		self.p = p
		self.imagegrab = img
		Screen.do(self)
		self.done = False
		return self.choices[self.choice]
	
class CommandList(Menu): # This one is created dynamically...
	'Creates a command list'
	def __init__(self, p, area, **args):
		'__init(self,p,area,**args)'
		self.p = p
		specials = [k.upper() for k, v in p.at.iteritems() if len(k) > 2 and not v.super]
		supers = [k.upper() for k, v in p.at.iteritems() if v.super]
		mapc = {'[':'(', ']':')'}
		for n, i in enumerate(specials):
			specials[n] = [mapc.get(c,c) for c in i]
		Menu.__init__(self, choices=specials+supers, area=area, **args)		
	def main(self):
		self.area.font['metal'].CenterXPrint(self.y-60, '%s\'S COMMAND LIST' % self.p.name.upper())
		Menu.main(self)
	def do(self, img=None):
		Menu.do(self, self.p, img)from ika import *
from xi import fps
import load

##f = load.getFont()
fp = fps.FPSManager(60)

class Screen:
	def __init__(self, im=None, maxtime=None, keycond=lambda: True, area=None, mouse=False, stdcontrols=True):
		global fp
		self.fp, self.f, self.area, self.maxtime, self.mouse = fp, area.f, area, maxtime, mouse
		self.font = area.font
		self.t = 0
		if im is not None:
			self.im = load.All(im, cwd=area.cwd)			
		self.keycond = keycond
		self.timecond = lambda: True if self.maxtime is None else lambda: self.t < self.maxtime
		if stdcontrols:
			p1, p2 = self.area.dp1, self.area.dp2
			self.up 	= lambda: p1.up.Pressed() or p2.up.Pressed()
			self.down 	= lambda: p1.down.Pressed() or p2.down.Pressed()
			self.right 	= lambda: p1.right.Pressed() or p2.right.Pressed()
			self.left 	= lambda: p1.left.Pressed() or p2.left.Pressed()
			self.W 		= lambda: p1.W.Pressed() or p2.W.Pressed()
			self.M 		= lambda: p1.M.Pressed() or p2.M.Pressed()
			self.S 		= lambda: p1.S.Pressed() or p2.S.Pressed()
			self.start 	= lambda: p1.start.Pressed() or p2.start.Pressed()			
	def main2(self):
		self.main()
		if self.mouse:
			self.mx, self.my = Input.mouse.x.Position(), Input.mouse.y.Position()
			Video.DrawLine(self.mx-320, self.my, self.mx+320, self.my, RGB(255,0,255))
			Video.DrawLine(self.mx, self.my-320, self.mx, self.my+320, RGB(255,0,255))
			self.f.Print(300, 0, '%d,%d' % (self.mx, self.my))
		self.t += 1
	def scrollbg(self):
		logo = self.area.logoim
		self.t = self.t % 100
		bx, by = self.t*logo.width/100, self.t*logo.height/100
		for x in range(-1, 2):
			for y in range(-1, 4):
				logo.Blit(x*logo.width+bx, y*logo.height+by)
	def do(self):
		while self.timecond() and self.keycond():
			fp.render(self.main2)
			Input.Update()from ika import *
from screen import Screen

class Select(Screen):
	def __init__(self, p1, p2, **args):
		self.p1, self.p2 = p1, p2
		cond = lambda: '' in [p1.selected, p2.selected]
		Screen.__init__(self, 'system/select', keycond=cond, **args)
		p1.px, p1.py, p2.px, p2.py = 0, 0, 3, 0
		#p1.cursor, p2.cursor = self.im['1player-cursor'], self.im['2player-cursor']
		p1.c, p2.c = RGB(0, 255, 0), RGB(0, 0, 255)
		p1.tagx, p2.tagx = 8, 38
		p1.namex, p2.namex = 10, 520
		p1.selected, p2.selected = '', ''
		self.characters = [['genjuro', '', '', ''], ['', 'kyo', '', '']]
		self.xmul, self.ymul = 96, 66	
		self.flashcols = [RGB(255, 0, 0, 64), RGB(0, 255, 0, 64), RGB(0, 0, 255, 64)]
	def intro(self, t):
		self.im['selectscreen-bg'].Blit(0, 0)
		self.im['map'].ScaleBlit(54, 24 + (50-t)*2, 532, t*4)
		self.im['sidepanel-right'].Blit(640-(t*147/50), 0)
		self.im['sidepanel-left'].Blit(-147+(t*147/50), 0)
		for y, row in enumerate(self.characters):
			for x, pic in enumerate(row):
				if pic in [self.p1.selected, self.p2.selected] and pic:
					c = self.flashcols[(self.t/5)%3]
				else:
					c = RGB(255, 255, 255)
				(self.im['face'] if pic=='' else self.im[pic]).TintBlit(148+x*self.xmul, 306+y*self.ymul, c)
	def main(self):
		if self.t < 50:
			self.intro(self.t)
		else:
			self.intro(50)
			Height, Width = 2, 4			
			self.f.Print(0, 0, "%d,%d %d,%d" % (self.p1.px, self.p1.py, self.p2.px, self.p2.py))
			for p in [self.p1, self.p2]:
				#p.cursor.Blit(148 + p.px*96, 306 + p.py*64)
				p.name = self.characters[p.py][p.px]
				self.font['metal'].Print(p.namex, 440, p.name.upper())
				c = RGB(0, 255, 255) if (self.p1.px, self.p1.py) == (self.p2.px, self.p2.py) else p.c
				x, y = 148 + p.px*self.xmul, 306 + p.py*self.ymul
				self.im['cursor'].TintBlit(x, y, c)
				self.im[p.pname].TintBlit(x+p.tagx, y+50, p.c)
				if p.selected == '':
					if p.up.Pressed():	p.py = (p.py-1) % Height
					if p.right.Pressed():	p.px = (p.px+1) % Width
					if p.left.Pressed():	p.px = (p.px-1) % Width
					if p.down.Pressed():	p.py = (p.py+1) % Height
				if p.W.Pressed() or p.S.Pressed():
					p.selected = p.name if p.name else p.selected
				elif p.M.Pressed():
					p.selected = ''
	def do(self):
		self.p1.selected, self.p2.selected = '', ''
		Screen.do(self)
		#self.p2.name, self.p1.name = 'genjuro', 'kyo'from ika import *
from screen import Screen

text = """
This one big dude came and stole everyone's souls!!!!
That is because he wanted to beat all of the strongest
people in the world!!!!!!  So these strongest people
will compete for their souls!!!!!  These are the people
that will use the cheapest fighting styles to win!!!!!"""

class Story(Screen):
	def __init__(self, **args):
		self.textall = text.split('\n')
		Screen.__init__(self, maxtime = 60 * 5, **args)
	def main(self):
		self.f.Print(0,0,str(self.t))
		for y, i in enumerate(self.textall):
			self.f.Print(5, y*32 + 480-self.t, i)from ika import *
from screen import Screen

class Title(Screen):
	def __init__(self, **args):
		self.choice = self.nextchoice = 0
		self.choices = [i.upper() for i in ['Arcade', 'VS Mode', 'Training', 'Options', 'Exit']]
		self.done = False
		keycond = lambda: not self.done
		Screen.__init__(self, 'system/title', keycond=keycond, **args)
		self.incx = 0
	def main(self):
		self.im['titlescreen-bg'].Blit(0, 0)		
		logo = self.im['metal-logo']
		logo.Blit(320-logo.width/2, 10)
		#self.scrollbg()
		self.f.Print(0,0, '%d' % self.t)		
		rb = self.im['red-bar']
		rb.Blit(0, 240-rb.height/2)

		for i in range(-1, 4):
			l = len(self.choices)
			if i == 1 and self.incx == 0:
				f = self.area.font['menuwhite']
			else:
				f = self.area.font['menugray']
			f.Print(640/3*i+60+self.incx, 240-f.h/2, self.choices[(self.choice+i)%l])
		if self.right() and self.incx < 640*2/3:
			self.nextchoice = (self.nextchoice + 1) % len(self.choices)
			self.incx += 640/3
		if self.left() and self.incx > -640*2/3:
			self.nextchoice = (self.nextchoice - 1) % len(self.choices)
			self.incx += -640/3
		if self.incx == 0:
			self.choice = self.nextchoice
			if self.S() or self.start():
				self.done = True
		else:
			sign = lambda x: -1 if x < 0 else 1
			self.incx -= sign(self.incx)*12
			if abs(self.incx) < 16:
				self.incx = 0
			self.choice = self.nextchoice
	def do(self):
		self.done = False
		#Screen.do(self)
		#return self.choices[(self.choice+1)%len(self.choices)]
		return 'VS MODE'from ika import *
from screen import Screen

class Vs(Screen):
	def __init__(self, p1, p2, **args):
		cond = lambda: not self.done
		Screen.__init__(self, 'system/vs', keycond=cond, **args)
		self.p1, self.p2 = p1, p2
		self.c = [RGB(255,0,0,32), RGB(0,255,0,32), RGB(0,0,255,32)]
		self.f = self.area.font['menuwhite']
		self.barmax = p1.totalframes + p2.totalframes
		self.bar = 0
	def main(self):
		self.im['versus-bg-1'].Blit(0, 0)
		Video.DrawRect(0,0,640,480,self.c[(self.t/8)%3],1)
		self.im['vs-text'].Blit(200, 180)
		def next(p):
			p.loader.next()
			#text = 	'LOADING %3d OUT OF %3d' % (self.bar, self.barmax*2)
			#w, h = self.f.width(text), self.f.h
			#Video.DrawRect(2, 2, w, h, RGB(0,0,0), 1)
			#Video.DrawRect(2, 2, self.bar*w/self.barmax/2, h, RGB(0,0,255), 1)
			#self.f.Print(2, 2, text)
			self.bar += 1
		try:
			next(self.p1)
		except StopIteration:
			try:
				next(self.p2)
			except StopIteration:
				#if self.start() or self.t > 60 * 10:
				self.done = True
	def do(self):
		self.done = False
		Screen.do(self)from ika import *
from sysobj import Fireball
from math import cos, pi
def Spawn(p, o, a, name, obj=Fireball, **args): #@UnusedVariable
	'Use with func property in attacks'
	a.objects.append(obj(a, p.x, p.y, p, o, name=name, **args))
def FarRightTeleport(p, o, a): #@UnusedVariable
	p.x = o.x + 640
def FarLeftTeleport(p, o, a): #@UnusedVariable
	p.x = o.x - 640
def BehindTeleport(p, o, a): # Work in Progress @UnusedVariable
	p.x = o.x + (p.w2()+o.w2())*-o.facing
	
class At:
	def __init__(self, name, alen=10, dmg=10, hit=10, ghit=10, push=(0,0), move=(0,0), 
			 framelist=None, hitlist=[], reverse=False, cycle=1, cycleframe=3,
			 super=False, barcost=0, funcs={}, imgname = None, overhead = False,
			 holdback=0, holddown=0):
		self.funcs = funcs # self.funcs[p.movet](p, o, area)
		self.imgname = name if imgname is None else imgname
		self.reverse = reverse
		self.name, self.alen = name, alen
		self.push,self.move = push, move
		self.ghit,self.hit = ghit, hit
		self.dmg = dmg
		self.framelist = framelist
		self.hitlist = hitlist[:]
		self.barcost,self.super = barcost, super
		self.cycle,self.cycleframe = cycle, cycleframe
		self.addxy = lambda p: (0,0) #@UnusedVariable
		self.overhead = overhead
		self.holdback, self.holddown = holdback, holddown
		self.width = lambda p: p.width()
	def hitbox(self, p):
		return p.hitbox.get(p.drawstate(), None)
	def draw(self, x, y, p): pass
	
	def loadframes(self, p):
		self.framelist = range(self.flen)
		if self.cycle == 1:
			self.framelist += range(self.flen, -1, -1)				
		else:
			for i in range(self.cycle-1): #@UnusedVariable
				self.framelist += range(self.flen,self.cycleframe-1, -1)					
				self.framelist += range(self.cycleframe,self.flen)
			self.framelist += range(self.flen, -1, -1)
		
	def load(self, p):
		self.flen = p.framelen[self.imgname]
		if self.framelist is None:
			self.loadframes(p)
		self.listlen = len(self.framelist)-1

		if self.hitlist == [] and self.cycle > 1:
			for i in range(1, self.alen):
				if self.frame(i-1) != self.frame(i) == self.flen:
					self.hitlist.append(i)
		if self.reverse: self.framelist.reverse()
	def frame(self, movet):
		t = movet*self.listlen/self.alen
		return self.framelist[-t-1]			
#	def refresh(self, p):
#		return p.refresh
	def drawstate(self, p):
		return '%s-%02d' % (self.imgname, self.frame(p.movet))		
	
class Pre(At):
	pass
#	def drawstate(self, p):
		#t = (p.movet*self.flen*2/self.alen)
		#m =self.flen - abs(self.flen-t)
#		t = p.movet*self.listlen/self.alen
#		return '%s-%02d' % (self.imgname,self.framelist[t])

class Extend(At): # Attacks that extend*
	'Attacks that consist of a predrawn self part, an extension image, and an end.'
	def __init__(self, y, y2, rang=5, startup=0, **args):
		At.__init__(self, **args)
		self.rang = rang
		self.code = lambda t: (0, 0) # Path where atim will be @UnusedVariable
		self.y,self.y2 = y, y2
		#self.leng = lambda p:
		self.extw = lambda p: -p.pic[self.imgname+'ext'].width		
		self.extcx = lambda p: 0 if p.facing == 1 else -self.extw(p)
		self.end = lambda p: p.w2()*p.facing
		self.hitbox = lambda p: p.selfbox[self.name+'end']
		self.addxy = lambda p: (self.endx(p)-self.p.cx(), self.y2)
		self.startup = startup
		self.ralen = lambda: self.alen - self.startup  
		self.rt = lambda p: p.movet - self.startup
		self.width = lambda p: p.pic[self.imgname+'end'].width
		#Sself.cx = 
	def leng(self, p):
		t = (self.ralen() - self.rt(p))*pi / self.ralen()
		return int((1-abs(cos(t)))**2*self.rang*p.facing/self.extw(p)*self.extw(p))
	def endx(self, p):
		endpic = p.pic[self.imgname+'end']
		cx = 0 if p.facing == 1 else -endpic.width
		return cx+self.end(p)+self.leng(p)
	def draw(self, x, y, p):
		endpic = p.pic[self.imgname+'end']
		ext = p.pic[self.imgname+'ext']
		extcx = 0 if p.facing == 1 else self.extw(p)
		if p.movet<self.alen-self.startup:
			endpic.Blit(x+self.endx(p), y+self.y2)
			for i in range(0,abs(self.leng(p)),ext.width):
				ext.Blit(x+self.end(p)+i*p.facing+extcx, y+self.y)

class Air(At):
	def __init__(self, midleng=20, **args):
		At.__init__(self, **args)
		self.midleng = midleng		
	def loadframes(self, p):
		self.framelist = range(self.flen)
		self.framelist = [self.flen for i in range(self.midleng)] #@UnusedVariable
		self.framelist += range(self.flen, -1, -1)				# 			def cache(dire, im, source=None, saveOriginal=True):
# 				canv = Canvas(dire+im) if source is None else source
# 				rc = Canvas(canv.width, canv.height)
# 				canv.Blit(rc, 0, 0); rc.Mirror()
# 				if saveOriginal:
# 					canv.Save(dire+im)
# 				rc.Save(dire+'l'+im)
# 				return (canv, rc)
# 			def toSilho(pic, col):
# 				for x in xrange(pic.width):
# 					for y in xrange(pic.height):
# 						if GetRGB(pic.GetPixel(x, y))[3] != 0:
# 							pic.SetPixel(x, y, col)
# 						return pic
# 			for im in listdir(fol):
# 				k = im[:-4]
# 				try: # Check for silhoutte
# 					p.silho[1][k], p.silho[-1][k] = Canvas(cachefol+p.pname+im), Canvas(cachefol+'l'+p.pname+im)
# 					loadpics(im)
# 				except (RuntimeError, IOError): # If not make the silhoutte while making a cache
# 					if p.name not in listdir(imfol+'cache/characters'):
# 						mkdir(cachefol)
# 					pic = toSilho(cache(cachefol, im, source=Canvas(fol+im), saveOriginal=False)[0], p.silhoc)
# 					try:
# 						toSilho(Canvas(hitfolsrc+im), p.hitboxc).Blit(pic, 0, 0, Matte)
# 					except IOError:
# 						pass
# 					p.silho[1][k], p.silho[-1][k] = cache(cachefol, p.pname+im, source=pic)
# 					loadpics(im)
# 		try:
# 			for x in xrange(640/48):
# 				for y in xrange(480/48):
# 					c = a.silho.GetPixel(x*48, y*48)
# 					if c == RGB(128,256,128) or a.p2.win and a.p1.win:
# 						raise 'break'
# 					elif c == RGB(0,256,128):
# 						a.p2.win = True
# 					elif c == RGB(128,128,128):
# 						a.p1.win = True
# 		except 'break':
# 			pass
		#	a.p1.barx, a.p2.barx = 20, 360
import ika

c = ika.RGB
h, x = 128, 255

R = c(x,0,0)
O = c(x,h,0)
G = c(0,x,0)
Y = c(x,x,0)
C = c(0,x,x)
B = c(0,0,x)
M = c(x,0,x)
White = c(x,x,x)
Black = c(0,0,0)import ika
x, h = 255, 128
red = ika.RGB(x,0,0)
green = ika.RGB(0,x,0)
blue = ika.RGB(0,0,x)
cyan = ika.RGB(0,x,x)
yellow = ika.RGB(x,x,0)
purple = ika.RGB(x,0,x)
aqua = ika.RGB(0,x,h)
white = ika.RGB(x,x,x)
black = ika.RGB(0,0,0)

import os, sys
done = False
print 'Enter character name:'
charname = raw_input()
print 'Enter a image name:'
imgname = raw_input()

try:
    def remove(im):
        print 'Removing %s...' % im
        os.remove(im)
    fill = (os.getcwd(), charname)
    folder = '%s/Images/characters/%s' % fill
    flist = [(os.getcwd(), charname, i[:-4]) for i in os.listdir(folder) if imgname in i]
    for fill in flist:
        remove('%s/Images/cache/characters/%s/l%s.png' % fill)
        remove('%s/cache/outline/%s/self%s' % fill)
        remove('%s/Images/cache/characters/%s/lp1%s.png' % fill)
        remove('%s/Images/cache/characters/%s/p1%s.png' % fill)
except WindowsError:
    passfrom __future__ import with_statement
import wx, os, cPickle

rbId, playId, exitId, p1Id, p2Id = tuple(range(10,15))
runIka = False

##WXK_BACK 	WXK_EXECUTE 	WXK_F1 	WXK_NUMPAD_SPACE 	WXK_WINDOWS_LEFT
##WXK_TAB 	WXK_SNAPSHOT 	WXK_F2 	WXK_NUMPAD_TAB 	WXK_WINDOWS_RIGHT
##WXK_RETURN 	WXK_INSERT 	WXK_F3 	WXK_NUMPAD_ENTER 	WXK_WINDOWS_MENU
##WXK_ESCAPE 	WXK_HELP 	WXK_F4 	WXK_NUMPAD_F1 	WXK_SPECIAL1
##WXK_SPACE 	WXK_NUMPAD0 	WXK_F5 	WXK_NUMPAD_F2 	WXK_SPECIAL2
##WXK_DELETE 	WXK_NUMPAD1 	WXK_F6 	WXK_NUMPAD_F3 	WXK_SPECIAL3
##WXK_LBUTTON 	WXK_NUMPAD2 	WXK_F7 	WXK_NUMPAD_F4 	WXK_SPECIAL4
##WXK_RBUTTON 	WXK_NUMPAD3 	WXK_F8 	WXK_NUMPAD_HOME 	WXK_SPECIAL5
##WXK_CANCEL 	WXK_NUMPAD4 	WXK_F9 	WXK_NUMPAD_LEFT 	WXK_SPECIAL6
##WXK_MBUTTON 	WXK_NUMPAD5 	WXK_F10 	WXK_NUMPAD_UP 	WXK_SPECIAL7
##WXK_CLEAR 	WXK_NUMPAD6 	WXK_F11 	WXK_NUMPAD_RIGHT 	WXK_SPECIAL8
##WXK_SHIFT 	WXK_NUMPAD7 	WXK_F12 	WXK_NUMPAD_DOWN 	WXK_SPECIAL9
##WXK_ALT 	WXK_NUMPAD8 	WXK_F13 	WXK_NUMPAD_PRIOR 	WXK_SPECIAL10
##WXK_CONTROL 	WXK_NUMPAD9 	WXK_F14 	WXK_NUMPAD_PAGEUP 	WXK_SPECIAL11
##WXK_MENU 	WXK_MULTIPLY 	WXK_F15 	WXK_NUMPAD_NEXT 	WXK_SPECIAL12
##WXK_PAUSE 	WXK_ADD 	WXK_F16 	WXK_NUMPAD_PAGEDOWN 	WXK_SPECIAL13
##WXK_CAPITAL 	WXK_SEPARATOR 	WXK_F17 	WXK_NUMPAD_END 	WXK_SPECIAL14
##WXK_PRIOR 	WXK_SUBTRACT 	WXK_F18 	WXK_NUMPAD_BEGIN 	WXK_SPECIAL15
##WXK_NEXT 	WXK_DECIMAL 	WXK_F19 	WXK_NUMPAD_INSERT 	WXK_SPECIAL16
##WXK_END 	WXK_DIVIDE 	WXK_F20 	WXK_NUMPAD_DELETE 	WXK_SPECIAL17
##WXK_HOME 	WXK_NUMLOCK 	WXK_F21 	WXK_NUMPAD_EQUAL 	WXK_SPECIAL18
##WXK_LEFT 	WXK_SCROLL 	WXK_F22 	WXK_NUMPAD_MULTIPLY 	WXK_SPECIAL19
##WXK_UP 	WXK_PAGEUP 	WXK_F23 	WXK_NUMPAD_ADD 	WXK_SPECIAL20
##WXK_RIGHT 	WXK_PAGEDOWN 	WXK_F24 	WXK_NUMPAD_SEPARATOR 	 
##WXK_DOWN 	  	  	WXK_NUMPAD_SUBTRACT 	 
##WXK_SELECT 	  	  	WXK_NUMPAD_DECIMAL 	 
##WXK_PRINT 	  	  	WXK_NUMPAD_DIVIDE
#keys = ['wx.WXK_BACK', 'wx.WXK_EXECUTE', 'wx.WXK_F1', 'wx.WXK_NUMPAD_SPACE', 'wx.WXK_WINDOWS_LEFT', 'wx.WXK_TAB', 'wx.WXK_SNAPSHOT', 'wx.WXK_F2', 'wx.WXK_NUMPAD_TAB', 'wx.WXK_WINDOWS_RIGHT', 'wx.WXK_RETURN', 'wx.WXK_INSERT', 'wx.WXK_F3', 'wx.WXK_NUMPAD_ENTER', 'wx.WXK_WINDOWS_MENU', 'wx.WXK_ESCAPE', 'wx.WXK_HELP', 'wx.WXK_F4', 'wx.WXK_NUMPAD_F1', 'wx.WXK_SPECIAL1', 'wx.WXK_SPACE', 'wx.WXK_NUMPAD0', 'wx.WXK_F5', 'wx.WXK_NUMPAD_F2', 'wx.WXK_SPECIAL2', 'wx.WXK_DELETE', 'wx.WXK_NUMPAD1', 'wx.WXK_F6', 'wx.WXK_NUMPAD_F3', 'wx.WXK_SPECIAL3', 'wx.WXK_LBUTTON', 'wx.WXK_NUMPAD2', 'wx.WXK_F7', 'wx.WXK_NUMPAD_F4', 'wx.WXK_SPECIAL4', 'wx.WXK_RBUTTON', 'wx.WXK_NUMPAD3', 'wx.WXK_F8', 'wx.WXK_NUMPAD_HOME', 'wx.WXK_SPECIAL5', 'wx.WXK_CANCEL', 'wx.WXK_NUMPAD4', 'wx.WXK_F9', 'wx.WXK_NUMPAD_LEFT', 'wx.WXK_SPECIAL6', 'wx.WXK_MBUTTON', 'wx.WXK_NUMPAD5', 'wx.WXK_F10', 'wx.WXK_NUMPAD_UP', 'wx.WXK_SPECIAL7', 'wx.WXK_CLEAR', 'wx.WXK_NUMPAD6', 'wx.WXK_F11', 'wx.WXK_NUMPAD_RIGHT', 'wx.WXK_SPECIAL8', 'wx.WXK_SHIFT', 'wx.WXK_NUMPAD7', 'wx.WXK_F12', 'wx.WXK_NUMPAD_DOWN', 'wx.WXK_SPECIAL9', 'wx.WXK_ALT', 'wx.WXK_NUMPAD8', 'wx.WXK_F13', 'wx.WXK_NUMPAD_PRIOR', 'wx.WXK_SPECIAL10', 'wx.WXK_CONTROL', 'wx.WXK_NUMPAD9', 'wx.WXK_F14', 'wx.WXK_NUMPAD_PAGEUP', 'wx.WXK_SPECIAL11', 'wx.WXK_MENU', 'wx.WXK_MULTIPLY', 'wx.WXK_F15', 'wx.WXK_NUMPAD_NEXT', 'wx.WXK_SPECIAL12', 'wx.WXK_PAUSE', 'wx.WXK_ADD', 'wx.WXK_F16', 'wx.WXK_NUMPAD_PAGEDOWN', 'wx.WXK_SPECIAL13', 'wx.WXK_CAPITAL', 'wx.WXK_SEPARATOR', 'wx.WXK_F17', 'wx.WXK_NUMPAD_END', 'wx.WXK_SPECIAL14', 'wx.WXK_PRIOR', 'wx.WXK_SUBTRACT', 'wx.WXK_F18', 'wx.WXK_NUMPAD_BEGIN', 'wx.WXK_SPECIAL15', 'wx.WXK_NEXT', 'wx.WXK_DECIMAL', 'wx.WXK_F19', 'wx.WXK_NUMPAD_INSERT', 'wx.WXK_SPECIAL16', 'wx.WXK_END', 'wx.WXK_DIVIDE', 'wx.WXK_F20', 'wx.WXK_NUMPAD_DELETE', 'wx.WXK_SPECIAL17', 'wx.WXK_HOME', 'wx.WXK_NUMLOCK', 'wx.WXK_F21', 'wx.WXK_NUMPAD_EQUAL', 'wx.WXK_SPECIAL18', 'wx.WXK_LEFT', 'wx.WXK_SCROLL', 'wx.WXK_F22', 'wx.WXK_NUMPAD_MULTIPLY', 'wx.WXK_SPECIAL19', 'wx.WXK_UP', 'wx.WXK_PAGEUP', 'wx.WXK_F23', 'wx.WXK_NUMPAD_ADD', 'wx.WXK_SPECIAL20', 'wx.WXK_RIGHT', 'wx.WXK_PAGEDOWN', 'wx.WXK_F24', 'wx.WXK_NUMPAD_SEPARATOR', 'wx.WXK_DOWN', 'wx.WXK_NUMPAD_SUBTRACT', 'wx.WXK_SELECT', 'wx.WXK_NUMPAD_DECIMAL', 'wx.WXK_PRINT', 'wx.WXK_NUMPAD_DIVIDE']

keyId2Name = {8: 'BACK', 9: 'TAB', 13: 'RETURN', 27: 'ESCAPE', 32: 'SPACE', 127: 'DELETE', 193: 'SPECIAL1', 194: 'SPECIAL2', 195: 'SPECIAL3', 196: 'SPECIAL4', 197: 'SPECIAL5', 198: 'SPECIAL6', 199: 'SPECIAL7', 200: 'SPECIAL8', 201: 'SPECIAL9', 202: 'SPECIAL10', 203: 'SPECIAL11', 204: 'SPECIAL12', 205: 'SPECIAL13', 206: 'SPECIAL14', 207: 'SPECIAL15', 208: 'SPECIAL16', 209: 'SPECIAL17', 210: 'SPECIAL18', 211: 'SPECIAL19', 212: 'SPECIAL20', 301: 'LBUTTON', 302: 'RBUTTON', 303: 'CANCEL', 304: 'MBUTTON', 305: 'CLEAR', 306: 'SHIFT', 307: 'ALT', 308: 'CONTROL', 309: 'MENU', 310: 'PAUSE', 311: 'CAPITAL', 312: 'END', 313: 'HOME', 314: 'LEFT', 315: 'UP', 316: 'RIGHT', 317: 'DOWN', 318: 'SELECT', 319: 'PRINT', 320: 'EXECUTE', 321: 'SNAPSHOT', 322: 'INSERT', 323: 'HELP', 324: 'NUMPAD0', 325: 'NUMPAD1', 326: 'NUMPAD2', 327: 'NUMPAD3', 328: 'NUMPAD4', 329: 'NUMPAD5', 330: 'NUMPAD6', 331: 'NUMPAD7', 332: 'NUMPAD8', 333: 'NUMPAD9', 334: 'MULTIPLY', 335: 'ADD', 336: 'SEPARATOR', 337: 'SUBTRACT', 338: 'DECIMAL', 339: 'DIVIDE', 340: 'F1', 341: 'F2', 342: 'F3', 343: 'F4', 344: 'F5', 345: 'F6', 346: 'F7', 347: 'F8', 348: 'F9', 349: 'F10', 350: 'F11', 351: 'F12', 352: 'F13', 353: 'F14', 354: 'F15', 355: 'F16', 356: 'F17', 357: 'F18', 358: 'F19', 359: 'F20', 360: 'F21', 361: 'F22', 362: 'F23', 363: 'F24', 364: 'NUMLOCK', 365: 'SCROLL', 366: 'PAGEUP', 367: 'PAGEDOWN', 368: 'NUMPAD_SPACE', 369: 'NUMPAD_TAB', 370: 'NUMPAD_ENTER', 371: 'NUMPAD_F1', 372: 'NUMPAD_F2', 373: 'NUMPAD_F3', 374: 'NUMPAD_F4', 375: 'NUMPAD_HOME', 376: 'NUMPAD_LEFT', 377: 'NUMPAD_UP', 378: 'NUMPAD_RIGHT', 379: 'NUMPAD_DOWN', 380: 'NUMPAD_PAGEUP', 381: 'NUMPAD_PAGEDOWN', 382: 'NUMPAD_END', 383: 'NUMPAD_BEGIN', 384: 'NUMPAD_INSERT', 385: 'NUMPAD_DELETE', 386: 'NUMPAD_EQUAL', 387: 'NUMPAD_MULTIPLY', 388: 'NUMPAD_ADD', 389: 'NUMPAD_SEPARATOR', 390: 'NUMPAD_SUBTRACT', 391: 'NUMPAD_DECIMAL', 392: 'NUMPAD_DIVIDE', 393: 'WINDOWS_LEFT', 394: 'WINDOWS_RIGHT', 395: 'WINDOWS_MENU'}

class DemoPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        self.parent = parent  # Sometimes one can use inline Comments
        rb = wx.RadioBox(self, rbId, "Screen mode", wx.DefaultPosition, wx.DefaultSize, ['Window', 'Fullscreen'])
        okcancel = wx.BoxSizer(wx.HORIZONTAL)
        b1 = wx.Button(self, playId, label='Play')
        b2 = wx.Button(self, exitId, label='Exit')
        for b in (b1, b2):
            okcancel.Add(b, 0, wx.ALIGN_RIGHT|wx.ALL, 5)        
        controlbox = wx.StaticBox(self, -1, label='Configure Controls')
        controls = wx.StaticBoxSizer(controlbox, wx.HORIZONTAL)
        #controls = wx.BoxSizer(wx.HORIZONTAL)
        p1 = wx.Button(self, p1Id, label="Player 1")
        p2 = wx.Button(self, p2Id, label="Player 2")
        for p in (p1, p2):
            controls.Add(p, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        self.rb = rb
        #b2.Bind(wx.EVT_BUTTON, self.OnExit)
        #sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)
        #NothingBtn.Bind(wx.EVT_BUTTON, self.DoNothing )

        sizer = wx.BoxSizer(wx.VERTICAL)
        for b in (rb, controls, line, okcancel):
            sizer.Add(b, 0, wx.ALIGN_LEFT|wx.ALL|wx.GROW, 5)
        #keysink = KeySink(self)
        #sizer.Add(keysink, wx.GROW)
        self.SetSizerAndFit(sizer)

class Dialog(wx.Dialog):
    default = {1:'WASDERF1', 2:'IJKLUYH2'}
    joyk = ('up', 'left', 'down', 'right', '1', '2', '3', '4')
    defaultJoy = {1:['J0-%s'%i for i in joyk],  2:['J1-%s'%i for i in joyk]}
    def __init__(self, parent, n, *args):
        wx.Dialog.__init__(self, parent, *args)
        vsizer = wx.BoxSizer(wx.VERTICAL)
        self.n = n
        self.keys = ['up', 'left', 'down', 'right', 'w', 'm', 's', 'start']
        #keylist = []
        self.boxn = 0
        self.boxes = []
        self.filename = '%s/cache/p%dcontrols' % (os.getcwd(), self.n)
        self.t = wx.StaticText(self)        
        vsizer.Add(self.t, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        keyssb = wx.StaticBox(self, -1, 'Configuration')
        keyssbsizer = wx.StaticBoxSizer(keyssb, wx.VERTICAL)
        gridsizer = wx.GridSizer(len(self.keys), 2, 2, 2)
        keyssbsizer.Add(gridsizer, -1, wx.GROW|wx.ALL)
        for n, i in enumerate(self.keys):
           k = wx.StaticText(self, -1, i.upper()+':')
           t = wx.StaticText(self, -1, '%s' % Dialog.default[self.n][n])
           self.boxes.append(t)
           gridsizer.Add(k, -1, flag=wx.ALIGN_RIGHT)
           gridsizer.Add(t, -1, flag=wx.ALIGN_LEFT)
        hsizer2.Add(keyssbsizer, -1, wx.ALL, 2)
        vb = wx.StaticBox(self, -1, 'Reset to Defaults')
        vbsizer = wx.StaticBoxSizer(vb, wx.VERTICAL)
        for n, i in enumerate(['P1 Keyboard', 'P2 Keyboard', 'P1 Joystick', 'P2 Joystick']):
            b = wx.Button(self, 60+n, i)
            vbsizer.Add(b, -1, wx.GROW|wx.ALL, 2)
        hsizer2.Add(vbsizer, -1, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2)
        vsizer.Add(hsizer2, -1, wx.ALL|wx.GROW, 2)
        
        wx.EVT_BUTTON(self, 60, lambda e: self.OnDefault(Dialog.default, 1))
        wx.EVT_BUTTON(self, 61, lambda e: self.OnDefault(Dialog.default, 2))
        wx.EVT_BUTTON(self, 62, lambda e: self.OnDefault(Dialog.defaultJoy, 1))
        wx.EVT_BUTTON(self, 63, lambda e: self.OnDefault(Dialog.defaultJoy, 2))

        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        for x, b in enumerate('Ok Cancel'.split()):
            b = wx.Button(self, 50+x, b)
            hsizer.Add(b, -1, wx.ALL | wx.GROW, 2)
        #vsizer.Add(wx.StaticLine(self, -1, size=(1,-1), style=wx.LI_HORIZONTAL), -1, wx.GROW|wx.ALL)
        vsizer.Add(hsizer, flag=wx.CENTER)
        #self.log = wx.StaticText(self); vsizer.Add(self.log, -1, wx.ALL|wx, 2)
        wx.EVT_BUTTON(self, 50, self.OnOk)
        wx.EVT_BUTTON(self, 51, self.OnCancel)
        #Srwx.EVT_TEXT_CTRL_(self, self.OnKeyUp)
        keysink = KeySink(self)
        keysink.SetSizeWH(0,0)      
        vsizer.Add(keysink)
        self.SetSizerAndFit(vsizer)
        self.UpdateText(None)
        load = cPickle.load(file(self.filename))
        key2i = dict((i,n) for n, i in enumerate(self.keys))
        #cPickle.dump(dict((k, self.default[self.n][n]) for n, k in enumerate(self.keys)), file(self.filename, 'w'))
        #raise 'u'
        for k, v in load.iteritems():
            self.boxes[key2i[k.lower()]].SetLabel(v)
    def UpdateText(self, evt, type=None, n=None, label=None):
        global keyId2Name
        if evt is not None:
            if type == wx.EVT_KEY_UP:
                code = evt.GetKeyCode()
                label =  keyId2Name[code] if code in keyId2Name else chr(code)
            elif type == wx.EVT_JOYSTICK_EVENTS:
                pass # HI THERE
            self.boxes[self.boxn-1].SetLabel('%-9s'%label.upper())
        self.boxes[self.boxn].SetFont(wx.Font(-1,wx.NORMAL,wx.NORMAL,wx.BOLD))
        if self.boxn > 0:
            self.boxes[self.boxn-1].SetFont(wx.Font(-1,wx.NORMAL,wx.NORMAL,wx.NORMAL))
        self.t.SetLabel('Press a key for %s!' % self.keys[self.boxn])
        self.boxn += 1
        if self.boxn == len(self.keys):
            self.OnOk(None)
                    
    def OnOk(self, event):
        dic = dict((k, self.boxes[n].GetLabel().strip()) for n, k in enumerate(self.keys))
        
        with file(self.filename, 'w') as f:
            cPickle.dump(dic, f)
        self.Close()
    def OnCancel(self, event):
        self.Close()
    
    def OnDefault(self, dic, sn):
        for n, i in enumerate(self.keys):
            self.boxes[n].SetLabel(dic[sn][n])
    
        
class KeySink(wx.Window):
    def __init__(self, parent):
        wx.Window.__init__(self, parent, -1)
        self.parent = parent
        self.haveFocus = False
        self.callSkip = True
        self.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
        self.SetFocus()
        self.joysticks = []
        self.firstj = wx.Joystick(wx.JOYSTICK1)
        self.joysticks.append(self.firstj)
        self.firstj.SetCapture(self)
        self.Bind(wx.EVT_JOYSTICK_EVENTS, lambda evt: self.JoyEventHandler(0, evt))        
        for n in range(self.firstj.GetNumberJoysticks()-1):
            j = wx.Joystick(eval('wx.JOYSTICK%d'%n+2))
            j.SetCapture(self)
            self.joysticks.append(j)
            j.Bind(EVT_JOYSTICK_EVENTS, lambda evt: self.JoyEventHandler(n+1, evt))
            raise '%s'%self.joysticks

    def JoyEventHandler(self, n, evt):
        e = evt
        #self.parent.log.SetLabel('%s'%e.GetPosition())
        pos = evt.GetPosition()
        buttons = evt.GetButtonState()
        posname = None
        label = None
        if pos[1] == 0:    posname = 'UP'
        elif pos[1] == -1: posname = 'DOWN'
        elif pos[0] == 0:  posname = 'LEFT'
        elif pos[0] == -1: posname = 'RIGHT'
        
        if posname is not None:
            label = 'J%d-%s' % (n, posname)
        else:
            def func():
                for i in range(4):
                    if buttons & (1<<i):
                        return i
                for i in range(4, 16):
                    if (buttons|8) & (1<<i):
                        return i
                return None
            but = func()
            if but is not None:
                label = 'J%d-%s' % (n, but)
        if label is not None:
            self.parent.UpdateText(evt, wx.EVT_JOYSTICK_EVENTS, n, label)

    def OnKeyUp(self, evt):
        self.parent.UpdateText(evt, wx.EVT_KEY_UP)

class DemoFrame(wx.Frame):
    """Main Frame holding the Panel."""
    def __init__(self, *args, **kwargs):
        global exitId, playId
        wx.Frame.__init__(self, 
            style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.RESIZE_BOX | wx.MAXIMIZE_BOX),
            *args, **kwargs)
        # Add the Widget Panel
        self.Panel = DemoPanel(self)
        self.Fit()
        wx.EVT_BUTTON(self, exitId, self.OnQuit)
        wx.EVT_BUTTON(self, playId, self.OnPlay)
        wx.EVT_BUTTON(self, p1Id, lambda event: self.Config(1, event))
        wx.EVT_BUTTON(self, p2Id, lambda event: self.Config(2, event))
        #self.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
        

        self.dic = {}
        filename = '%s/user.cfg' % os.getcwd()        
        self.usercfg = file(filename, 'r')
        for i in self.usercfg.readlines():
            data, var = i.strip().split(' ')
            self.dic[data] = var
        self.usercfg.close()
        self.Panel.rb.SetSelection(int(self.dic['fullscreen']))
        self.runika = False
    #def OnKeyUp(key, event):
    #    key = event.KeyCode()
    #    raise '%d' % key
    def Config(self, n, event=None):
        dlg = Dialog(self, n, -1, 'Configure Player %d Controls' % n)
        dlg.CenterOnScreen()
        val = dlg.ShowModal()   
        dlg.Destroy()     
    def OnQuit(self, event=None):
        self.Close()
    def OnPlay(self, event=None):
        global runIka
        self.dic['fullscreen'] = '%d'% self.Panel.rb.GetSelection()
        o = file('%s/user.cfg' % os.getcwd(), 'w')
        for k, v in self.dic.iteritems():
            o.write('%s %s\n'% (k, v))
        runIka = True
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    frame = DemoFrame(None, title="Beast Genesis")
    frame.CenterOnScreen()
    frame.Show()
    app.MainLoop()
    if runIka:
        os.system('"%s/ika.exe"' % os.getcwd())
intro = {}

def Get(a, b, t):
    global intro
    if b < a:
        a, b = b, a
    try:
        intro[a, b](t)
    except KeyError:
        return None'Combined intros for characters'
dic = {}

def LivsNancy(self): # I don't care much aobut this..
    pass

dic['li', 'nancy'] = LivsNancy
def lookup(self, name1, name2):
    return dic[sorted(name1, name2)]
from os import *
from ika import *
from zoomblit import ZoomImage
# giancarlo.montalbano@gmail.com
	
obj2ext = {'Image':'png', 'ZoomImage':'png', 'Canvas':'png', 'Sound':'ogg'}

def All(folder_name, obj='ZoomImage', cwd=getcwd()):
	global obj2ext
	fol = '%s/%ss/%s/' % (cwd, 'Image' if obj != 'Sound' else 'Sound', folder_name)
	object = eval(obj)
	fun = lambda i: len(i)> 3 and i[-3:].lower() == obj2ext[obj]
	return dict((i[:-4], object(fol+i)) for i in listdir(fol) if fun(i))
	
#def Cache(text):
#	
	
def FlipAll(folder_name, cwd=getcwd()):
	left, right = {}, {}
	cachefol = '%s/cache' % cwd
	fol = '%s/%s/' % (cachefol, folder_name)
	if folder_name not in listdir(cachefol):
		makedirs(fol)
	dire = listdir(fol)
	if len(dire):
		for k in listdir(fol):
			o = k[1:-4]
			left[o] = Image(fol+k)
			right[o] = Image('%s/Images/%s/%s' % (cwd, folder_name, k[1:]))
	else:
		orig = All(folder_name, obj = 'Canvas')
		for k, v in orig.iteritems():
			right[k] = Image(v)
			v.Mirror()
			left[k] = Image(v)
			v.Save(fol+'l'+k+'.png')
	return (right, left)

#def Cache(source, dest, sourcef, destf, manipf):
#	s = sourcef(source)
	
	
def Flip(dire, im, source=None, saveOriginal=True):
	canv = Canvas(dire+im) if source is None else source
	rc = Canvas(canv.width, canv.height)
	canv.Blit(rc, 0, 0); rc.Mirror()
	#if saveOriginal:
	#	canv.Save(dire+im)
	#rc.Save(dire+'l'+im)
	#im, rim = Image(canv), Image(rc)
	return (canv, rc)from ika import *

def Outline(pic):
	s = set()
	Width, Height = pic.width, pic.height
	for x in xrange(1,Width):
		for y in xrange(1,Height):
			o, a, b = (x,y), (x-1,y), (x,y-1)
			to, ta, tb = tuple(GetRGB(pic.GetPixel(j,k))[3]<32 for j,k in [o,a,b])
			if to and (not ta or not tb):	s.add(o)
			elif not to and tb:				s.add(b)
			elif not to and ta:				s.add(a)
			elif not tb and y == 1:			s.add(b)
			elif not to and y == Height-1:	s.add(o)
			elif not ta and x == 1:			s.add(a)
			elif not to and x == Width-1:	s.add(o)
	return s

def HLines(pic): # Go through each y, then go through each x finding outline points
	min, max = {}, {}
	Width, Height = pic.width, pic.height
	for y in xrange(Height):
		def find_extreme(dic, start, end, step):
			for x in xrange(start, end, step):
				o, a = (x, y), (x-step, y)
				transp = lambda (x,y): GetRGB(pic.GetPixel(x,y))[3]<16 
				to, ta  = transp(o), transp(a)
				if not to and ta or (not ta and x == start):
					dic[y] = x
					break
		find_extreme(min, 1, Width, 1)
		find_extreme(max, Width-2, -1, -1)
	return dict((k,(min[k],max[k])) for k in min)

def VLines(pic): # Go through each x, then go through each y finding outline points	
	min, max = {}, {}
	Width, Height = pic.width, pic.height
	for x in xrange(Width):
		def find_extreme(dic, start, end, step):
			for y in xrange(start, end, step):
				o, a = (x, y), (x, y-step)
				transp = lambda (x,y): GetRGB(pic.GetPixel(x,y))[3]<16 
				to, ta  = transp(o), transp(a)
				if not to and ta or (not ta and y==start):
					dic[x] = y
					break
		find_extreme(min, 1, Height, 1)
		find_extreme(max, Height-2, -1, -1)
	return dict((k,(min[k],max[k])) for k in min)

def Lines(pic):
	return (HLines(pic), VLines(pic))#@PydevCodeAnalysisIgnore
from distutils.core import setup
import py2exe
setup(console=['gui.py'])from ika import Video, RGB, Random
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
            Video.DrawLine(x+self.rx(), y1+self.ry(), x+self.rx(), y2+self.ry(), self.vc)        from screens import config
from sysobj import CollisionTester
import cPickle
import intro
try:
	import psyco; psyco.full() #@UnresolvedImport
except ImportError: pass
from ika import *
from xi import fps
#from cProfile import runctx
from os import getcwd, listdir, mkdir, path
cwd, f = getcwd(), Font('font.fnt') # ugly, butworks
from chars import genjuro, kyo, player #@UnusedImport
import load, cPickle
from screens import edit, select, title, vs, control, menu, story
#from threading import Thread, Lock
#import profile
import sysobj
from math import sqrt
from zoomblit import ZoomImage
import os
from time import time, strftime, localtime

clamp = lambda n, mn, mx: max(mn, min(n, mx))
# open

def reset_cache(): 
	global cwd	
	moddic = cPickle.load(file('%s/cache/mod' % cwd))
	def removeifexist(filename):
		if path.isfile(filename):
			os.remove(filename)
			print 'removing...', filename
	for char in listdir('%s/Images/characters' % cwd):
		for im in listdir('%s/Images/characters/%s' % (cwd, char)):			
			filename = '%s/Images/characters/%s/%s' % (cwd, char, im)
			tim = path.getmtime(filename)
			if tim != moddic.get(char+im, None):
				removeifexist('%s/cache/outline/%s/self%s' % (cwd, char, im[:-4]))
				removeifexist('%s/cache/outline/%s/hit%s' % (cwd, char, im[:-4]))
				moddic[char+im] = tim
		cPickle.dump(moddic, file('%s/cache/mod' % cwd, 'w'))
reset_cache()
#===============================================================================
# def Test():
#	'load two images then build a dict from colors A to colors B, then use the dict to make a colorized image'
#	img1 = Canvas('%s/Images/characters/li/w-00.png'%cwd)
#	img2 = Canvas('%s/Images/colorizer/li.png'%cwd)
#	img3 = Canvas('%s/Images/characters/li/w-01.png'%cwd)
#	dic = {}
#	for x in xrange(img1.width):
#		for y in xrange(img1.height):
#			dic[img1.GetPixel(x,y)] = img2.GetPixel(x,y)
#	for k, v in dic.iteritems():
#		try:
#			print '%d->%d' % (GetRGB(k), GetRGB(v))
#		except TypeError:
#			print '%d->%d' % (k, v)
#	for x in xrange(img3.width):		
#		for y in xrange(img3.height):
#			img3.SetPixel(x, y, dic[img3.GetPixel(x,y)])
#	img4 = Image(img3)
#	while True:
#		img4.Blit(0,0)
#		Video.ShowPage()
# Test()
#===============================================================================


def Blur(canv):
	for x in range(1,640-1):
		for y in range(1,480-1):
			g = canv.GetPixel(x, y)
			c = GetRGB(g)
			for p in [(x-1,y), (x+1, y), (x, y-1), (x, y+1)]:
				x1, y1 = p
				o = GetRGB(canv.GetPixel(x1, y1))
				canv.SetPixel(x1, y1, RGB((c[0]+o[0])/2, (c[1]+o[1])/2, (c[2]+o[2])/2))
	return Image(canv)

VLine = lambda x, y1, y2, c: Video.DrawLine(x, y1, x, y2, c)
HLine = lambda x1, y, x2, c: Video.DrawLine(x1, y, x2, y, c)

class MyFont:
	def __init__(self, name, area, debug = False):
		#Thread.__init__(self)
		self.name, self.area = name, area
		self.chars = ' !\"#$ &\'()^+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		self.letterspan = {} # The span of each individual letter in the picture
		self.spanname = name[:-4]+'span'
		self.done = False
		#self.start()
	#def run(self):
		imname = '%s/Images/system/fonts/%s' % (self.area.cwd, self.name)
		lastx = i = 0
		try:
			self.letterspan = self.area.load(self.spanname)
			self.pic = Image(imname)
		except IOError:
			print 'Making font' + imname
			self.pic = Canvas(imname)
			c = self.pic.GetPixel(0,0)
			for x in range(self.pic.width):
				if self.pic.GetPixel(x, 0) == c:
					self.letterspan[self.chars[i]] = (lastx, x)
					lastx = x
					i += 1
			area.save(self.spanname, self.letterspan)
			self.pic = Image(self.pic)
		self.h = self.pic.height
		self.done = True
	def Print(self, x, y, text, tint = None, debug = False):
		if self.done:
			curx = x
			for c in text:
				x1, x2 = self.letterspan[c]
				span = x2-x1
				Video.ClipBlit(self.pic, curx, y, x1, 0, span, self.h-1)
				curx += span
	def width(self, text):
		return sum(self.letterspan[i][1] - self.letterspan[i][0] for i in text)
	def CenterXPrint(self, y, text):
		if self.done:
			leng = self.width(text)
			self.Print(320-leng/2, y, text)
	def CenterPrint(self, text):
		self.CenterXPrint(240-self.h/2, text)

class Area:
	x = 255
	r, g, b = RGB(x,0,0), RGB(0,x,0), RGB(0,0,x)
	c, y, m = RGB(0,x,x), RGB(x,x,0), RGB(x,0,x)
	black, white = RGB(0,0,0), RGB(x,x,x)
	rainbow = [r,y,g,c,b,m]
	def __init__(self):
		global cwd, f
		SetCaption('Beast Genesis') #@UndefinedVariable
		self.f, self.cwd = f, cwd
		# Make the base cache folders if they don't exist		
		self.cachefol = '%s/cache/' % self.cwd
		self.fols = dict(
			imfol = '%s/Images/characters/' % self.cwd,
			outlinefol = '%s/cache/outline/' % self.cwd,
			reversefol = '%s/Images/cache/characters/' % self.cwd,
			hitfolcache = '%s/Images/cache/hitbox/' % self.cwd,
			hitfolsrc = '%s/Images/hitbox/' % self.cwd)
		for char in listdir(self.fols['imfol']): # Make dirs if they don't exist
			for fol in self.fols.values():
				if char not in listdir(fol):
					mkdir(fol+char)
		# Set the attributes for player 1 and 2 that are different
		# Initialize map stuff	
		self.maxt = 30*60
		self.bg = Image(getcwd()+'/images/bg/training.png')
		self.width, self.height =  1500, 900
		self.zoomx1, self.zoomy1, self.zoomx2, self.zoomy2 = 0, 0, 640, 480
		self.nrounds = 2
		self.jumpn = 0
		self.objects = []
		fontdir = listdir('%s/Images/system/fonts'%self.cwd)
		self.font = dict((i[:-4], MyFont(i,self)) for i in fontdir)
		self.combo = 0
		self.mode, self.modet = 'intro', 30
		self.winnar = ''
		self.strikim = load.All('strike', cwd=self.cwd)
		self.logoim = Image('%s/Images/system/title/metal-logo.png' % self.cwd)
		self.totalwins = 0
		self.roundn = lambda: self.p1.wins + self.p2.wins
		self.dp1, self.dp2 = player.DummyPlayer(self, 'p1'), player.DummyPlayer(self, 'p2')
		self.dp1.pname, self.dp2.pname = 'p1', 'p2'
		self.titlemode = ''
		self.title = title.Title(area=self)		
		self.pausemenu = menu.Menu(['RETURN', 'CONTROLS', 'MOVE LIST', 'CHARACTER', 'EXIT'], area=self)
		self.select = select.Select(self.dp1, self.dp2, area=self)
		self.done = False
		self.config = config.Config(area=self)

	def changehp(self, p, n):
		p.hp = max(p.hp+n, 0)
		p.hpdecr = max(p.hpdecr-n, 0)
	def changebar(self, p, n):
		p.bar = max(p.bar+n, 0)
		p.bardecr = max(p.bardecr-n, 0)
	def resetbattles(self, init=False): # Several rounds
		self.select.do()
		#self.font['menuwhite'].CenterPrint('LOADING...')
		#Video.ShowPage()
		samechar = self.dp1.name == self.dp2.name
		self.p1 = eval('%s.%s' % (self.dp1.name,self.dp1.name))(area=self, pname='p1', samechar=samechar)
		self.p2 = eval('%s.%s' % (self.dp2.name,self.dp2.name))(area=self, pname='p2', samechar=samechar)
		
		vs.Vs(self.p1, self.p2, area=self).do()
		
		self.p1.defaultFacing, self.p2.defaultFacing = 1, -1
		self.p1.barim, self.p2.barim = load.FlipAll('bars')
		self.p1.barx, self.p2.barx = 20, 360
		self.p1.bar1x, self.p2.bar1x = 33, 393
		self.p1.bar2x, self.p2.bar2x = 144, 392
		self.p1.combox, self.p2.combox = 20, 360
		self.p1.pname, self.p2.pname = 'p1', 'p2'
		self.p1.roundx, self.p2.roundx = 134, 510
		self.p1.wins, self.p2.wins = 0, 0
		self.p1.controls, self.p2.controls = self.dp1.controls, self.dp2.controls
		if init:
			self.p1.wins = self.p2.wins = 0
			self.winstreak = 0
			self.rwinner = None
		if self.rwinner is not None and self.rwinner.name == self.winnar:
			self.winstreak += 1
		else:
			self.winstreak = 0
			self.rwinner = self.p1 if self.p1.name == self.winnar else self.p2	
		self.resetbattle()

	def save(self, name, data): # Save system data
		outf = file(self.cachefol+name,'w')
		cPickle.dump(data, outf)
	def load(self, name):
		return cPickle.load(file(self.cachefol+name))		

	def resetbattle(self):
		self.t = self.maxt
		self.p1.x, self.p1.y, self.p2.x, self.p2.y = 650, 680, 850, 680
		self.p1.facing, self.p2.facing = 1, -1
		self.objects = []
		for p in [self.p1, self.p2]:
			p.changestate('stand')
			p.dx = p.dy = 0
			p.alreadyHit = False
			p.hp = 1000
			p.bar = 500
			p.movet = 0
			p.hpdecr = p.bardecr = 0
 			p.holdback = self.holddown = 0
 			p.combo = 0

	def titlemain(self):
		if self.titlemode == '':
			self.titlemode = self.title.do()
		elif self.titlemode in ('ARCADE', 'VS MODE', 'TRAINING'):
			self.resetbattles(init=True)
			fp = fps.FPSManager(60)
			while self.titlemode in ('ARCADE', 'VS MODE', 'TRAINING'):
				fp.render(self.main)
		elif self.titlemode == 'EXIT':
			self.done = True
		elif self.titlemode == 'OPTIONS':
			self.config.do()
	
	def main(self): # Called between ticks. State machine
		self.modet -= 1
		def onend(mode, t=30):
			if self.modet == 0:
				self.mode, self.modet = mode, t
				return True
			return False
		if self.mode == 'endround':
			self.tick('')
			if 60 < self.modet < 120:
				self.font['metal'].CenterXPrint(200, 'TIME UP' if self.t < 2 else 'KNOCK OUT')
			else:
				self.font['metal'].CenterXPrint(200, self.winnar)
			onend('intro', 4*30)
		elif self.mode == 'intro': # Intro
			if max(self.p1.wins, self.p2.wins) >= self.nrounds: # Dump back to character select.
				self.resetbattles()
			if intro.Get(self.p1.name, self.p2.name, self.modet) is None:
				self.maxmodet = 4*30
				self.p1.intro()
				self.p2.intro()				
			self.tick('')		
			if self.modet == 4*30 - 1:
				self.resetbattle()
			elif  2 * 30 < self.modet < 4*30:
				self.font['metal'].CenterXPrint(200, 'ROUND %d' % (self.roundn()+1))
			else:
				self.font['metal'].CenterXPrint(200, 'START')
			onend('control', 0)
		elif self.mode == 'super':
			self.tick('')
			self.superp.tintcolor = Area.rainbow[self.modet/2 % 6]
			t = self.modet*4 / 120.0
			Video.DrawEllipse(self.superp.x, self.superp.y, int(t*self.superp.w2()), int(t*self.superp.height()/2), RGB(255,255,255,128))
			if onend('control',0):
				self.superp.tintcolor = RGB(255,255,255,255)
		elif self.mode == 'hit':
			self.tick('control')
			Video.DrawRect(0,0,640,480,RGB(255,0,0,128+abs(5-self.modet)*8), 1)
			onend('control', 0)
		else:
			self.tick('control')
			if self.p1.hp < 1 or self.p2.hp < 1 or self.t == 0:
				self.p1.hp, self.p2.hp = max(0, self.p1.hp), max(0, self.p2.hp)
				if self.p1.hp < self.p2.hp:
					self.p2.wins += 1
					self.winnar = 'PLAYER 2 WINS'
				elif self.p2.hp < self.p1.hp:
					self.p1.wins += 1
					self.winnar = 'PLAYER 1 WINS'
				else:
					self.p1.wins += 1
					self.p2.wins += 1
					self.winnar = 'DRAW'
				self.mode, self.modet = 'endround', 2*60
		if Input.keyboard['F1'].Pressed():
			self.screenshot()
	def screenshot(self):
			screenshot = Video.GrabCanvas(0,0,640,480)
			n = 0
			for i in listdir(self.cwd):
				split = i.split('-')
				if split[0] == 'screenshot':
					n = max(int(split[1][:-4]), n)
			screenshot.Save('%s/screenshot-%02d.png' % (self.cwd, n+1))						
	def tick(self, mode = 'control'):
		#leastx = min(self.p1.bedge(), self.p2.bedge())
		clamp = lambda n, mn, mx: max(mn, min(n, mx))
		midx, midy = (self.p1.sedge() + self.p2.sedge())/2, (self.p1.y+self.p2.y-self.p1.sheight()-self.p2.sheight())/2
		midx2 = (self.p1.x+self.p2.x)/2
		self.zoomx1 = clamp(midx2-320, 0,self.width-640)
		self.zoomy1 = clamp(midy, 0, 900-480)
		self.zoomx2 = self.zoomx1 + 640
		self.zoomy2 = self.zoomy1 + 480
		#self.f.Print(300,0,'%3d %3d->%3d %3d midx=%3d dist=%3d' % (self.zoomx1, self.zoomy1, self.zoomx2, self.zoomy2, midx, abs(self.p2.x-self.p1.x)))			
		if mode == 'control':
			self.t -= 1
			for p, o in [(self.p1, self.p2), (self.p2, self.p1)]:		
				p.dx = clamp(p.dx, -p.maxspeed, p.maxspeed)
				p.x, p.y = p.x+p.dx, p.y+p.dy
				if p.y >= 680 and p.state[1] == '8':
					p.movet = 0 # Stops all air attacks...
				p.x, p.y = clamp(p.x,0,1499),clamp(p.y,0,680) # clamp to stage
				if p.y < 680:
					p.x = clamp(p.x, 1, 1498) # Additional clampage.
				if p.y == 680:
					p.dx = int(p.dx*0.8)
				if 1 < p.dx < -1:
					p.dx = 0
				if p.state == 'stand':
					p.dx = clamp(p.dx, -p.maxwalk, p.maxwalk)					
				p.x = clamp(p.x, self.zoomx1, self.zoomx1+640)
				if p.bar < 1000:
					self.changebar(p, sqrt(max(p.dx*p.facing,0))/2)		
			getpo = lambda cond:(self.p1, self.p2) if cond else (self.p2, self.p1)
			xcond = abs(self.p1.x-self.p2.x) < (self.p1.sw2()+self.p2.sw2())
			p, o = getpo(self.p1.y < self.p2.y)
			ycond = p.y <= o.y <= p.y + p.sheight()
			print '%d <= %d <= %d = %s' % (p.y, o.y, p.y+p.sheight()*3/4, ycond)  
			if 'thrown' not in [self.p1.state, self.p2.state] and xcond and ycond:		
				if self.p1.y == self.p2.y == 680 or 'airdash' in [self.p1.state, self.p2.state]:				 
					p, o = getpo(abs(self.p1.dx) >= abs(self.p2.dx))
					p.x = midx-p.sdedge()+(p.dx+o.dx)
					o.x = midx-o.sdedge()+(p.dx+o.dx)
					p.x, o.x = max(p.x, 0), max(o.x, 0)
					p, o = getpo(self.p1.x < self.p2.x)
					p.x = clamp(p.x, 0, self.width - p.sw2() - o.sw2() - 1)
					o.x = clamp(o.x, p.sw2()+o.sw2(), self.width - 1)
				elif 680 in [self.p1.y, self.p2.y]:
					p, o = getpo(self.p1.y > self.p2.y)
					if o.x > p.x: # Move ->
						o.x = p.x+o.sw2()+p.sw2()
					elif o.x < p.x: # Move <-
						o.x = p.x-o.sw2()-p.sw2()
		Video.ClipBlit(self.bg, 0, 0, self.zoomx1, 420 - self.zoomy1, 640, 480)
		
		for p, o in [(self.p1, self.p2), (self.p2, self.p1)]:
			if mode == 'control':
				if self.mode == 'buffer':
					p.checkattacks(o)
				else:
					p.tick(o)

			p.draw_shadow(p.x-self.zoomx1, p.y-self.zoomy1)

			
		for p in (a.p1, a.p2):
			p.draw(p.x-self.zoomx1, p.y-self.zoomy1)
		for i in self.objects:
			i.tick(self)
		self.objects = [i for i in self.objects if i.t > 0] # Delete thingies whoes timers expired
		
		#self.zoom(midx)
						
		if Input.keyboard['3'].Pressed():edit.Edit(self.p1, area=self).do()
		if Input.keyboard['4'].Pressed():edit.Edit(self.p2, area=self).do()
		
		#self.f.Print(200, 200, 'midx=%d, zoom=%d' % (midx-self.zoomx1, xdisp)) # As midx increases, zoom left
		for p, o in [(self.p1, self.p2), (self.p2, self.p1)]:
			pb, hit = p.selfbox1(), o.hitbox1()
			px, py = p.x+p.cx(), p.y+p.cy()
			ox, oy = o.x+o.cx(), o.y+o.cy()

			if hit is not None:
				oxp, oyp = o.cat().addxy(o)
				result = self.collide((p, p.width(), pb, px, py), (o, o.cat().width(o), hit, ox+oxp, oy+oyp))
				if result is not None:
					x, y = result
					if self.resolveHit(o.cat(), result, p, o):
						name = ''.join([i for i in 'wms' if i in o.state])
						dic = {'w':4, 'm':5, 's':7}
						frames = dic[name]
						self.objects.append(sysobj.LightStrike(self, x, y, p, o, 10, 'block-'+name, frames))
			
			p.hpdecr = max(0, p.hpdecr-max(p.hpdecr/64, 1))
			p.bardecr = max(0, p.bardecr-max(p.bardecr/64, 1))
			
			f = p.defaultFacing
			x1 = 30
			lifebar, guardbar = p.barim['lifebar'], p.barim['guard-bar']
			p.barim['top-bar'].Blit(p.barx, x1)

			MaxHP = MaxBar = 1000
			hpn, barn = 217*p.hp/MaxHP, 107*p.bar/MaxBar
			hpdn, bardn = 217*(p.hpdecr)/MaxHP, 107*(p.bardecr)/MaxBar
			if f == -1:
				Video.ClipBlit(lifebar, p.bar1x, 34, 0, 0, hpn, 9)
				Video.ClipBlit(guardbar, p.bar2x, 49, 0, 0, barn, 3)
			else:
				lo, lg = 217-hpn, 107-barn
				Video.ClipBlit(lifebar, p.bar1x+lo, 34, lo, 0, hpn, 9)
				Video.ClipBlit(guardbar, p.bar2x+lg, 49, lg, 0, barn, 3)
			if p.hpdecr > 0:
				if f == 1:
					s1, e1 = p.bar1x+217-hpn-hpdn, p.bar1x+216-hpn
				else:
					s1, e1 = p.bar1x+hpn, p.bar1x+hpn+hpdn
				Video.DrawRect(s1, 34, e1, 42, RGB(255,0,0,128), 1)
			if p.bardecr > 0:
				if f == 1:
					s2, e2 = p.bar2x+107-barn-bardn, p.bar2x+106-barn
				else:
					s2, e2 = p.bar2x+barn, p.bar2x+bardn+barn
				Video.DrawRect(s2, 49, e2, 52, RGB(128,128,128,128), 1)				
			self.f.Print(p.barx+50, 35, '%s:%d'% (p.name, p.hp))			
			self.f.Print(p.barx-20, 8, '%3d+%3d,%3d+%3d %2d %-8s %-8s' % (p.x,p.dx,p.y,p.dy,p.movet,p.state,p.drawstate()))
			self.f.Print(p.barx-20, 16,'%-5s %-6s %2d %3d %3d %3d' % (p.alreadyHit, p.next, p.facing, p.holdback, p.holddown, p.holdt))
			for i in range(self.nrounds):
					Video.DrawEllipse(p.roundx+10*-p.defaultFacing*i, 54, 4, 4, RGB(0,255,255),1 if p.wins>i else 0)
			if p.combo > 0:
				self.font['metal'].Print(p.combox, 230, 'COMBO: %2d'% (p.combo+1))
			if p.start.Pressed():
				grab = Video.GrabImage(0,0,640,480)
				choice = self.pausemenu.do(p, img=grab)
				if choice == 'EXIT':
					self.titlemode = ''
				elif choice == 'CHARACTER':
					self.resetbattles()
				elif choice == 'MOVE LIST':
					menu.CommandList(p, area=self).do(img=grab)
				elif choice == 'CONTROLS':
					p.controls.do()
			if p.movet > 0 and self.mode == 'hit': # Pushing on attacks; o is attacker
				if (o.facing == 1 and p.x >= self.width-4) or (o.facing == -1 and p.x <= 3):
					d = clamp(p.x, 0, self.width-1)
					o.x -= max(3, abs(p.x-d))*o.facing
					p.x = d
				else:
					p.x += 3*o.facing

		self.font['metal'].Print(305, 30, '%02d'%(self.t/60))
		self.f.Print(0, 0, '%s%d' % (self.mode, self.modet))

	def zoom(self, midx):		
		#myimg = Video.GrabImage(0,0,640,480)
		myimg = GetScreenImage()
		zoom = (640 - max(abs(self.p1.x - self.p2.x), abs(self.p1.y - self.p2.y)))/8		
		xdisp = (320 - (midx - self.zoomx1))*zoom/300
		#xdisp = zoom+(320-(midx-self.zoomx1))/320
		x1, y1 = -zoom + xdisp, -zoom*7/4
		x2, y2 = zoom+640 + xdisp, 480
		myimg.DistortBlit((x1, y1), (x2, y1), (x2, y2), (x1, y2))

	def resolveHit(self, at, result, p, o, backPush = True):		
		if not o.alreadyHit or o.movet in at.hitlist:
			x, y = result
			o.alreadyHit = True
			if p.state in ['hit', 'throwstun']:
				o.combo += 1
			p.dx, p.dy = 0, 0
			p.state, p.movet = ('hit', at.hit) if p.state != 'block' else ('ghit', at.ghit)
			if p.state == 'hit':
				self.changehp(p, -at.dmg)						
			p.backPush = backPush
			self.mode = 'hit'; self.modet = 10
		else:
			return False
		return True
	def collide(self, ptup, otup):		
		def log(x, y, t):			
			self.f.Print(x, y, t)
			return x + y
		(p, pwide, plines, px, py) = ptup
		(o, owide, olines, ox, oy) = otup
		#tup = [ptup, otup]
		px -= self.zoomx1; py -= self.zoomy1
		ox -= self.zoomx1; oy -= self.zoomy1
		sumx, sumy = [], []
		invo = lambda x: x if o.facing==1 else owide-x
		invp = lambda x: x if p.facing==1 else pwide-x
		for y, (hx1, hx2) in olines[0].iteritems():
			try:
				sx1, sx2 = plines[0][y+(oy-py)]
				hmin, hmax = invo(hx1)+ox, invo(hx2)+ox
				smin, smax = invp(sx1)+px, invp(sx2)+px
				
				if hmin > hmax: hmin, hmax = hmax, hmin
				if smin > smax: smin, smax = smax, smin
				
				HLine(hmin, oy+y, hmax, RGB(255,0,0,128))
				HLine(smin, oy+y, smax, RGB(0,0,255,128))
	
				if smin<hmax and smax>hmin:
					sumx += [smin, smax]
			except KeyError: pass

		for x, (hy1, hy2) in olines[1].iteritems():
			try:
				hmin, hmax = hy1+oy, hy2+oy
				var = invp(invo(x))+(ox-px)*p.facing
				# nancy = 1, li = -1
				# nancy  = 1, li = -1				
				#VLine(invo(x)+ox, hmin, hmax, RGB(255,0,0,128))
				#VLine(invo(x)+ox, smin, smax, RGB(0,0,255,128))
				#f.Print(100, 100+x*16, 'ox=%d, px=%d, d=%d, invo=%d, invp=%d, var=%d ' % (ox, px, ox-px, invo(x), invp(invo(x)), var)) 
				sy1, sy2 = plines[1][var]
				smin, smax = sy1+py, sy2+py
				
				if smin<hmax and smax>hmin:
					sumy += [smin, smax]
			except KeyError: pass
		lx, ly = len(sumx), len(sumy)
		return None if 0 in (lx, ly) else (sum(sumx)/lx, sum(sumy)/ly)
	def dosuper(self, p):
		self.mode = 'super'
		self.modet = 1*60
		self.superp = p
	def do(self):
		self.done = False
		while not self.done:
			Input.Update()
			self.titlemain()
a = Area()
a.do()
#runctx('a.do()', globals(), locals())#@PydevCodeAnalysisIgnore
import wx
import os

class Keys(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Dialog.__init__(self, parent, *args, **kwargs)
        pass


class DemoPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        rbId, playId, exitId, p1ControlsId, p2ControlsId = tuple(range(10,15))
        self.parent = parent  # Sometimes one can use inline Comments
        rb = wx.RadioBox(self, rbId, "Screen mode", wx.DefaultPosition, wx.DefaultSize, ['Full Screen', 'Window'])
        okcancel = wx.BoxSizer(wx.HORIZONTAL)
        b1 = wx.Button(self, playId, label='Play')
        b2 = wx.Button(self, exitId, label='Exit')
        for b in (b1, b2):
            okcancel.Add(b, 0, wx.ALIGN_LEFT|wx.ALL, 5)        
        controls = wx.BoxSizer(wx.HORIZONTAL)
        p1 = wx.Button(self, p1Id, label="P1 Controls")
        p2 = wx.Button(self, p2Id, label="P2 Controls")
        for p in (p1, p2):
            controls.Add(p, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        wx.EVT_BUTTON(self, exitId, self.OnExit)
        #b2.Bind(wx.EVT_BUTTON, self.OnExit)
        #sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)
        #NothingBtn.Bind(wx.EVT_BUTTON, self.DoNothing )

        sizer = wx.BoxSizer(wx.VERTICAL)
        for b in (rb, controls, line, okcancel):
            sizer.Add(b, 0, wx.ALIGN_LEFT|wx.ALL|wx.GROW, 5)

        self.SetSizerAndFit(sizer)

    def OnExit(self, event=None):
        self.Close(True)

    def OnMsgBtn(self, event=None):
        """Bring up a wx.MessageDialog with a useless message."""
        dlg = wx.MessageDialog(self,
                               message='A completely useless message',
                               caption='A Message Box',
                               style=wx.OK|wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()

class DemoFrame(wx.Frame):
    """Main Frame holding the Panel."""
    def __init__(self, *args, **kwargs):
        """Create the DemoFrame."""
        wx.Frame.__init__(self, 
            style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.RESIZE_BOX | wx.MAXIMIZE_BOX),
            *args, **kwargs)
        # Add the Widget Panel
        self.Panel = DemoPanel(self)
        self.Fit()

    def OnQuit(self, event=None):
        """Exit application."""
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    frame = DemoFrame(None, title="Beast Genesis")
    frame.Show()
    app.MainLoop()import __main__
import unittest
import system


if __name__ == __main__:
    unittest.main()

import ika

class ZoomImage:
    def __init__(self, *args):
        self.im = ika.Image(*args)
        self.width, self.height = self.im.width, self.im.height        
        self.Blit = lambda *args: self.im.Blit(*args)
        self.TintDistortBlit = lambda *args: ika.Video.TintDistortBlit(self.im, *args)
        self.TintBlit = lambda *args: ika.Video.TintBlit(self.im, *args)
        self.ScaleBlit = lambda *args: self.im.ScaleBlit(*args)
    def ZoomBlit(self, x, y, facing=1, tint=None):
        x2, y2 = x+self.width, y+self.height
        if tint is None:
            if facing == 1:
                self.im.Blit(x, y)
            else:
                self.im.DistortBlit((x2, y), (x, y), (x, y2), (x2, y2))
        else:
            if facing == 1:
                ika.Video.TintBlit(self.im, x, y, tint)
            else:
                ika.Video.TintDistortBlit(self.im, (x2, y, tint), (x, y, tint), (x, y2, tint), (x2, y2, tint))