from player import Player
from attack import Extend, Pre, BehindTeleport, FarLeftTeleport, FarRightTeleport, Air, Spawn 
from ika import RGB
import sysobj

class kyo(Player):
    def __init__(self, **args):
        def LiFire(p, o, a):
            Spawn(p, o, a, name='fireball', dx=8*p.facing)
        def LiHole(p, o, a):
            a.objects.append(sysobj.BlackHole(a, p.edge(), p.y, p, o))
        def mkBubble(p, o, a):
            a.objects.append(sysobj.Bubble(a, p.edge(), p.y, p, o, dx=1*p.facing))

        at = [Pre(name='s', dmg=60, hit=10, alen=40),
              Pre(name='2s',dmg=60, hit=10, alen=40),
              Pre(name='22m', imgname='2s', hit=40, ghit=40, alen=20, funcs={20:mkBubble}),
              Pre(name='236s', imgname='2s', hit=40, ghit=40, alen=40, funcs={35:LiFire}),
              Pre(name='623m', imgname='2s', hit=40, ghit=40, alen=20, funcs={10:LiHole}),
              Air(name='8s', dmg=60, hit=12, alen=25)
        ]
        dic = {RGB(192,74,77):RGB(60,119,152), RGB(143,76,82):RGB(65,92,107),
        RGB(60,119,152):RGB(192,74,77), RGB(65,92,107):RGB(143,76,82)}
        Player.__init__(self, name='kyo', at=at, p1colors=dic, **args)