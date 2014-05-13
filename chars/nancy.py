from player import Player
from attack import Extend, Pre, BehindTeleport, FarLeftTeleport, FarRightTeleport 
from ika import RGB
import sysobj

class nancy(Player):
	def __init__(self, **args):
		def makeTeleport(key, func, len=40):
			return Pre(name='22%s'%key, imgname='tele', alen=len,funcs={len/2:func})
		def NancyBall(p, o, a):			
			a.objects.append(sysobj.UndergroundBall(a, o.x, o.y, p, o, name='ball'))
		at = [Extend(49, 47, 120, name='w', imgname='m', dmg=20, hit=33, alen=26),
			  Extend(49, 47, 250, name='m', imgname='m', dmg=40, hit=35, alen=31),
			  Extend(49, 47, 400, name='s', imgname='m', dmg=80, hit=39, alen=35),
			  Pre(name='236m', dmg=50, hit=20, alen=90, push=(-1,0), cycle=5, cycleframe=4),
			  Extend(37, 37, 600, name='41236S', imgname='236236m', dmg=350, alen=60, super=True, barcost=5001),
			  makeTeleport('m', BehindTeleport, len=30),
			  makeTeleport('w', FarLeftTeleport, len=70),
			  makeTeleport('s', FarRightTeleport, len=70),
			  Pre(name='[4]6m', imgname='tele', alen=30, dmg=100, holdback=60, funcs={15:NancyBall})
		]
		dic = {RGB(192,74,77):RGB(60,119,152), RGB(143,76,82):RGB(65,92,107),
		RGB(60,119,152):RGB(192,74,77), RGB(65,92,107):RGB(143,76,82)}
		Player.__init__(self, name='nancy', at=at, p1colors=dic, **args)
#	def intro(self, t):
#		self.state = 'intro'
		