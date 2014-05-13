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
        return self.hitbox1() is not None