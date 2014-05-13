from os import *
from ika import *
from zoomblit import ZoomImage
# giancarlo.montalbano@gmail.com
	
obj2ext = {'Image':'png', 'ZoomImage':'png', 'Canvas':'png', 'Sound':'ogg'}

def All(folder_name, obj='ZoomImage', cwd=getcwd()):
	global obj2ext
	fol = '%s/%ss/%s/' % (cwd, 'Image' if obj != 'Sound' else 'Sound', folder_name)
	object = eval(obj)
	fun = lambda i: len(i)> 3 and i[-3:].lower() == obj2ext[obj]
	return dict((i[:-4], object(fol+i)) for i in listdir(fol) if fun(i))
	
#def Cache(text):
#	
	
def FlipAll(folder_name, cwd=getcwd()):
	left, right = {}, {}
	cachefol = '%s/cache' % cwd
	fol = '%s/%s/' % (cachefol, folder_name)
	if folder_name not in listdir(cachefol):
		makedirs(fol)
	dire = listdir(fol)
	if len(dire):
		for k in listdir(fol):
			o = k[1:-4]
			left[o] = Image(fol+k)
			right[o] = Image('%s/Images/%s/%s' % (cwd, folder_name, k[1:]))
	else:
		orig = All(folder_name, obj = 'Canvas')
		for k, v in orig.iteritems():
			right[k] = Image(v)
			v.Mirror()
			left[k] = Image(v)
			v.Save(fol+'l'+k+'.png')
	return (right, left)

#def Cache(source, dest, sourcef, destf, manipf):
#	s = sourcef(source)
	
	
def Flip(dire, im, source=None, saveOriginal=True):
	canv = Canvas(dire+im) if source is None else source
	rc = Canvas(canv.width, canv.height)
	canv.Blit(rc, 0, 0); rc.Mirror()
	#if saveOriginal:
	#	canv.Save(dire+im)
	#rc.Save(dire+'l'+im)
	#im, rim = Image(canv), Image(rc)
	return (canv, rc)