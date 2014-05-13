from ika import *
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
		#self.p.save('cnames',  self.key2name)