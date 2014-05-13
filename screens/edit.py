from ika import RGB, Input, Video
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
		self.p.save('center', self.p.center)