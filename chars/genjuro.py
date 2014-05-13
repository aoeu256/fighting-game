from player import Player
from attack import Extend, Pre, BehindTeleport, FarLeftTeleport, FarRightTeleport 
from ika import RGB
import sysobj

class genjuro(Player):
    def __init__(self, **args):
        def NancyBall(p, o, a):            
            a.objects.append(sysobj.UndergroundBall(a, o.x, o.y, p, o, name='ball'))

        at = [Pre(name='m', dmg=60, hit=33, alen=50),
              Pre(name='[4]6s', imgname='m', dmg=30, hit=20, alen=20, funcs={10:NancyBall})
        ]
        dic = {RGB(192,74,77):RGB(60,119,152), RGB(143,76,82):RGB(65,92,107),
        RGB(60,119,152):RGB(192,74,77), RGB(65,92,107):RGB(143,76,82)}
        Player.__init__(self, name='genjuro', at=at, p1colors=dic, **args)
        self.drawstatef['intro'] = lambda: 'stand'
        self.drawstatef['stand'] = lambda: 'stand'
        self.drawstatef['crouch'] = lambda: 'crouch'