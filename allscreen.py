from ika import *
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
		Screen.do(self)