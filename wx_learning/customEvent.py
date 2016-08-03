import wx

class doubleBtnClick(wx.PyCommandEvent):
    def __init__(self,evtType,id):
        wx.PyCommandEvent.__init__(self,evtType,id)
        self.clickCount = 0

    def getClickCount(self):
        return self.clickCount

    def setClickCount(self,clickCount):
        self.clickCount = clickCount

myEVT_TWO_BUTTONS = wx.NewEventType()
EVT_TWO_BUTTONS = wx.PyEventBinder(myEVT_TWO_BUTTONS,1)

class Frame(wx.Frame):
    def __init__(self,parent=None,id=-1,title='custom event window',pos=wx.DefaultPosition,size=(330,200)):
        wx.Frame.__init__(self,parent,id,title,pos,size)
        self.panel = wx.Panel(self,1)
        self.panel.SetBackgroundColour('Dark Grey')

        self.btnInfo = (('apple',self.appleClick),('banana',self.bananaClick))
        print self.btnInfo
        self.createButtons(self.panel)

        self.appleClick = False
        self.bananaClick = False
        self.buttonClick = 0

    def createButtons(self,parent,yPos=50):
        xPos = 50
        for label,handler in self.btnInfo:
            pos = (xPos,yPos)
            button = self.createOneButton(parent,label,pos,handler)
            width = button.GetSize().width
            xPos += width + 20

    def createOneButton(self,parent,label,pos,handler,size=(100,30)):
        button = wx.Button(parent,wx.NewId(),label,pos,size)
        button.Bind(wx.EVT_LEFT_DOWN,handler,button)
        return button

    def appleClick(self,event):
        self.appleClick = True
        evt = self.btnClick()
        self.SetTitle('click count : %s',evt.getClickCount())
        event.Skip()
    def bananaClick(self,event):
        self.bananaClick = True
        evt = self.btnClick()
        self.SetTitle('click count : %s',evt.getClickCount())
        event.Skip()

    def btnClick(self):
        self.buttonClick += 1
        if self.bananaClick and self.appleClick:
            self.bananaClick = False
            self.bananaClick = False
            print "click : ",self.buttonClick
            evt = doubleBtnClick(myEVT_TWO_BUTTONS,self.GetId())
            evt.setClickCount(self.buttonClick)
            self.GetEventHandler().ProcessEvent(evt)
            return evt


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = Frame()
    frame.Show()
    app.MainLoop()