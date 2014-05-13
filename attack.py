from ika import *
from sysobj import Fireball
from math import cos, pi
def Spawn(p, o, a, name, obj=Fireball, **args): #@UnusedVariable
	'Use with func property in attacks'
	a.objects.append(obj(a, p.x, p.y, p, o, name=name, **args))
def FarRightTeleport(p, o, a): #@UnusedVariable
	p.x = o.x + 640
def FarLeftTeleport(p, o, a): #@UnusedVariable
	p.x = o.x - 640
def BehindTeleport(p, o, a): # Work in Progress @UnusedVariable
	p.x = o.x + (p.w2()+o.w2())*-o.facing
	
class At:
	def __init__(self, name, alen=10, dmg=10, hit=10, ghit=10, push=(0,0), move=(0,0), 
			 framelist=None, hitlist=[], reverse=False, cycle=1, cycleframe=3,
			 super=False, barcost=0, funcs={}, imgname = None, overhead = False,
			 holdback=0, holddown=0):
		self.funcs = funcs # self.funcs[p.movet](p, o, area)
		self.imgname = name if imgname is None else imgname
		self.reverse = reverse
		self.name, self.alen = name, alen
		self.push,self.move = push, move
		self.ghit,self.hit = ghit, hit
		self.dmg = dmg
		self.framelist = framelist
		self.hitlist = hitlist[:]
		self.barcost,self.super = barcost, super
		self.cycle,self.cycleframe = cycle, cycleframe
		self.addxy = lambda p: (0,0) #@UnusedVariable
		self.overhead = overhead
		self.holdback, self.holddown = holdback, holddown
		self.width = lambda p: p.width()
	def hitbox(self, p):
		return p.hitbox.get(p.drawstate(), None)
	def draw(self, x, y, p): pass
	
	def loadframes(self, p):
		self.framelist = range(self.flen)
		if self.cycle == 1:
			self.framelist += range(self.flen, -1, -1)				
		else:
			for i in range(self.cycle-1): #@UnusedVariable
				self.framelist += range(self.flen,self.cycleframe-1, -1)					
				self.framelist += range(self.cycleframe,self.flen)
			self.framelist += range(self.flen, -1, -1)
		
	def load(self, p):
		self.flen = p.framelen[self.imgname]
		if self.framelist is None:
			self.loadframes(p)
		self.listlen = len(self.framelist)-1

		if self.hitlist == [] and self.cycle > 1:
			for i in range(1, self.alen):
				if self.frame(i-1) != self.frame(i) == self.flen:
					self.hitlist.append(i)
		if self.reverse: self.framelist.reverse()
	def frame(self, movet):
		t = movet*self.listlen/self.alen
		return self.framelist[-t-1]			
#	def refresh(self, p):
#		return p.refresh
	def drawstate(self, p):
		return '%s-%02d' % (self.imgname, self.frame(p.movet))		
	
class Pre(At):
	pass
#	def drawstate(self, p):
		#t = (p.movet*self.flen*2/self.alen)
		#m =self.flen - abs(self.flen-t)
#		t = p.movet*self.listlen/self.alen
#		return '%s-%02d' % (self.imgname,self.framelist[t])

class Extend(At): # Attacks that extend*
	'Attacks that consist of a predrawn self part, an extension image, and an end.'
	def __init__(self, y, y2, rang=5, startup=0, **args):
		At.__init__(self, **args)
		self.rang = rang
		self.code = lambda t: (0, 0) # Path where atim will be @UnusedVariable
		self.y,self.y2 = y, y2
		#self.leng = lambda p:
		self.extw = lambda p: -p.pic[self.imgname+'ext'].width		
		self.extcx = lambda p: 0 if p.facing == 1 else -self.extw(p)
		self.end = lambda p: p.w2()*p.facing
		self.hitbox = lambda p: p.selfbox[self.name+'end']
		self.addxy = lambda p: (self.endx(p)-self.p.cx(), self.y2)
		self.startup = startup
		self.ralen = lambda: self.alen - self.startup  
		self.rt = lambda p: p.movet - self.startup
		self.width = lambda p: p.pic[self.imgname+'end'].width
		#Sself.cx = 
	def leng(self, p):
		t = (self.ralen() - self.rt(p))*pi / self.ralen()
		return int((1-abs(cos(t)))**2*self.rang*p.facing/self.extw(p)*self.extw(p))
	def endx(self, p):
		endpic = p.pic[self.imgname+'end']
		cx = 0 if p.facing == 1 else -endpic.width
		return cx+self.end(p)+self.leng(p)
	def draw(self, x, y, p):
		endpic = p.pic[self.imgname+'end']
		ext = p.pic[self.imgname+'ext']
		extcx = 0 if p.facing == 1 else self.extw(p)
		if p.movet<self.alen-self.startup:
			endpic.Blit(x+self.endx(p), y+self.y2)
			for i in range(0,abs(self.leng(p)),ext.width):
				ext.Blit(x+self.end(p)+i*p.facing+extcx, y+self.y)

class Air(At):
	def __init__(self, midleng=20, **args):
		At.__init__(self, **args)
		self.midleng = midleng		
	def loadframes(self, p):
		self.framelist = range(self.flen)
		self.framelist = [self.flen for i in range(self.midleng)] #@UnusedVariable
		self.framelist += range(self.flen, -1, -1)				