import ika

class ZoomImage:
    def __init__(self, *args):
        self.im = ika.Image(*args)
        self.width, self.height = self.im.width, self.im.height        
        self.Blit = lambda *args: self.im.Blit(*args)
        self.TintDistortBlit = lambda *args: ika.Video.TintDistortBlit(self.im, *args)
        self.TintBlit = lambda *args: ika.Video.TintBlit(self.im, *args)
        self.ScaleBlit = lambda *args: self.im.ScaleBlit(*args)
    def ZoomBlit(self, x, y, facing=1, tint=None):
        x2, y2 = x+self.width, y+self.height
        if tint is None:
            if facing == 1:
                self.im.Blit(x, y)
            else:
                self.im.DistortBlit((x2, y), (x, y), (x, y2), (x2, y2))
        else:
            if facing == 1:
                ika.Video.TintBlit(self.im, x, y, tint)
            else:
                ika.Video.TintDistortBlit(self.im, (x2, y, tint), (x, y, tint), (x, y2, tint), (x2, y2, tint))