import wx
class MyWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MyWindow, self).__init__(parent, title = title, size = (300, 200))

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        self.label = wx.StaticText(panel, label = "Your choice:", style = wx.ALIGN_CENTER)
        box.Add(self.label, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 20)

        cblbl = wx.StaticText(panel, label = "combo box", style = wx.ALIGN_CENTER)
        box.Add(cblbl, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)


        languages = ['C', 'C++', 'Python', 'Java', 'Perl']
        self.combo = wx.ComboBox(panel, choices = languages)
        box.Add(self.combo, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)


        chlbl = wx.StaticText(panel, label = "Choice control", style = wx.ALIGN_CENTER)
        box.Add(chlbl, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        self.choice = wx.Choice(panel, choices = languages)
        box.Add(self.choice, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5)

        box.AddStretchSpacer()
        self.combo.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        self.choice.Bind(wx.EVT_CHOICE, self.OnChoice)

        panel.SetSizer(box)
        self.Center()
        self.Show()

    def OnCombo(self, event):
        self.label.SetLabel("You selected "+self.combo.GetValue()+" from combobox")

    def OnChoice(self, event):
        self.label.SetLabel("You selected "+self.choice.GetString(self.choice.GetSelection())+" from choice")

app = wx.App()
MyWindow(None, "ComboBox and Choice demo")
app.MainLoop()