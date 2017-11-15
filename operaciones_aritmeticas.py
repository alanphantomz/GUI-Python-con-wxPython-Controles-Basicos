import wx
class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        # CREAMOS LOS TEXTOS A MOSTRAR
        self.txtNumero1 = wx.StaticText(self, label = "Numero1: ", pos = (25, 25))
        self.txtNumero2 = wx.StaticText(self, label = "Numero2: ", pos = (25, 75))
        self.txtResultado = wx.StaticText(self, label = "Resultado", pos = (25, 125))

        # CREAMOS LAS CAJAS DONDE SE INTRODUCIRAN LOS NUMEROS
        self.etNum1 = wx.TextCtrl(self, pos = (110, 25))
        self.etNum2 = wx.TextCtrl(self, pos = (110, 75))
        self.etResul = wx.TextCtrl(self, pos = (110, 125))

        # CREAMOS LOS BOTONES
        btnSumar = wx.Button(self, label = "+", pos = (250, 25))
        btnRestar = wx.Button(self, label="-", pos=(250, 65))
        btnMulti = wx.Button(self, label="*", pos=(250, 105))
        btnDivid = wx.Button(self, label="/", pos=(250, 145))
        btnBorrar = wx.Button(self, label = "Borrar", pos = (250, 195))

        # ENLAZAMOS A METODO MANEJADOR DE EVENTOS
        btnSumar.Bind(wx.EVT_BUTTON, self.btnclk)
        btnRestar.Bind(wx.EVT_BUTTON, self.btnclk)
        btnMulti.Bind(wx.EVT_BUTTON, self.btnclk)
        btnDivid.Bind(wx.EVT_BUTTON, self.btnclk)

        btnBorrar.Bind(wx.EVT_BUTTON, self.btnclk)


    def btnclk(self, e):
        valor = e.GetEventObject().GetLabel()
        if  valor == "Borrar":
            self.etNum1.SetValue("")
            self.etNum2.SetValue("")
            self.etResul.SetValue("")
        elif valor == "+":
            num1 = int(self.etNum1.GetValue())
            num2 = int(self.etNum2.GetValue())
            suma = num1 + num2
            self.etResul.SetValue(str(suma))
        elif valor == "-":
            num1 = int(self.etNum1.GetValue())
            num2 = int(self.etNum2.GetValue())
            resta = num1 - num2
            self.etResul.SetValue(str(resta))
        elif valor == "*":
            num1 = int(self.etNum1.GetValue())
            num2 = int(self.etNum2.GetValue())
            mul = num1 * num2
            self.etResul.SetValue(str(mul))
        elif valor == "/":
            num1 = int(self.etNum1.GetValue())
            num2 = int(self.etNum2.GetValue())
            div = num1 / num2
            self.etResul.SetValue(str(div))


class Example(wx.Frame):
    def __init__(self, parent):
        super(Example, self).__init__(parent)
        self.InitUI()

    def InitUI(self):
        mpnl = MyPanel(self)
        self.SetTitle("Operaciones Fundamentales")
        self.Centre()
        self.Show(True)

ex = wx.App()
Example(None)
ex.MainLoop()