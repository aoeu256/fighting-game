from __future__ import with_statement
import wx, os, cPickle

rbId, playId, exitId, p1Id, p2Id = tuple(range(10,15))
runIka = False

##WXK_BACK 	WXK_EXECUTE 	WXK_F1 	WXK_NUMPAD_SPACE 	WXK_WINDOWS_LEFT
##WXK_TAB 	WXK_SNAPSHOT 	WXK_F2 	WXK_NUMPAD_TAB 	WXK_WINDOWS_RIGHT
##WXK_RETURN 	WXK_INSERT 	WXK_F3 	WXK_NUMPAD_ENTER 	WXK_WINDOWS_MENU
##WXK_ESCAPE 	WXK_HELP 	WXK_F4 	WXK_NUMPAD_F1 	WXK_SPECIAL1
##WXK_SPACE 	WXK_NUMPAD0 	WXK_F5 	WXK_NUMPAD_F2 	WXK_SPECIAL2
##WXK_DELETE 	WXK_NUMPAD1 	WXK_F6 	WXK_NUMPAD_F3 	WXK_SPECIAL3
##WXK_LBUTTON 	WXK_NUMPAD2 	WXK_F7 	WXK_NUMPAD_F4 	WXK_SPECIAL4
##WXK_RBUTTON 	WXK_NUMPAD3 	WXK_F8 	WXK_NUMPAD_HOME 	WXK_SPECIAL5
##WXK_CANCEL 	WXK_NUMPAD4 	WXK_F9 	WXK_NUMPAD_LEFT 	WXK_SPECIAL6
##WXK_MBUTTON 	WXK_NUMPAD5 	WXK_F10 	WXK_NUMPAD_UP 	WXK_SPECIAL7
##WXK_CLEAR 	WXK_NUMPAD6 	WXK_F11 	WXK_NUMPAD_RIGHT 	WXK_SPECIAL8
##WXK_SHIFT 	WXK_NUMPAD7 	WXK_F12 	WXK_NUMPAD_DOWN 	WXK_SPECIAL9
##WXK_ALT 	WXK_NUMPAD8 	WXK_F13 	WXK_NUMPAD_PRIOR 	WXK_SPECIAL10
##WXK_CONTROL 	WXK_NUMPAD9 	WXK_F14 	WXK_NUMPAD_PAGEUP 	WXK_SPECIAL11
##WXK_MENU 	WXK_MULTIPLY 	WXK_F15 	WXK_NUMPAD_NEXT 	WXK_SPECIAL12
##WXK_PAUSE 	WXK_ADD 	WXK_F16 	WXK_NUMPAD_PAGEDOWN 	WXK_SPECIAL13
##WXK_CAPITAL 	WXK_SEPARATOR 	WXK_F17 	WXK_NUMPAD_END 	WXK_SPECIAL14
##WXK_PRIOR 	WXK_SUBTRACT 	WXK_F18 	WXK_NUMPAD_BEGIN 	WXK_SPECIAL15
##WXK_NEXT 	WXK_DECIMAL 	WXK_F19 	WXK_NUMPAD_INSERT 	WXK_SPECIAL16
##WXK_END 	WXK_DIVIDE 	WXK_F20 	WXK_NUMPAD_DELETE 	WXK_SPECIAL17
##WXK_HOME 	WXK_NUMLOCK 	WXK_F21 	WXK_NUMPAD_EQUAL 	WXK_SPECIAL18
##WXK_LEFT 	WXK_SCROLL 	WXK_F22 	WXK_NUMPAD_MULTIPLY 	WXK_SPECIAL19
##WXK_UP 	WXK_PAGEUP 	WXK_F23 	WXK_NUMPAD_ADD 	WXK_SPECIAL20
##WXK_RIGHT 	WXK_PAGEDOWN 	WXK_F24 	WXK_NUMPAD_SEPARATOR 	 
##WXK_DOWN 	  	  	WXK_NUMPAD_SUBTRACT 	 
##WXK_SELECT 	  	  	WXK_NUMPAD_DECIMAL 	 
##WXK_PRINT 	  	  	WXK_NUMPAD_DIVIDE
#keys = ['wx.WXK_BACK', 'wx.WXK_EXECUTE', 'wx.WXK_F1', 'wx.WXK_NUMPAD_SPACE', 'wx.WXK_WINDOWS_LEFT', 'wx.WXK_TAB', 'wx.WXK_SNAPSHOT', 'wx.WXK_F2', 'wx.WXK_NUMPAD_TAB', 'wx.WXK_WINDOWS_RIGHT', 'wx.WXK_RETURN', 'wx.WXK_INSERT', 'wx.WXK_F3', 'wx.WXK_NUMPAD_ENTER', 'wx.WXK_WINDOWS_MENU', 'wx.WXK_ESCAPE', 'wx.WXK_HELP', 'wx.WXK_F4', 'wx.WXK_NUMPAD_F1', 'wx.WXK_SPECIAL1', 'wx.WXK_SPACE', 'wx.WXK_NUMPAD0', 'wx.WXK_F5', 'wx.WXK_NUMPAD_F2', 'wx.WXK_SPECIAL2', 'wx.WXK_DELETE', 'wx.WXK_NUMPAD1', 'wx.WXK_F6', 'wx.WXK_NUMPAD_F3', 'wx.WXK_SPECIAL3', 'wx.WXK_LBUTTON', 'wx.WXK_NUMPAD2', 'wx.WXK_F7', 'wx.WXK_NUMPAD_F4', 'wx.WXK_SPECIAL4', 'wx.WXK_RBUTTON', 'wx.WXK_NUMPAD3', 'wx.WXK_F8', 'wx.WXK_NUMPAD_HOME', 'wx.WXK_SPECIAL5', 'wx.WXK_CANCEL', 'wx.WXK_NUMPAD4', 'wx.WXK_F9', 'wx.WXK_NUMPAD_LEFT', 'wx.WXK_SPECIAL6', 'wx.WXK_MBUTTON', 'wx.WXK_NUMPAD5', 'wx.WXK_F10', 'wx.WXK_NUMPAD_UP', 'wx.WXK_SPECIAL7', 'wx.WXK_CLEAR', 'wx.WXK_NUMPAD6', 'wx.WXK_F11', 'wx.WXK_NUMPAD_RIGHT', 'wx.WXK_SPECIAL8', 'wx.WXK_SHIFT', 'wx.WXK_NUMPAD7', 'wx.WXK_F12', 'wx.WXK_NUMPAD_DOWN', 'wx.WXK_SPECIAL9', 'wx.WXK_ALT', 'wx.WXK_NUMPAD8', 'wx.WXK_F13', 'wx.WXK_NUMPAD_PRIOR', 'wx.WXK_SPECIAL10', 'wx.WXK_CONTROL', 'wx.WXK_NUMPAD9', 'wx.WXK_F14', 'wx.WXK_NUMPAD_PAGEUP', 'wx.WXK_SPECIAL11', 'wx.WXK_MENU', 'wx.WXK_MULTIPLY', 'wx.WXK_F15', 'wx.WXK_NUMPAD_NEXT', 'wx.WXK_SPECIAL12', 'wx.WXK_PAUSE', 'wx.WXK_ADD', 'wx.WXK_F16', 'wx.WXK_NUMPAD_PAGEDOWN', 'wx.WXK_SPECIAL13', 'wx.WXK_CAPITAL', 'wx.WXK_SEPARATOR', 'wx.WXK_F17', 'wx.WXK_NUMPAD_END', 'wx.WXK_SPECIAL14', 'wx.WXK_PRIOR', 'wx.WXK_SUBTRACT', 'wx.WXK_F18', 'wx.WXK_NUMPAD_BEGIN', 'wx.WXK_SPECIAL15', 'wx.WXK_NEXT', 'wx.WXK_DECIMAL', 'wx.WXK_F19', 'wx.WXK_NUMPAD_INSERT', 'wx.WXK_SPECIAL16', 'wx.WXK_END', 'wx.WXK_DIVIDE', 'wx.WXK_F20', 'wx.WXK_NUMPAD_DELETE', 'wx.WXK_SPECIAL17', 'wx.WXK_HOME', 'wx.WXK_NUMLOCK', 'wx.WXK_F21', 'wx.WXK_NUMPAD_EQUAL', 'wx.WXK_SPECIAL18', 'wx.WXK_LEFT', 'wx.WXK_SCROLL', 'wx.WXK_F22', 'wx.WXK_NUMPAD_MULTIPLY', 'wx.WXK_SPECIAL19', 'wx.WXK_UP', 'wx.WXK_PAGEUP', 'wx.WXK_F23', 'wx.WXK_NUMPAD_ADD', 'wx.WXK_SPECIAL20', 'wx.WXK_RIGHT', 'wx.WXK_PAGEDOWN', 'wx.WXK_F24', 'wx.WXK_NUMPAD_SEPARATOR', 'wx.WXK_DOWN', 'wx.WXK_NUMPAD_SUBTRACT', 'wx.WXK_SELECT', 'wx.WXK_NUMPAD_DECIMAL', 'wx.WXK_PRINT', 'wx.WXK_NUMPAD_DIVIDE']

