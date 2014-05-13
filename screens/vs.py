from ika import *
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
		Screen.do(self)