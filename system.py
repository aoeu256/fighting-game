from screens import config
from sysobj import CollisionTester
import cPickle
import intro
try:
	import psyco; psyco.full() #@UnresolvedImport
except ImportError: pass
from ika import *
from xi import fps
#from cProfile import runctx
from os import getcwd, listdir, mkdir, path
cwd, f = getcwd(), Font('font.fnt') # ugly, butworks
from chars import genjuro, kyo, player #@UnusedImport
import load, cPickle
from screens import edit, select, title, vs, control, menu, story
#from threading import Thread, Lock
#import profile
import sysobj
from math import sqrt
from zoomblit import ZoomImage
import os
from time import time, strftime, localtime

clamp = lambda n, mn, mx: max(mn, min(n, mx))
# open

def reset_cache(): 
	global cwd	
	moddic = cPickle.load(file('%s/cache/mod' % cwd))
	def removeifexist(filename):
		if path.isfile(filename):
			os.remove(filename)
			print 'removing...', filename
	for char in listdir('%s/Images/characters' % cwd):
		for im in listdir('%s/Images/characters/%s' % (cwd, char)):			
			filename = '%s/Images/characters/%s/%s' % (cwd, char, im)
			tim = path.getmtime(filename)
			if tim != moddic.get(char+im, None):
				removeifexist('%s/cache/outline/%s/self%s' % (cwd, char, im[:-4]))
				removeifexist('%s/cache/outline/%s/hit%s' % (cwd, char, im[:-4]))
				moddic[char+im] = tim
		cPickle.dump(moddic, file('%s/cache/mod' % cwd, 'w'))
reset_cache()
#===============================================================================
# def Test():
#	'load two images then build a dict from colors A to colors B, then use the dict to make a colorized image'
#	img1 = Canvas('%s/Images/characters/li/w-00.png'%cwd)
#	img2 = Canvas('%s/Images/colorizer/li.png'%cwd)
#	img3 = Canvas('%s/Images/characters/li/w-01.png'%cwd)
#	dic = {}
#	for x in xrange(img1.width):
#		for y in xrange(img1.height):
#			dic[img1.GetPixel(x,y)] = img2.GetPixel(x,y)
#	for k, v in dic.iteritems():
#		try:
#			print '%d->%d' % (GetRGB(k), GetRGB(v))
#		except TypeError:
#			print '%d->%d' % (k, v)
#	for x in xrange(img3.width):		
#		for y in xrange(img3.height):
#			img3.SetPixel(x, y, dic[img3.GetPixel(x,y)])
#	img4 = Image(img3)
#	while True:
#		img4.Blit(0,0)
#		Video.ShowPage()
# Test()
#===============================================================================


def Blur(canv):
	for x in range(1,640-1):
		for y in range(1,480-1):
			g = canv.GetPixel(x, y)
			c = GetRGB(g)
			for p in [(x-1,y), (x+1, y), (x, y-1), (x, y+1)]:
				x1, y1 = p
				o = GetRGB(canv.GetPixel(x1, y1))
				canv.SetPixel(x1, y1, RGB((c[0]+o[0])/2, (c[1]+o[1])/2, (c[2]+o[2])/2))
	return Image(canv)

VLine = lambda x, y1, y2, c: Video.DrawLine(x, y1, x, y2, c)
HLine = lambda x1, y, x2, c: Video.DrawLine(x1, y, x2, y, c)

class MyFont:
	def __init__(self, name, area, debug = False):
		#Thread.__init__(self)
		self.name, self.area = name, area
		self.chars = ' !\"#$ &\'()^+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		self.letterspan = {} # The span of each individual letter in the picture
		self.spanname = name[:-4]+'span'
		self.done = False
		#self.start()
	#def run(self):
		imname = '%s/Images/system/fonts/%s' % (self.area.cwd, self.name)
		lastx = i = 0
		try:
			self.letterspan = self.area.load(self.spanname)
			self.pic = Image(imname)
		except IOError:
			print 'Making font' + imname
			self.pic = Canvas(imname)
			c = self.pic.GetPixel(0,0)
			for x in range(self.pic.width):
				if self.pic.GetPixel(x, 0) == c:
					self.letterspan[self.chars[i]] = (lastx, x)
					lastx = x
					i += 1
			area.save(self.spanname, self.letterspan)
			self.pic = Image(self.pic)
		self.h = self.pic.height
		self.done = True
	def Print(self, x, y, text, tint = None, debug = False):
		if self.done:
			curx = x
			for c in text:
				x1, x2 = self.letterspan[c]
				span = x2-x1
				Video.ClipBlit(self.pic, curx, y, x1, 0, span, self.h-1)
				curx += span
	def width(self, text):
		return sum(self.letterspan[i][1] - self.letterspan[i][0] for i in text)
	def CenterXPrint(self, y, text):
		if self.done:
			leng = self.width(text)
			self.Print(320-leng/2, y, text)
	def CenterPrint(self, text):
		self.CenterXPrint(240-self.h/2, text)

