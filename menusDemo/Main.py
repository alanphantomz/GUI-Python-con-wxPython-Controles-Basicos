import wx
class MyWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MyWindow, self).__init__(parent, title = title, size = (250, 150))
        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()

        menu = wx.Menu()

        #  MenuItem nuevo
        newItem = wx.MenuItem(menu, wx.ID_NEW, text = "Nuevo", kind = wx.ITEM_NORMAL)
        newItem.SetBitmap(wx.Bitmap("new.png"))
        menu.AppendItem(newItem)
        menu.AppendSeparator()

        #  Menu dentro de Menu
        editMenu = wx.Menu()

        copyItem = wx.MenuItem(editMenu, 100, text = "copiar", kind = wx.ITEM_NORMAL)
        copyItem.SetBitmap(wx.Bitmap("copiar.png"))
        editMenu.AppendItem(copyItem)

        cutItem = wx.MenuItem(editMenu, 101, text = "cortar", kind = wx.ITEM_NORMAL)
        cutItem.SetBitmap(wx.Bitmap("cortar.png"))
        editMenu.AppendItem(cutItem)

        pasteItem = wx.MenuItem(editMenu, 102, text = "pegar", kind = wx.ITEM_NORMAL)
        pasteItem.SetBitmap(wx.Bitmap("pegar.png"))
        editMenu.AppendItem(pasteItem)

        menu.AppendMenu(wx.ID_ANY, "Editar", editMenu)
        menu.AppendSeparator()

        #  Menu Radio
        radio1 = wx.MenuItem(menu, 200, text = "Radio 1", kind = wx.ITEM_RADIO)
        radio2  =wx.MenuItem(menu, 300, text = "Radio 2", kind = wx.ITEM_RADIO)
        menu.AppendItem(radio1)
        menu.AppendItem(radio2)
        menu.AppendSeparator()

        # menuItem check
        menu.AppendCheckItem(103, "Checkable")
        quit = wx.MenuItem(menu, wx.ID_EXIT, "&Quit\tCtrl+Q")
        menu.AppendItem(quit)

        menubar.Append(menu, '&File')
        self.SetMenuBar(menubar)
        self.text = wx.TextCtrl(self, -1, style = wx.EXPAND | wx.TE_MULTILINE)
        self.Bind(wx.EVT_MENU, self.menuhandler)
        self.SetSize((350, 250))
        self.Centre()
        self.Show(True)

    def menuhandler(self, event):
        id = event.GetId()
        if id == wx.ID_NEW:
            self.text.AppendText("new" + "\n")

ex = wx.App()
MyWindow(None, 'MenuBar demo')
ex.MainLoop()

