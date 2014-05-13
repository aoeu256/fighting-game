from ika import *
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
			Input.Update()