from ika import *
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
		#self.p2.name, self.p1.name = 'genjuro', 'kyo'