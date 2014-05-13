#@PydevCodeAnalysisIgnore
import wx
import os

class Keys(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Dialog.__init__(self, parent, *args, **kwargs)
        pass


class DemoPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        rbId, playId, exitId, p1ControlsId, p2ControlsId = tuple(range(10,15))
        self.parent = parent  # Sometimes one can use inline Comments
        rb = wx.RadioBox(self, rbId, "Screen mode", wx.DefaultPosition, wx.DefaultSize, ['Full Screen', 'Window'])
        okcancel = wx.BoxSizer(wx.HORIZONTAL)
        b1 = wx.Button(self, playId, label='Play')
        b2 = wx.Button(self, exitId, label='Exit')
        for b in (b1, b2):
            okcancel.Add(b, 0, wx.ALIGN_LEFT|wx.ALL, 5)        
        controls = wx.BoxSizer(wx.HORIZONTAL)
        p1 = wx.Button(self, p1Id, label="P1 Controls")
        p2 = wx.Button(self, p2Id, label="P2 Controls")
        for p in (p1, p2):
            controls.Add(p, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        wx.EVT_BUTTON(self, exitId, self.OnExit)
        #b2.Bind(wx.EVT_BUTTON, self.OnExit)
        #sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)
        #NothingBtn.Bind(wx.EVT_BUTTON, self.DoNothing )

        sizer = wx.BoxSizer(wx.VERTICAL)
        for b in (rb, controls, line, okcancel):
            sizer.Add(b, 0, wx.ALIGN_LEFT|wx.ALL|wx.GROW, 5)

        self.SetSizerAndFit(sizer)

    def OnExit(self, event=None):
        self.Close(True)

    def OnMsgBtn(self, event=None):
        """Bring up a wx.MessageDialog with a useless message."""
        dlg = wx.MessageDialog(self,
                               message='A completely useless message',
                               caption='A Message Box',
                               style=wx.OK|wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()

class DemoFrame(wx.Frame):
    """Main Frame holding the Panel."""
    def __init__(self, *args, **kwargs):
        """Create the DemoFrame."""
        wx.Frame.__init__(self, 
            style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.RESIZE_BOX | wx.MAXIMIZE_BOX),
            *args, **kwargs)
        # Add the Widget Panel
        self.Panel = DemoPanel(self)
        self.Fit()

    def OnQuit(self, event=None):
        """Exit application."""
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    frame = DemoFrame(None, title="Beast Genesis")
    frame.Show()
    app.MainLoop()