class Area:
	x = 255
	r, g, b = RGB(x,0,0), RGB(0,x,0), RGB(0,0,x)
	c, y, m = RGB(0,x,x), RGB(x,x,0), RGB(x,0,x)
	black, white = RGB(0,0,0), RGB(x,x,x)
	rainbow = [r,y,g,c,b,m]
	def __init__(self):
		global cwd, f
		SetCaption('Beast Genesis') #@UndefinedVariable
		self.f, self.cwd = f, cwd
		# Make the base cache folders if they don't exist		
		self.cachefol = '%s/cache/' % self.cwd
		self.fols = dict(
			imfol = '%s/Images/characters/' % self.cwd,
			outlinefol = '%s/cache/outline/' % self.cwd,
			reversefol = '%s/Images/cache/characters/' % self.cwd,
			hitfolcache = '%s/Images/cache/hitbox/' % self.cwd,
			hitfolsrc = '%s/Images/hitbox/' % self.cwd)
		for char in listdir(self.fols['imfol']): # Make dirs if they don't exist
			for fol in self.fols.values():
				if char not in listdir(fol):
					mkdir(fol+char)
		# Set the attributes for player 1 and 2 that are different
		# Initialize map stuff	
		self.maxt = 30*60
		self.bg = Image(getcwd()+'/images/bg/training.png')
		self.width, self.height =  1500, 900
		self.zoomx1, self.zoomy1, self.zoomx2, self.zoomy2 = 0, 0, 640, 480
		self.nrounds = 2
		self.jumpn = 0
		self.objects = []
		fontdir = listdir('%s/Images/system/fonts'%self.cwd)
		self.font = dict((i[:-4], MyFont(i,self)) for i in fontdir)
		self.combo = 0
		self.mode, self.modet = 'intro', 30
		self.winnar = ''
		self.strikim = load.All('strike', cwd=self.cwd)
		self.logoim = Image('%s/Images/system/title/metal-logo.png' % self.cwd)
		self.totalwins = 0
		self.roundn = lambda: self.p1.wins + self.p2.wins
		self.dp1, self.dp2 = player.DummyPlayer(self, 'p1'), player.DummyPlayer(self, 'p2')
		self.dp1.pname, self.dp2.pname = 'p1', 'p2'
		self.titlemode = ''
		self.title = title.Title(area=self)		
		self.pausemenu = menu.Menu(['RETURN', 'CONTROLS', 'MOVE LIST', 'CHARACTER', 'EXIT'], area=self)
		self.select = select.Select(self.dp1, self.dp2, area=self)
		self.done = False
		self.config = config.Config(area=self)

	def changehp(self, p, n):
		p.hp = max(p.hp+n, 0)
		p.hpdecr = max(p.hpdecr-n, 0)
	def changebar(self, p, n):
		p.bar = max(p.bar+n, 0)
		p.bardecr = max(p.bardecr-n, 0)
	def resetbattles(self, init=False): # Several rounds
		self.select.do()
		#self.font['menuwhite'].CenterPrint('LOADING...')
		#Video.ShowPage()
		samechar = self.dp1.name == self.dp2.name
		self.p1 = eval('%s.%s' % (self.dp1.name,self.dp1.name))(area=self, pname='p1', samechar=samechar)
		self.p2 = eval('%s.%s' % (self.dp2.name,self.dp2.name))(area=self, pname='p2', samechar=samechar)
		
		vs.Vs(self.p1, self.p2, area=self).do()
		
		self.p1.defaultFacing, self.p2.defaultFacing = 1, -1
		self.p1.barim, self.p2.barim = load.FlipAll('bars')
		self.p1.barx, self.p2.barx = 20, 360
		self.p1.bar1x, self.p2.bar1x = 33, 393
		self.p1.bar2x, self.p2.bar2x = 144, 392
		self.p1.combox, self.p2.combox = 20, 360
		self.p1.pname, self.p2.pname = 'p1', 'p2'
		self.p1.roundx, self.p2.roundx = 134, 510
		self.p1.wins, self.p2.wins = 0, 0
		self.p1.controls, self.p2.controls = self.dp1.controls, self.dp2.controls
		if init:
			self.p1.wins = self.p2.wins = 0
			self.winstreak = 0
			self.rwinner = None
		if self.rwinner is not None and self.rwinner.name == self.winnar:
			self.winstreak += 1
		else:
			self.winstreak = 0
			self.rwinner = self.p1 if self.p1.name == self.winnar else self.p2	
		self.resetbattle()

	def save(self, name, data): # Save system data
		outf = file(self.cachefol+name,'w')
		cPickle.dump(data, outf)
	def load(self, name):
		return cPickle.load(file(self.cachefol+name))		

	def resetbattle(self):
		self.t = self.maxt
		self.p1.x, self.p1.y, self.p2.x, self.p2.y = 650, 680, 850, 680
		self.p1.facing, self.p2.facing = 1, -1
		self.objects = []
		for p in [self.p1, self.p2]:
			p.changestate('stand')
			p.dx = p.dy = 0
			p.alreadyHit = False
			p.hp = 1000
			p.bar = 500
			p.movet = 0
			p.hpdecr = p.bardecr = 0
 			p.holdback = self.holddown = 0
 			p.combo = 0

	def titlemain(self):
		if self.titlemode == '':
			self.titlemode = self.title.do()
		elif self.titlemode in ('ARCADE', 'VS MODE', 'TRAINING'):
			self.resetbattles(init=True)
			fp = fps.FPSManager(60)
			while self.titlemode in ('ARCADE', 'VS MODE', 'TRAINING'):
				fp.render(self.main)
		elif self.titlemode == 'EXIT':
			self.done = True
		elif self.titlemode == 'OPTIONS':
			self.config.do()
	
	def main(self): # Called between ticks. State machine
		self.modet -= 1
		def onend(mode, t=30):
			if self.modet == 0:
				self.mode, self.modet = mode, t
				return True
			return False
		if self.mode == 'endround':
			self.tick('')
			if 60 < self.modet < 120:
				self.font['metal'].CenterXPrint(200, 'TIME UP' if self.t < 2 else 'KNOCK OUT')
			else:
				self.font['metal'].CenterXPrint(200, self.winnar)
			onend('intro', 4*30)
		elif self.mode == 'intro': # Intro
			if max(self.p1.wins, self.p2.wins) >= self.nrounds: # Dump back to character select.
				self.resetbattles()
			if intro.Get(self.p1.name, self.p2.name, self.modet) is None:
				self.maxmodet = 4*30
				self.p1.intro()
				self.p2.intro()				
			self.tick('')		
			if self.modet == 4*30 - 1:
				self.resetbattle()
			elif  2 * 30 < self.modet < 4*30:
				self.font['metal'].CenterXPrint(200, 'ROUND %d' % (self.roundn()+1))
			else:
				self.font['metal'].CenterXPrint(200, 'START')
			onend('control', 0)
		elif self.mode == 'super':
			self.tick('')
			self.superp.tintcolor = Area.rainbow[self.modet/2 % 6]
			t = self.modet*4 / 120.0
			Video.DrawEllipse(self.superp.x, self.superp.y, int(t*self.superp.w2()), int(t*self.superp.height()/2), RGB(255,255,255,128))
			if onend('control',0):
				self.superp.tintcolor = RGB(255,255,255,255)
		elif self.mode == 'hit':
			self.tick('control')
			Video.DrawRect(0,0,640,480,RGB(255,0,0,128+abs(5-self.modet)*8), 1)
			onend('control', 0)
		else:
			self.tick('control')
			if self.p1.hp < 1 or self.p2.hp < 1 or self.t == 0:
				self.p1.hp, self.p2.hp = max(0, self.p1.hp), max(0, self.p2.hp)
				if self.p1.hp < self.p2.hp:
					self.p2.wins += 1
					self.winnar = 'PLAYER 2 WINS'
				elif self.p2.hp < self.p1.hp:
					self.p1.wins += 1
					self.winnar = 'PLAYER 1 WINS'
				else:
					self.p1.wins += 1
					self.p2.wins += 1
					self.winnar = 'DRAW'
				self.mode, self.modet = 'endround', 2*60
		if Input.keyboard['F1'].Pressed():
			self.screenshot()
	def screenshot(self):
			screenshot = Video.GrabCanvas(0,0,640,480)
			n = 0
			for i in listdir(self.cwd):
				split = i.split('-')
				if split[0] == 'screenshot':
					n = max(int(split[1][:-4]), n)
			screenshot.Save('%s/screenshot-%02d.png' % (self.cwd, n+1))						
	def tick(self, mode = 'control'):
		#leastx = min(self.p1.bedge(), self.p2.bedge())
		clamp = lambda n, mn, mx: max(mn, min(n, mx))
		midx, midy = (self.p1.sedge() + self.p2.sedge())/2, (self.p1.y+self.p2.y-self.p1.sheight()-self.p2.sheight())/2
		midx2 = (self.p1.x+self.p2.x)/2
		self.zoomx1 = clamp(midx2-320, 0,self.width-640)
		self.zoomy1 = clamp(midy, 0, 900-480)
		self.zoomx2 = self.zoomx1 + 640
		self.zoomy2 = self.zoomy1 + 480
		#self.f.Print(300,0,'%3d %3d->%3d %3d midx=%3d dist=%3d' % (self.zoomx1, self.zoomy1, self.zoomx2, self.zoomy2, midx, abs(self.p2.x-self.p1.x)))			
		if mode == 'control':
			self.t -= 1
			for p, o in [(self.p1, self.p2), (self.p2, self.p1)]:		
				p.dx = clamp(p.dx, -p.maxspeed, p.maxspeed)
				p.x, p.y = p.x+p.dx, p.y+p.dy
				if p.y >= 680 and p.state[1] == '8':
					p.movet = 0 # Stops all air attacks...
				p.x, p.y = clamp(p.x,0,1499),clamp(p.y,0,680) # clamp to stage
				if p.y < 680:
					p.x = clamp(p.x, 1, 1498) # Additional clampage.
				if p.y == 680:
					p.dx = int(p.dx*0.8)
				if 1 < p.dx < -1:
					p.dx = 0
				if p.state == 'stand':
					p.dx = clamp(p.dx, -p.maxwalk, p.maxwalk)					
				p.x = clamp(p.x, self.zoomx1, self.zoomx1+640)
				if p.bar < 1000:
					self.changebar(p, sqrt(max(p.dx*p.facing,0))/2)		
			getpo = lambda cond:(self.p1, self.p2) if cond else (self.p2, self.p1)
			xcond = abs(self.p1.x-self.p2.x) < (self.p1.sw2()+self.p2.sw2())
			p, o = getpo(self.p1.y < self.p2.y)
			ycond = p.y <= o.y <= p.y + p.sheight()
			print '%d <= %d <= %d = %s' % (p.y, o.y, p.y+p.sheight()*3/4, ycond)  
			if 'thrown' not in [self.p1.state, self.p2.state] and xcond and ycond:		
				if self.p1.y == self.p2.y == 680 or 'airdash' in [self.p1.state, self.p2.state]:				 
					p, o = getpo(abs(self.p1.dx) >= abs(self.p2.dx))
					p.x = midx-p.sdedge()+(p.dx+o.dx)
					o.x = midx-o.sdedge()+(p.dx+o.dx)
					p.x, o.x = max(p.x, 0), max(o.x, 0)
					p, o = getpo(self.p1.x < self.p2.x)
					p.x = clamp(p.x, 0, self.width - p.sw2() - o.sw2() - 1)
					o.x = clamp(o.x, p.sw2()+o.sw2(), self.width - 1)
				elif 680 in [self.p1.y, self.p2.y]:
					p, o = getpo(self.p1.y > self.p2.y)
					if o.x > p.x: # Move ->
						o.x = p.x+o.sw2()+p.sw2()
					elif o.x < p.x: # Move <-
						o.x = p.x-o.sw2()-p.sw2()
		Video.ClipBlit(self.bg, 0, 0, self.zoomx1, 420 - self.zoomy1, 640, 480)
		
		for p, o in [(self.p1, self.p2), (self.p2, self.p1)]:
			if mode == 'control':
				if self.mode == 'buffer':
					p.checkattacks(o)
				else:
					p.tick(o)

			p.draw_shadow(p.x-self.zoomx1, p.y-self.zoomy1)

			
		for p in (a.p1, a.p2):
			p.draw(p.x-self.zoomx1, p.y-self.zoomy1)
		for i in self.objects:
			i.tick(self)
		self.objects = [i for i in self.objects if i.t > 0] # Delete thingies whoes timers expired
		
		#self.zoom(midx)
						
		if Input.keyboard['3'].Pressed():edit.Edit(self.p1, area=self).do()
		if Input.keyboard['4'].Pressed():edit.Edit(self.p2, area=self).do()
		
		#self.f.Print(200, 200, 'midx=%d, zoom=%d' % (midx-self.zoomx1, xdisp)) # As midx increases, zoom left
		for p, o in [(self.p1, self.p2), (self.p2, self.p1)]:
			pb, hit = p.selfbox1(), o.hitbox1()
			px, py = p.x+p.cx(), p.y+p.cy()
			ox, oy = o.x+o.cx(), o.y+o.cy()

			if hit is not None:
				oxp, oyp = o.cat().addxy(o)
				result = self.collide((p, p.width(), pb, px, py), (o, o.cat().width(o), hit, ox+oxp, oy+oyp))
				if result is not None:
					x, y = result
					if self.resolveHit(o.cat(), result, p, o):
						name = ''.join([i for i in 'wms' if i in o.state])
						dic = {'w':4, 'm':5, 's':7}
						frames = dic[name]
						self.objects.append(sysobj.LightStrike(self, x, y, p, o, 10, 'block-'+name, frames))
			
			p.hpdecr = max(0, p.hpdecr-max(p.hpdecr/64, 1))
			p.bardecr = max(0, p.bardecr-max(p.bardecr/64, 1))
			
			f = p.defaultFacing
			x1 = 30
			lifebar, guardbar = p.barim['lifebar'], p.barim['guard-bar']
			p.barim['top-bar'].Blit(p.barx, x1)

			MaxHP = MaxBar = 1000
			hpn, barn = 217*p.hp/MaxHP, 107*p.bar/MaxBar
			hpdn, bardn = 217*(p.hpdecr)/MaxHP, 107*(p.bardecr)/MaxBar
			if f == -1:
				Video.ClipBlit(lifebar, p.bar1x, 34, 0, 0, hpn, 9)
				Video.ClipBlit(guardbar, p.bar2x, 49, 0, 0, barn, 3)
			else:
				lo, lg = 217-hpn, 107-barn
				Video.ClipBlit(lifebar, p.bar1x+lo, 34, lo, 0, hpn, 9)
				Video.ClipBlit(guardbar, p.bar2x+lg, 49, lg, 0, barn, 3)
			if p.hpdecr > 0:
				if f == 1:
					s1, e1 = p.bar1x+217-hpn-hpdn, p.bar1x+216-hpn
				else:
					s1, e1 = p.bar1x+hpn, p.bar1x+hpn+hpdn
				Video.DrawRect(s1, 34, e1, 42, RGB(255,0,0,128), 1)
			if p.bardecr > 0:
				if f == 1:
					s2, e2 = p.bar2x+107-barn-bardn, p.bar2x+106-barn
				else:
					s2, e2 = p.bar2x+barn, p.bar2x+bardn+barn
				Video.DrawRect(s2, 49, e2, 52, RGB(128,128,128,128), 1)				
			self.f.Print(p.barx+50, 35, '%s:%d'% (p.name, p.hp))			
			self.f.Print(p.barx-20, 8, '%3d+%3d,%3d+%3d %2d %-8s %-8s' % (p.x,p.dx,p.y,p.dy,p.movet,p.state,p.drawstate()))
			self.f.Print(p.barx-20, 16,'%-5s %-6s %2d %3d %3d %3d' % (p.alreadyHit, p.next, p.facing, p.holdback, p.holddown, p.holdt))
			for i in range(self.nrounds):
					Video.DrawEllipse(p.roundx+10*-p.defaultFacing*i, 54, 4, 4, RGB(0,255,255),1 if p.wins>i else 0)
			if p.combo > 0:
				self.font['metal'].Print(p.combox, 230, 'COMBO: %2d'% (p.combo+1))
			if p.start.Pressed():
				grab = Video.GrabImage(0,0,640,480)
				choice = self.pausemenu.do(p, img=grab)
				if choice == 'EXIT':
					self.titlemode = ''
				elif choice == 'CHARACTER':
					self.resetbattles()
				elif choice == 'MOVE LIST':
					menu.CommandList(p, area=self).do(img=grab)
				elif choice == 'CONTROLS':
					p.controls.do()
			if p.movet > 0 and self.mode == 'hit': # Pushing on attacks; o is attacker
				if (o.facing == 1 and p.x >= self.width-4) or (o.facing == -1 and p.x <= 3):
					d = clamp(p.x, 0, self.width-1)
					o.x -= max(3, abs(p.x-d))*o.facing
					p.x = d
				else:
					p.x += 3*o.facing

		self.font['metal'].Print(305, 30, '%02d'%(self.t/60))
		self.f.Print(0, 0, '%s%d' % (self.mode, self.modet))

	def zoom(self, midx):		
		#myimg = Video.GrabImage(0,0,640,480)
		myimg = GetScreenImage()
		zoom = (640 - max(abs(self.p1.x - self.p2.x), abs(self.p1.y - self.p2.y)))/8		
		xdisp = (320 - (midx - self.zoomx1))*zoom/300
		#xdisp = zoom+(320-(midx-self.zoomx1))/320
		x1, y1 = -zoom + xdisp, -zoom*7/4
		x2, y2 = zoom+640 + xdisp, 480
		myimg.DistortBlit((x1, y1), (x2, y1), (x2, y2), (x1, y2))

	def resolveHit(self, at, result, p, o, backPush = True):		
		if not o.alreadyHit or o.movet in at.hitlist:
			x, y = result
			o.alreadyHit = True
			if p.state in ['hit', 'throwstun']:
				o.combo += 1
			p.dx, p.dy = 0, 0
			p.state, p.movet = ('hit', at.hit) if p.state != 'block' else ('ghit', at.ghit)
			if p.state == 'hit':
				self.changehp(p, -at.dmg)						
			p.backPush = backPush
			self.mode = 'hit'; self.modet = 10
		else:
			return False
		return True
	def collide(self, ptup, otup):		
		def log(x, y, t):			
			self.f.Print(x, y, t)
			return x + y
		(p, pwide, plines, px, py) = ptup
		(o, owide, olines, ox, oy) = otup
		#tup = [ptup, otup]
		px -= self.zoomx1; py -= self.zoomy1
		ox -= self.zoomx1; oy -= self.zoomy1
		sumx, sumy = [], []
		invo = lambda x: x if o.facing==1 else owide-x
		invp = lambda x: x if p.facing==1 else pwide-x
		for y, (hx1, hx2) in olines[0].iteritems():
			try:
				sx1, sx2 = plines[0][y+(oy-py)]
				hmin, hmax = invo(hx1)+ox, invo(hx2)+ox
				smin, smax = invp(sx1)+px, invp(sx2)+px
				
				if hmin > hmax: hmin, hmax = hmax, hmin
				if smin > smax: smin, smax = smax, smin
				
				HLine(hmin, oy+y, hmax, RGB(255,0,0,128))
				HLine(smin, oy+y, smax, RGB(0,0,255,128))
	
				if smin<hmax and smax>hmin:
					sumx += [smin, smax]
			except KeyError: pass

		for x, (hy1, hy2) in olines[1].iteritems():
			try:
				hmin, hmax = hy1+oy, hy2+oy
				var = invp(invo(x))+(ox-px)*p.facing
				# nancy = 1, li = -1
				# nancy  = 1, li = -1				
				#VLine(invo(x)+ox, hmin, hmax, RGB(255,0,0,128))
				#VLine(invo(x)+ox, smin, smax, RGB(0,0,255,128))
				#f.Print(100, 100+x*16, 'ox=%d, px=%d, d=%d, invo=%d, invp=%d, var=%d ' % (ox, px, ox-px, invo(x), invp(invo(x)), var)) 
				sy1, sy2 = plines[1][var]
				smin, smax = sy1+py, sy2+py
				
				if smin<hmax and smax>hmin:
					sumy += [smin, smax]
			except KeyError: pass
		lx, ly = len(sumx), len(sumy)
		return None if 0 in (lx, ly) else (sum(sumx)/lx, sum(sumy)/ly)
	def dosuper(self, p):
		self.mode = 'super'
		self.modet = 1*60
		self.superp = p
	def do(self):
		self.done = False
		while not self.done:
			Input.Update()
			self.titlemain()
a = Area()
a.do()
#runctx('a.do()', globals(), locals())