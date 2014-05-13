from ika import *

def Outline(pic):
	s = set()
	Width, Height = pic.width, pic.height
	for x in xrange(1,Width):
		for y in xrange(1,Height):
			o, a, b = (x,y), (x-1,y), (x,y-1)
			to, ta, tb = tuple(GetRGB(pic.GetPixel(j,k))[3]<32 for j,k in [o,a,b])
			if to and (not ta or not tb):	s.add(o)
			elif not to and tb:				s.add(b)
			elif not to and ta:				s.add(a)
			elif not tb and y == 1:			s.add(b)
			elif not to and y == Height-1:	s.add(o)
			elif not ta and x == 1:			s.add(a)
			elif not to and x == Width-1:	s.add(o)
	return s

def HLines(pic): # Go through each y, then go through each x finding outline points
	min, max = {}, {}
	Width, Height = pic.width, pic.height
	for y in xrange(Height):
		def find_extreme(dic, start, end, step):
			for x in xrange(start, end, step):
				o, a = (x, y), (x-step, y)
				transp = lambda (x,y): GetRGB(pic.GetPixel(x,y))[3]<16 
				to, ta  = transp(o), transp(a)
				if not to and ta or (not ta and x == start):
					dic[y] = x
					break
		find_extreme(min, 1, Width, 1)
		find_extreme(max, Width-2, -1, -1)
	return dict((k,(min[k],max[k])) for k in min)

def VLines(pic): # Go through each x, then go through each y finding outline points	
	min, max = {}, {}
	Width, Height = pic.width, pic.height
	for x in xrange(Width):
		def find_extreme(dic, start, end, step):
			for y in xrange(start, end, step):
				o, a = (x, y), (x, y-step)
				transp = lambda (x,y): GetRGB(pic.GetPixel(x,y))[3]<16 
				to, ta  = transp(o), transp(a)
				if not to and ta or (not ta and y==start):
					dic[x] = y
					break
		find_extreme(min, 1, Height, 1)
		find_extreme(max, Height-2, -1, -1)
	return dict((k,(min[k],max[k])) for k in min)

def Lines(pic):
	return (HLines(pic), VLines(pic))