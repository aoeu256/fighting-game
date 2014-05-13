from ika import *
from screen import Screen

class Config(Screen):
    def __init__(self, **args):
        self.choices = ['RETURN', 'P1 CONTROLS', 'P2 CONTROLS', 'MUSIC VOLUME', 'SFX VOLUME', 'AI DIFFICULTY', 
                        'SHOW HITBOXES', 'NUMBER OF ROUNDS', 'TIMER']
        self.extra = {}
        self.extra['MUSIC VOLUME'] = self.extra['SFX VOLUME'] = [0, 25, 50, 75 ,100]
        self.extra['NUMBER OF ROUNDS'] = [1, 3, 5]
        self.extra['SHOW HITBOXES'] = ['YES', 'NO']
        self.extra['AI DIFFICULTY'] = ['GIANCARLO', 'VERY EASY', 'EASY', 'NORMAL', 'HARD', 'VERY HARD']
        self.extra['TIMER'] = [20, 30, 45, 99]
        self.config = {}
        self.config['MUSIC VOLUME'] = 2
        self.config['SHOW HITBOXES'] = 0
        self.config['SFX VOLUME'] = 2
        self.config['NUMBER OF ROUNDS'] = 2
        self.config['AI DIFFICULTY'] = 3
        self.config['TIMER'] = 2
        self.volume = 50
        self.nrounds = 2
        keycond = lambda: not self.done
        Screen.__init__(self, 'system/title', keycond=keycond, **args)
        self.f = self.area.font['metal']
        self.incx = 0
        self.x, self.y = 8, 8
        self.choice = 0
        self.setting = lambda configname: self.extra[configname][self.config[configname]]
    def main(self):
        #raise 'wtf'
        coi = self.choices[self.choice]
        self.scrollbg()
        Video.DrawRect(0,0,640,480,RGB(0,255,0,128))
        for y, i in enumerate(self.choices):
            f = self.area.font['menuwhite'] if self.choice == y else self.area.font['menugray']
            if i not in ('RETURN', 'P1 CONTROLS', 'P2 CONTROLS'):
                print i, self.config[i], self.extra[i]
            text = '%s %-8s' % (i, self.setting(i) if i in self.config else '')
            f.CenterXPrint(self.y + y*f.h, text)
        if self.up(): self.choice = (self.choice-1)%len(self.choices)
        if self.down(): self.choice = (self.choice+1)%len(self.choices)
        if self.right(): self.config[coi] = (self.config[coi]+1)%len(self.extra[coi])
        if self.left(): self.config[coi] = (self.config[coi]-1)%len(self.extra[coi])
    def do(self):
        self.done = False
        Screen.do(self)
        areavars2conf = {'nrounds':'NUMBER OF ROUNDS', 'maxt':'TIMER', 'ailevel':'AI DIFFICULTY', 
                    'musicvol':'MUSIC VOLUME', 'sfxvol':'SFX VOLUME'}
        for k, v in areavars2conf:
            self.area.__dict__[k] = self.setting(v)
#===============================================================================
#        self.area.nrounds = self.setting('NUMBER OF ROUNDS')
#        self.maxt = self.setting('TIMER')
#        self.ailevel = self.setting('AI DIFFICULTY')
#        self.showhitbox = self.setting('SHOW HITBOXES')
#        self.musicvol = self.setting('MUSIC VOLUME')
#        self.sfxvol =  self.setting('SFX VOLUME')
#===============================================================================