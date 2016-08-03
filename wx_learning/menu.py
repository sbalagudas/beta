import wx

class statusBar(wx.Frame):
    @staticmethod
    def initStatusBar(parent,id=1):
        statusBar = wx.StatusBar(parent,id)
        statusBar.SetFieldsCount(2)
        statusBar.SetStatusWidths([-1,-1])

class menuFrame(wx.Frame):
    def __init__(self,parent=None,id=-1):
        wx.Frame.__init__(self,parent,id)

        #statusBar.initStatusBar(self)
        self.initStatusBar()
    def initStatusBar(self):
        statusBar = self.CreateStatusBar()
        statusBar.SetFieldsCount(2)
        statusBar.SetStatusWidths([-1,-1])
        self.createMenuBar()



    def menuDataType1(self):
        return [("&File",(
                ("&New","New File",self.onNew),
                ("&Open","Open a File",self.onOpen),
                ("&Save","Save a File",self.onSave),
                ("","",""),
                ("Color",(
                ("&Black","",self.onColor,wx.ITEM_RADIO),
                ("&Red","",self.onColor,wx.ITEM_RADIO),
                ("&Green","",self.onColor,wx.ITEM_RADIO),
                ("&Blue","",self.onColor,wx.ITEM_RADIO),
                ("&Purple","",self.onColor,wx.ITEM_RADIO))),
                ("","",""),
                ("&Quit","Quit",self.onCloseWindow)))]


    def createMenuBar(self):
        self.menuBar = wx.MenuBar()
        for eachMenuData in self.menuDataType1():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1]
            self.menuBar.Append(self.createMenu(menuItems),menuLabel)
        self.SetMenuBar(self.menuBar)

    def createMenu(self,menudata):
        menu = wx.Menu()
        for eachItem in menudata:
            if 2 == len(eachItem):
                label = eachItem[0]
                subMenu = self.createMenu(eachItem[1])
                menu.AppendMenu(wx.NewId(),label,subMenu)
            else :
                print "eachItem : ",eachItem
                self.craeteMenuItem(menu,*eachItem)
        return menu

    def craeteMenuItem(self,menu,label,status,handler,kind=wx.ITEM_NORMAL):
        if not label:
            menu.AppendSeparator()
            return
        menuItem = menu.Append(-1,label,status,kind)
        self.Bind(wx.EVT_MENU,handler,menuItem)
    def onNew(self,event):
        pass
    def onOpen(self,event):
        pass
    def onSave(self,event):
        pass
    def onColor(self,event):
        menubar = self.GetMenuBar()
        itemId = event.GetId()
        item = menubar.FindItemById(itemId)
        color = item.GetLabel()
        self.pt.setColor(color)
    def onCloseWindow(self,event):
        pass

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = menuFrame()
    frame.Show()
    app.MainLoop()


