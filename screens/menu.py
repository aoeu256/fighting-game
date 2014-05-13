from ika import *
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
		Menu.do(self, self.p, img)