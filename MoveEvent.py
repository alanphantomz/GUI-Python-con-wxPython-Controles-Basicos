import wx
class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.Bind(wx.EVT_MOVE, self.OnMove)
        self.SetSize((250, 180))
        self.SetTitle('Move event')
        self.Centre()
        self.Show(True)

    def OnMove(self, e):
        x, y = e.GetPosition()
        print "Current window position x =", x, " y = ", y

ex = wx.App()
Example(None)
ex.MainLoop()