import wx
from paint import Paint as pt
import cPickle as pk
import ControlPanel as CP
import os

class Frame(wx.Frame):
    def __init__(self,parent=None,id=1,title="Saving Practice...",pos=wx.DefaultPosition,size=(800,600)):
        wx.Frame.__init__(self,parent,id,title,pos,size)
        self.paintWindow = pt(self,-1)
        self.createMenuBar()
        self.filename = ""
        #self.buttonLeft = wx.Button(self.paintWindow,label='Left',style=wx.ALIGN_RIGHT)
        self.createPanel()

        self.wildcard = "banana file (*.banana)|*.banana|All Files (*.*)|*.*"
    def createPanel(self):
        controlPanel = CP.ControlPanel(self,-1,self.paintWindow)
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(controlPanel,0,wx.EXPAND)
        box.Add(self.paintWindow,0,wx.EXPAND)
        #box.Add(self.buttonLeft,0,wx.EXPAND)
        self.SetSizer(box)

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

    #create menu bar and menu
    def createMenuBar(self):
        self.menuBar = wx.MenuBar()
        for eachMenuData in self.menuInfo():
            menuLabel = eachMenuData[0]
            menuData = eachMenuData[1]
            self.menuBar.Append(self.createMenu(menuData),menuLabel)
        self.SetMenuBar(self.menuBar)

    def createMenu(self,menuData):
        menu = wx.Menu()
        for eachMenu in menuData:
            if 2 == len(eachMenu):
                label = eachMenu[0]
                subMenu = self.createMenu(eachMenu[1])
                menu.AppendMenu(wx.NewId(),label,subMenu)
            else :
                self.createMenuItem(menu,*eachMenu)

        return menu
    def createMenuItem(self,menu,label,status,handler,kind=wx.ITEM_NORMAL):
        if not label:
            menu.AppendSeparator()
            return
        menuItem = menu.Append(-1,label,status,kind)
        self.Bind(wx.EVT_MENU,handler,menuItem)

    ####################################################
    #def the handler functions
    ####################################################
    def getItemLabel(self,event):
        menuBar = self.GetMenuBar()
        itemId = event.GetId()
        item = menuBar.FindItemById(itemId)
        itemLabel = item.GetLabel()
        return itemLabel

    def openFile(self,event):
        fileDlg = wx.FileDialog(self,message="open file",defaultDir=os.getcwd(),style=wx.OPEN,wildcard=self.wildcard)
        #fileDlg = wx.FileDialog(self,"open a file...",os.getcwd(),style=wx.OPEN,wildcard=self.wildcard)
        if fileDlg.ShowModal() == wx.ID_OK :
            self.filename = fileDlg.GetPath()
            self.readFile()
            self.SetTitle("open the file"+self.filename)
            fileDlg.Destroy()

    def readFile(self) :
        if self.filename :
            try :
                f = open(self.filename,'r')
                data = pk.load(f)
                f.close()
                self.paintWindow.setLinesData(data)
            except :
                 wx.MessageBox("read file failed...",style=wx.OK|wx.ICON_EXCLAMATION)

    def newFile(self,event):
        print "self.paintWindow.getLinesData()",self.paintWindow.getLinesData()
        if self.paintWindow.getLinesData():
            msgDlg = wx.MessageDialog(self,"do you want to save the current file ? ",style=wx.YES_NO)
            if msgDlg.ShowModal() == wx.ID_YES :
                print "saving ..."
                self.onSave(event)
            else :
                print "not saving ..."
                data = []
                self.paintWindow.setLinesData(data)
        else :
            print "nothing happens"
    def setPenSize(self,event):
        size = self.getItemLabel(event)
        self.paintWindow.setThickness(int(size))

    def setPenColor(self,event):
        color = self.getItemLabel(event)
        self.paintWindow.setColor(color)

    def saveFile(self,event):
        if self.filename :
            data = self.paintWindow.getLinesData()
            f = open(self.filename,'w')
            print "open file %s"%self.filename
            pk.dump(data,f)
            f.close()

    def otherColor(self,event):
        colorDlg = wx.ColourDialog(self)
        colorDlg.GetColourData().SetChooseFull(True)
        if colorDlg.ShowModal() == wx.ID_OK :
            self.paintWindow.setColor(colorDlg.GetColourData().GetColour())

    def onSave(self,event):
        if not self.filename :
            print "saveFileAs called."
            self.saveFileAs(event)
        else :
            print "saveFile called."
            self.saveFile(event)

    def saveFileAs(self,event):
        fileDlg = wx.FileDialog(self,message="save file as",defaultDir=os.getcwd(),style=wx.SAVE|wx.OVERWRITE_PROMPT,wildcard=self.wildcard)

        if fileDlg.ShowModal() == wx.ID_OK :
            tempFileName = fileDlg.GetPath()
            print "tempFileName",tempFileName
            if not os.path.splitext(tempFileName)[1]:
                tempFileName = tempFileName+'.banana'
            print "saveFile in saveFileAs called..."
            self.filename = tempFileName
            self.saveFile(event)
            fileDlg.SetTitle("saving file for "+self.filename)
        fileDlg.Destroy()
    def exit(self,event):
        self.Destroy()

class spalshScreen(wx.App):
    def __init__(self,redirect=False,filename=None):
        wx.App.__init__(self,redirect,filename)

    def OnInit(self):
        bmp = wx.Image("d:\\Jellyfish.jpg",wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        wx.SplashScreen(bmp,wx.SPLASH_NO_CENTRE|wx.SPLASH_TIMEOUT,10000,None,-1)
        wx.Yield()

        frame = Frame()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == "__main__" :
    #app = wx.PySimpleApp()
    #frame = Frame()
    #frame.Show()
    app = spalshScreen()
    app.MainLoop()