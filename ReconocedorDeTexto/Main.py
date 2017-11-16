import wx
# Leer una cadena, y contar nro. vocales, nro. palabras, nro. consonantes, nro. espacios
class MyWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MyWindow, self).__init__(parent, title = title, size = (300, 300))

        panel  = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        #  Para lectura de cadena
        l1 = wx.StaticText(panel, -1, "Cadena")
        self.t1 = wx.TextCtrl(panel, size = (180, 27))

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(l1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox1.Add(self.t1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox1)

        #  Boton para calcular
        self.btn = wx.Button(panel, -1, "calcular")
        self.btn.Bind(wx.EVT_BUTTON, self.OnClicked)
        vbox.Add(self.btn, 0, wx.EXPAND | wx.ALIGN_CENTER)


        # Para mostrar Numero de vocales
        l2 = wx.StaticText(panel, -1, "Vocales")
        self.t2 = wx.TextCtrl(panel)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(l2, 1, wx.ALIGN_LEFT | wx.ALL, 5)
        hbox2.Add(self.t2, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox2)


        # Para mostrar numero de palabras
        l3 = wx.StaticText(panel, -1, "Palabras")
        self.t3 = wx.TextCtrl(panel)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(l3, 1, wx.ALIGN_LEFT|wx.ALL, 5)
        hbox3.Add(self.t3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox3)


        # Para mostrar numero de consonantes
        l4 = wx.StaticText(panel, -1, "Consonantes")
        self.t4 = wx.TextCtrl(panel)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4.Add(l4, 1, wx.ALIGN_LEFT | wx.ALL, 5)
        hbox4.Add(self.t4, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox4)

        # Para mostrar el numero de espacios
        l5 = wx.StaticText(panel, -1, "Espacios")
        self.t5 = wx.TextCtrl(panel)
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5.Add(l5, 1, wx.ALIGN_LEFT | wx.ALL, 5)
        hbox5.Add(self.t5, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox5)

        panel.SetSizer(vbox)
        self.Centre()
        self.Show()

    def OnClicked(self, event):
        cadena = self.t1.GetValue()
        voc, con, esp, pal = self.ReconoceCadena(cadena)
        self.t2.SetValue(str(voc))
        self.t3.SetValue(str(pal))
        self.t4.SetValue(str(con))
        self.t5.SetValue(str(esp))

    def ReconoceCadena(self, cadena):
        cadena = cadena + " "
        numEsp = -1
        numVoc = 0
        numCon = 0
        for i in cadena:
            if i == " ": numEsp += 1
            elif i in ('a', 'e', 'i', 'o', 'u'): numVoc += 1
            elif (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90): numCon +=1
        return (numVoc, numCon, numEsp, numEsp + 1)


app = wx.App()
MyWindow(None, "Contador en cadenas")
app.MainLoop()