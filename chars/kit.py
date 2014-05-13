from player import Player
from attack import * 
from ika import RGB

class kit(Player):
	def __init__(self, **args):
		at = [Pre(name='w', dmg=30, hit=30, alen=30)
			]
		dic = {RGB(192,74,77):RGB(60,119,152), RGB(143,76,82):RGB(65,92,107),
		RGB(60,119,152):RGB(192,74,77), RGB(65,92,107):RGB(143,76,82)}			
		Player.__init__(self, at=at, name='kit', p1colors=dic, **args)
		#stdatks = ['w','m','s','2w','2m','2s','8w','8m','8s']
