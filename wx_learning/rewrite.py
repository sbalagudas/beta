import wx
class Frame(wx.Frame):
    def __init__(self,parent=None,id=-1,title='create menu',pos=wx.DefaultPosition,size=(800,600)):
        wx.Frame.__init__(self,parent,id,title,pos,size)
        panel = wx.Panel(self,-1)
        panel.SetBackgroundColour('Dim Grey')
        self.createMenuBar()

    def createMenuBar(self):
        self.menuBar = wx.MenuBar()
        for eachMenu in self.menuInfo():
            label = eachMenu[0]
            menuData = eachMenu[1]
            self.menuBar.Append(self.createMenu(menuData),label)
        self.SetMenuBar(self.menuBar)

    def createMenu(self,menudata):
        menu = wx.Menu()
        for eachMenu in menudata :
            if 2 == len(eachMenu):
                label = eachMenu[0]
                subMenu = self.createMenu(eachMenu[1])
                menu.AppendMenu(wx.NewId(),label,subMenu)
            else :
                self.createMenuItem(menu,*eachMenu)

        return menu

    def createMenuItem(self,menu,text,status,handler,kind=wx.ITEM_NORMAL):
        if not text:
            menu.AppendSeparator()
        else :
            menuItem = menu.Append(-1,text,status, kind)
            self.Bind(wx.EVT_MENU,handler,menuItem)


    def setPenSize(self,event):
        pass

    def setPenColor(self,event):
        pass
    def newFile(self,event):
        pass
    def openFile(self,event):
        pass
    def otherColor(self,event):
        pass
    def onSave(self,event):
        pass
    def exit(self,event):
        pass
    def saveFileAs(self,event):
        pass





    def menuInfo(self):
        return [("&File",(
                 ("&New","Create a new file",self.newFile),
                 ("&Open","open a file",self.openFile),
                 ("&Pen Size",(
                  ("&1","",self.setPenSize,wx.ITEM_RADIO),
                  ("&2","",self.setPenSize,wx.ITEM_RADIO),
                  ("&3","",self.setPenSize,wx.ITEM_RADIO),
                  ("&4","",self.setPenSize,wx.ITEM_RADIO),
                  ("&5","",self.setPenSize,wx.ITEM_RADIO))),
                 ("&Pen Colour",(
                  ("&Red","",self.setPenColor,wx.ITEM_RADIO),
                  ("&Green","",self.setPenColor,wx.ITEM_RADIO),
                  ("&Blue","",self.setPenColor,wx.ITEM_RADIO),
                  ("&Cyan","",self.setPenColor,wx.ITEM_RADIO),
                  ("&Other Color...","",self.otherColor,wx.ITEM_RADIO))),
                 ("&Save","save file",self.onSave),
                 ("&Save as...","save file as another file",self.saveFileAs),
                 ("&Exit","Quit",self.exit)))]

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = Frame()
    frame.Show()
    app.MainLoop()