keyId2Name = {8: 'BACK', 9: 'TAB', 13: 'RETURN', 27: 'ESCAPE', 32: 'SPACE', 127: 'DELETE', 193: 'SPECIAL1', 194: 'SPECIAL2', 195: 'SPECIAL3', 196: 'SPECIAL4', 197: 'SPECIAL5', 198: 'SPECIAL6', 199: 'SPECIAL7', 200: 'SPECIAL8', 201: 'SPECIAL9', 202: 'SPECIAL10', 203: 'SPECIAL11', 204: 'SPECIAL12', 205: 'SPECIAL13', 206: 'SPECIAL14', 207: 'SPECIAL15', 208: 'SPECIAL16', 209: 'SPECIAL17', 210: 'SPECIAL18', 211: 'SPECIAL19', 212: 'SPECIAL20', 301: 'LBUTTON', 302: 'RBUTTON', 303: 'CANCEL', 304: 'MBUTTON', 305: 'CLEAR', 306: 'SHIFT', 307: 'ALT', 308: 'CONTROL', 309: 'MENU', 310: 'PAUSE', 311: 'CAPITAL', 312: 'END', 313: 'HOME', 314: 'LEFT', 315: 'UP', 316: 'RIGHT', 317: 'DOWN', 318: 'SELECT', 319: 'PRINT', 320: 'EXECUTE', 321: 'SNAPSHOT', 322: 'INSERT', 323: 'HELP', 324: 'NUMPAD0', 325: 'NUMPAD1', 326: 'NUMPAD2', 327: 'NUMPAD3', 328: 'NUMPAD4', 329: 'NUMPAD5', 330: 'NUMPAD6', 331: 'NUMPAD7', 332: 'NUMPAD8', 333: 'NUMPAD9', 334: 'MULTIPLY', 335: 'ADD', 336: 'SEPARATOR', 337: 'SUBTRACT', 338: 'DECIMAL', 339: 'DIVIDE', 340: 'F1', 341: 'F2', 342: 'F3', 343: 'F4', 344: 'F5', 345: 'F6', 346: 'F7', 347: 'F8', 348: 'F9', 349: 'F10', 350: 'F11', 351: 'F12', 352: 'F13', 353: 'F14', 354: 'F15', 355: 'F16', 356: 'F17', 357: 'F18', 358: 'F19', 359: 'F20', 360: 'F21', 361: 'F22', 362: 'F23', 363: 'F24', 364: 'NUMLOCK', 365: 'SCROLL', 366: 'PAGEUP', 367: 'PAGEDOWN', 368: 'NUMPAD_SPACE', 369: 'NUMPAD_TAB', 370: 'NUMPAD_ENTER', 371: 'NUMPAD_F1', 372: 'NUMPAD_F2', 373: 'NUMPAD_F3', 374: 'NUMPAD_F4', 375: 'NUMPAD_HOME', 376: 'NUMPAD_LEFT', 377: 'NUMPAD_UP', 378: 'NUMPAD_RIGHT', 379: 'NUMPAD_DOWN', 380: 'NUMPAD_PAGEUP', 381: 'NUMPAD_PAGEDOWN', 382: 'NUMPAD_END', 383: 'NUMPAD_BEGIN', 384: 'NUMPAD_INSERT', 385: 'NUMPAD_DELETE', 386: 'NUMPAD_EQUAL', 387: 'NUMPAD_MULTIPLY', 388: 'NUMPAD_ADD', 389: 'NUMPAD_SEPARATOR', 390: 'NUMPAD_SUBTRACT', 391: 'NUMPAD_DECIMAL', 392: 'NUMPAD_DIVIDE', 393: 'WINDOWS_LEFT', 394: 'WINDOWS_RIGHT', 395: 'WINDOWS_MENU'}

class DemoPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        self.parent = parent  # Sometimes one can use inline Comments
        rb = wx.RadioBox(self, rbId, "Screen mode", wx.DefaultPosition, wx.DefaultSize, ['Window', 'Fullscreen'])
        okcancel = wx.BoxSizer(wx.HORIZONTAL)
        b1 = wx.Button(self, playId, label='Play')
        b2 = wx.Button(self, exitId, label='Exit')
        for b in (b1, b2):
            okcancel.Add(b, 0, wx.ALIGN_RIGHT|wx.ALL, 5)        
        controlbox = wx.StaticBox(self, -1, label='Configure Controls')
        controls = wx.StaticBoxSizer(controlbox, wx.HORIZONTAL)
        #controls = wx.BoxSizer(wx.HORIZONTAL)
        p1 = wx.Button(self, p1Id, label="Player 1")
        p2 = wx.Button(self, p2Id, label="Player 2")
        for p in (p1, p2):
            controls.Add(p, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        self.rb = rb
        #b2.Bind(wx.EVT_BUTTON, self.OnExit)
        #sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)
        #NothingBtn.Bind(wx.EVT_BUTTON, self.DoNothing )

        sizer = wx.BoxSizer(wx.VERTICAL)
        for b in (rb, controls, line, okcancel):
            sizer.Add(b, 0, wx.ALIGN_LEFT|wx.ALL|wx.GROW, 5)
        #keysink = KeySink(self)
        #sizer.Add(keysink, wx.GROW)
        self.SetSizerAndFit(sizer)

class Dialog(wx.Dialog):
    default = {1:'WASDERF1', 2:'IJKLUYH2'}
    joyk = ('up', 'left', 'down', 'right', '1', '2', '3', '4')
    defaultJoy = {1:['J0-%s'%i for i in joyk],  2:['J1-%s'%i for i in joyk]}
    def __init__(self, parent, n, *args):
        wx.Dialog.__init__(self, parent, *args)
        vsizer = wx.BoxSizer(wx.VERTICAL)
        self.n = n
        self.keys = ['up', 'left', 'down', 'right', 'w', 'm', 's', 'start']
        #keylist = []
        self.boxn = 0
        self.boxes = []
        self.filename = '%s/cache/p%dcontrols' % (os.getcwd(), self.n)
        self.t = wx.StaticText(self)        
        vsizer.Add(self.t, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        keyssb = wx.StaticBox(self, -1, 'Configuration')
        keyssbsizer = wx.StaticBoxSizer(keyssb, wx.VERTICAL)
        gridsizer = wx.GridSizer(len(self.keys), 2, 2, 2)
        keyssbsizer.Add(gridsizer, -1, wx.GROW|wx.ALL)
        for n, i in enumerate(self.keys):
           k = wx.StaticText(self, -1, i.upper()+':')
           t = wx.StaticText(self, -1, '%s' % Dialog.default[self.n][n])
           self.boxes.append(t)
           gridsizer.Add(k, -1, flag=wx.ALIGN_RIGHT)
           gridsizer.Add(t, -1, flag=wx.ALIGN_LEFT)
        hsizer2.Add(keyssbsizer, -1, wx.ALL, 2)
        vb = wx.StaticBox(self, -1, 'Reset to Defaults')
        vbsizer = wx.StaticBoxSizer(vb, wx.VERTICAL)
        for n, i in enumerate(['P1 Keyboard', 'P2 Keyboard', 'P1 Joystick', 'P2 Joystick']):
            b = wx.Button(self, 60+n, i)
            vbsizer.Add(b, -1, wx.GROW|wx.ALL, 2)
        hsizer2.Add(vbsizer, -1, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2)
        vsizer.Add(hsizer2, -1, wx.ALL|wx.GROW, 2)
        
        wx.EVT_BUTTON(self, 60, lambda e: self.OnDefault(Dialog.default, 1))
        wx.EVT_BUTTON(self, 61, lambda e: self.OnDefault(Dialog.default, 2))
        wx.EVT_BUTTON(self, 62, lambda e: self.OnDefault(Dialog.defaultJoy, 1))
        wx.EVT_BUTTON(self, 63, lambda e: self.OnDefault(Dialog.defaultJoy, 2))

        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        for x, b in enumerate('Ok Cancel'.split()):
            b = wx.Button(self, 50+x, b)
            hsizer.Add(b, -1, wx.ALL | wx.GROW, 2)
        #vsizer.Add(wx.StaticLine(self, -1, size=(1,-1), style=wx.LI_HORIZONTAL), -1, wx.GROW|wx.ALL)
        vsizer.Add(hsizer, flag=wx.CENTER)
        #self.log = wx.StaticText(self); vsizer.Add(self.log, -1, wx.ALL|wx, 2)
        wx.EVT_BUTTON(self, 50, self.OnOk)
        wx.EVT_BUTTON(self, 51, self.OnCancel)
        #Srwx.EVT_TEXT_CTRL_(self, self.OnKeyUp)
        keysink = KeySink(self)
        keysink.SetSizeWH(0,0)      
        vsizer.Add(keysink)
        self.SetSizerAndFit(vsizer)
        self.UpdateText(None)
        load = cPickle.load(file(self.filename))
        key2i = dict((i,n) for n, i in enumerate(self.keys))
        #cPickle.dump(dict((k, self.default[self.n][n]) for n, k in enumerate(self.keys)), file(self.filename, 'w'))
        #raise 'u'
        for k, v in load.iteritems():
            self.boxes[key2i[k.lower()]].SetLabel(v)
    def UpdateText(self, evt, type=None, n=None, label=None):
        global keyId2Name
        if evt is not None:
            if type == wx.EVT_KEY_UP:
                code = evt.GetKeyCode()
                label =  keyId2Name[code] if code in keyId2Name else chr(code)
            elif type == wx.EVT_JOYSTICK_EVENTS:
                pass # HI THERE
            self.boxes[self.boxn-1].SetLabel('%-9s'%label.upper())
        self.boxes[self.boxn].SetFont(wx.Font(-1,wx.NORMAL,wx.NORMAL,wx.BOLD))
        if self.boxn > 0:
            self.boxes[self.boxn-1].SetFont(wx.Font(-1,wx.NORMAL,wx.NORMAL,wx.NORMAL))
        self.t.SetLabel('Press a key for %s!' % self.keys[self.boxn])
        self.boxn += 1
        if self.boxn == len(self.keys):
            self.OnOk(None)
                    
    def OnOk(self, event):
        dic = dict((k, self.boxes[n].GetLabel().strip()) for n, k in enumerate(self.keys))
        
        with file(self.filename, 'w') as f:
            cPickle.dump(dic, f)
        self.Close()
    def OnCancel(self, event):
        self.Close()
    
    def OnDefault(self, dic, sn):
        for n, i in enumerate(self.keys):
            self.boxes[n].SetLabel(dic[sn][n])
    
        
class KeySink(wx.Window):
    def __init__(self, parent):
        wx.Window.__init__(self, parent, -1)
        self.parent = parent
        self.haveFocus = False
        self.callSkip = True
        self.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
        self.SetFocus()
        self.joysticks = []
        self.firstj = wx.Joystick(wx.JOYSTICK1)
        self.joysticks.append(self.firstj)
        self.firstj.SetCapture(self)
        self.Bind(wx.EVT_JOYSTICK_EVENTS, lambda evt: self.JoyEventHandler(0, evt))        
        for n in range(self.firstj.GetNumberJoysticks()-1):
            j = wx.Joystick(eval('wx.JOYSTICK%d'%n+2))
            j.SetCapture(self)
            self.joysticks.append(j)
            j.Bind(EVT_JOYSTICK_EVENTS, lambda evt: self.JoyEventHandler(n+1, evt))
            raise '%s'%self.joysticks

    def JoyEventHandler(self, n, evt):
        e = evt
        #self.parent.log.SetLabel('%s'%e.GetPosition())
        pos = evt.GetPosition()
        buttons = evt.GetButtonState()
        posname = None
        label = None
        if pos[1] == 0:    posname = 'UP'
        elif pos[1] == -1: posname = 'DOWN'
        elif pos[0] == 0:  posname = 'LEFT'
        elif pos[0] == -1: posname = 'RIGHT'
        
        if posname is not None:
            label = 'J%d-%s' % (n, posname)
        else:
            def func():
                for i in range(4):
                    if buttons & (1<<i):
                        return i
                for i in range(4, 16):
                    if (buttons|8) & (1<<i):
                        return i
                return None
            but = func()
            if but is not None:
                label = 'J%d-%s' % (n, but)
        if label is not None:
            self.parent.UpdateText(evt, wx.EVT_JOYSTICK_EVENTS, n, label)

    def OnKeyUp(self, evt):
        self.parent.UpdateText(evt, wx.EVT_KEY_UP)

class DemoFrame(wx.Frame):
    """Main Frame holding the Panel."""
    def __init__(self, *args, **kwargs):
        global exitId, playId
        wx.Frame.__init__(self, 
            style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.RESIZE_BOX | wx.MAXIMIZE_BOX),
            *args, **kwargs)
        # Add the Widget Panel
        self.Panel = DemoPanel(self)
        self.Fit()
        wx.EVT_BUTTON(self, exitId, self.OnQuit)
        wx.EVT_BUTTON(self, playId, self.OnPlay)
        wx.EVT_BUTTON(self, p1Id, lambda event: self.Config(1, event))
        wx.EVT_BUTTON(self, p2Id, lambda event: self.Config(2, event))
        #self.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
        

        self.dic = {}
        filename = '%s/user.cfg' % os.getcwd()        
        self.usercfg = file(filename, 'r')
        for i in self.usercfg.readlines():
            data, var = i.strip().split(' ')
            self.dic[data] = var
        self.usercfg.close()
        self.Panel.rb.SetSelection(int(self.dic['fullscreen']))
        self.runika = False
    #def OnKeyUp(key, event):
    #    key = event.KeyCode()
    #    raise '%d' % key
    def Config(self, n, event=None):
        dlg = Dialog(self, n, -1, 'Configure Player %d Controls' % n)
        dlg.CenterOnScreen()
        val = dlg.ShowModal()   
        dlg.Destroy()     
    def OnQuit(self, event=None):
        self.Close()
    def OnPlay(self, event=None):
        global runIka
        self.dic['fullscreen'] = '%d'% self.Panel.rb.GetSelection()
        o = file('%s/user.cfg' % os.getcwd(), 'w')
        for k, v in self.dic.iteritems():
            o.write('%s %s\n'% (k, v))
        runIka = True
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    frame = DemoFrame(None, title="Beast Genesis")
    frame.CenterOnScreen()
    frame.Show()
    app.MainLoop()
    if runIka:
        os.system('"%s/ika.exe"' % os.getcwd())