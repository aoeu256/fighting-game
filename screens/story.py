from ika import *
from screen import Screen

text = """
This one big dude came and stole everyone's souls!!!!
That is because he wanted to beat all of the strongest
people in the world!!!!!!  So these strongest people
will compete for their souls!!!!!  These are the people
that will use the cheapest fighting styles to win!!!!!"""

class Story(Screen):
	def __init__(self, **args):
		self.textall = text.split('\n')
		Screen.__init__(self, maxtime = 60 * 5, **args)
	def main(self):
		self.f.Print(0,0,str(self.t))
		for y, i in enumerate(self.textall):
			self.f.Print(5, y*32 + 480-self.t, i)