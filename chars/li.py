from player import Player
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
			Video.DrawEllipse(x, y, 8, 8, RGB(0,255,0,128), 1)