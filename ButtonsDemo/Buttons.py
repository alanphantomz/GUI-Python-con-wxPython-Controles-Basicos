import wx
class MyWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MyWindow, self).__init__(parent, title = title, size = (200, 200))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.btn = wx.Button(panel, -1, "click me")
        vbox.Add(self.btn, 0, wx.ALIGN_CENTER)
        self.btn.Bind(wx.EVT_BUTTON, self.OnClicked)

        self.tbtn = wx.ToggleButton(panel, -1, "click to on")
        vbox.Add(self.tbtn, 0, wx.EXPAND|wx.ALIGN_CENTER)
        self.tbtn.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggle)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        bmp = wx.Bitmap("aceptar.png", wx.BITMAP_TYPE_PNG)
        self.bmpbtn = wx.BitmapButton(panel, id = wx.ID_ANY, bitmap = bmp,
                                      size = (bmp.GetWidth()+10, bmp.GetHeight()+10))
        hbox.Add(self.bmpbtn,0, wx.ALIGN_CENTER)
        self.bmpbtn.Bind(wx.EVT_BUTTON, self.OnClicked)
        self.bmpbtn.SetLabel("aceptar")

        bmp1 = wx.Bitmap("back.png", wx.BITMAP_TYPE_PNG)
        self.bmpbtn1 = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp1,
                                      size=(bmp.GetWidth() + 10, bmp.GetHeight() + 10))
        hbox.Add(self.bmpbtn1, 0, wx.ALIGN_CENTER)
        self.bmpbtn1.Bind(wx.EVT_BUTTON, self.OnClicked)
        self.bmpbtn1.SetLabel("atras")

        bmp2 = wx.Bitmap("cancel.png", wx.BITMAP_TYPE_PNG)
        self.bmpbtn2 = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp2,
                                      size=(bmp.GetWidth() + 10, bmp.GetHeight() + 10))
        hbox.Add(self.bmpbtn2, 0, wx.ALIGN_CENTER)
        self.bmpbtn2.Bind(wx.EVT_BUTTON, self.OnClicked)
        self.bmpbtn2.SetLabel("cancelar")

        vbox.Add(hbox, 1, wx.ALIGN_CENTER)
        panel.SetSizer(vbox)

        self.Centre()
        self.Show()

    def OnClicked(self, event):
        btn = event.GetEventObject().GetLabel()
        print "Label of pressed button =", btn

    def OnToggle(self, event):
        state = event.GetEventObject().GetValue()
        if state == True:
            print "Toggle button state off"
            event.GetEventObject().SetLabel("click to off")

        else:
            print "Toggle button state on"
            event.GetEventObject().SetLabel("click to on")

app = wx.App()
MyWindow(None, "Button demo")
app.MainLoop()
