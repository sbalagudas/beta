import wx
import cPickle as pk
import os

from paint import Paint

class menuFrame(wx.Frame):
    def __init__(self,parent=None,id=-1,title='Menu',pos=wx.DefaultPosition,size=(800,600)):
        wx.Frame.__init__(self,parent,id,title,pos,size)

        self.pt = Paint(self,1)
        self.initStatusBar()
        self.pt.Bind(wx.EVT_MOTION,self.mouseMotion)
        self.createMenuBar()

        self.title = "Banana~~~~"
        self.filename = ""
        self.button = wx.Button(self.pt,label="A",pos=(0,0),size=(22,22))

    def mouseMotion(self,event):
        self.statusBar.SetStatusText("Position : %s"%(str(event.GetPositionTuple())),0)
        xPos = event.GetPositionTuple()[0]
        yPos = event.GetPositionTuple()[1]
        if xPos > 200 and xPos < 300 and yPos > 200 and yPos < 300:
            self.statusBar.SetStatusText("secret place~",1)
        else :
            self.statusBar.SetStatusText("",1)
        event.Skip()

    def initStatusBar(self):
        self.statusBar = self.CreateStatusBar()
        self.statusBar.SetFieldsCount(2)
        self.statusBar.SetStatusWidths([-1,-1])
    def menuData(self):
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
        for eachMenuData in self.menuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1]
            self.menuBar.Append(self.createMenu(menuItems),menuLabel)
        self.SetMenuBar(self.menuBar)

    def createMenu(self,menudata):
        menu = wx.Menu()
        for eachItem in menudata:
            #print "eachitem : ",eachItem
            if 2 == len(eachItem):
                label = eachItem[0]
                subMenu = self.createMenu(eachItem[1])
                menu.AppendMenu(wx.NewId(),label,subMenu)
            else :
                #print "eachItem : ",eachItem
                self.createMenuItem(menu,*eachItem)
        return menu

    def createMenuItem(self,menu,label,status,handler,kind=wx.ITEM_NORMAL):
        if not label:
            menu.AppendSeparator()
            return
        menuItem = menu.Append(-1,label,status,kind)
        self.Bind(wx.EVT_MENU,handler,menuItem)

    def onNew(self,event):
        self.pt.initBuffer()
    def onOpen(self,event):
        dlg = wx.FileDialog(self,"open a file...",os.getcwd(),style=wx.OPEN,wildcard=self.wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.readFile()
            self.SetTitle(self.title+"---"+self.filename)
        dlg.Destroy()

    def saveFile(self,event):
        if self.filename :
            data = self.pt.getLinesData()
            f = open(self.filename,'w')
            pk.dump(data,f)
            f.close()

    def onSave(self,event):
        if not self.filename :
            self.onSaveAs(event)
        else :
            self.saveFile(event)

    def onSaveAs(self,event):
        dlg = wx.FileDialog(self,"save a file as ...",os.getcwd(),style=wx.SAVE|wx.OVERWRITE_PROMPT,wildcard=self.wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            print "filename in get path : ",filename
            if not os.path.splitext(filename)[1]:
                filename = filename+'.banana'
            self.filename = filename
            self.saveFile(event)
            self.SetTitle(self.title+'----'+self.filename)
        dlg.Destroy()

    def readFile(self):
        if self.filename :
            try :
                f = open(self.filename,'r')
                data = pk.load(f)
                f.close()
                self.pt.setLinesData(data)
            #except pk.UnpickleableError:
            except :
                wx.MessageBox("read file failed...",style=wx.OK|wx.ICON_EXCLAMATION)
    wildcard = "banana file (*.banana)|*.banana|All Files (*.*)|*.*"


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
