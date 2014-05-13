from ika import *
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
		return 'VS MODE'