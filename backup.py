# 			def cache(dire, im, source=None, saveOriginal=True):
# 				canv = Canvas(dire+im) if source is None else source
# 				rc = Canvas(canv.width, canv.height)
# 				canv.Blit(rc, 0, 0); rc.Mirror()
# 				if saveOriginal:
# 					canv.Save(dire+im)
# 				rc.Save(dire+'l'+im)
# 				return (canv, rc)
# 			def toSilho(pic, col):
# 				for x in xrange(pic.width):
# 					for y in xrange(pic.height):
# 						if GetRGB(pic.GetPixel(x, y))[3] != 0:
# 							pic.SetPixel(x, y, col)
# 						return pic
# 			for im in listdir(fol):
# 				k = im[:-4]
# 				try: # Check for silhoutte
# 					p.silho[1][k], p.silho[-1][k] = Canvas(cachefol+p.pname+im), Canvas(cachefol+'l'+p.pname+im)
# 					loadpics(im)
# 				except (RuntimeError, IOError): # If not make the silhoutte while making a cache
# 					if p.name not in listdir(imfol+'cache/characters'):
# 						mkdir(cachefol)
# 					pic = toSilho(cache(cachefol, im, source=Canvas(fol+im), saveOriginal=False)[0], p.silhoc)
# 					try:
# 						toSilho(Canvas(hitfolsrc+im), p.hitboxc).Blit(pic, 0, 0, Matte)
# 					except IOError:
# 						pass
# 					p.silho[1][k], p.silho[-1][k] = cache(cachefol, p.pname+im, source=pic)
# 					loadpics(im)
# 		try:
# 			for x in xrange(640/48):
# 				for y in xrange(480/48):
# 					c = a.silho.GetPixel(x*48, y*48)
# 					if c == RGB(128,256,128) or a.p2.win and a.p1.win:
# 						raise 'break'
# 					elif c == RGB(0,256,128):
# 						a.p2.win = True
# 					elif c == RGB(128,128,128):
# 						a.p1.win = True
# 		except 'break':
# 			pass
		#	a.p1.barx, a.p2.barx = 20, 360