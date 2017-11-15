import wx
class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)
        b = wx.Button(self, label = "propagar", pos = (50,50))
        b.Bind(wx.EVT_BUTTON, self.btnclk)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

    def OnButtonClicked(self, e):
        print "Panel recibio el evento click. propagado a la clase Frame"
        e.Skip()

    def btnclk(self, e):
        print "Button recibe el evento click. propagado a la clase Panel"
        e.Skip()

class Example(wx.Frame):
    def __init__(self, parent):
        super(Example, self).__init__(parent)
        self.InitUI()

    def InitUI(self):
        mpnl = MyPanel(self)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        self.SetTitle("Event propagation demo")
        self.Centre()
        self.Show(True)

    def OnButtonClicked(self, e):
        print "click event received by frame class"
        e.Skip()

ex = wx.App()
Example(None)
ex.MainLoop()