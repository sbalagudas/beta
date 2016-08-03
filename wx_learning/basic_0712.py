import wx

class Frame(wx.Frame):
    def __init__(self,parent=None,id=-1,title='custom window',pos=wx.DefaultPosition,size=(400,300)):
        wx.Frame.__init__(self,parent,id,title,pos,size)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("Dim Grey")
        #self.panel.SetBackgroundColour("AQUAMARINE")

        self.buttonD = self.createButtons(self.panel)

    def buttonInfo(self):
        return (('apple',self.appleEnter),
                ('banana',self.bananaEnter),
                ('pear',self.pearEnter),
                ('strawberry',self.strawberryEnter),
                ('pineapple',self.pineappleEnter),
                ('peach',self.peachEnter))

    def createButtons(self,panel,xPos=0):
        yPos = 0
        i = 1
        buttonDict = {}
        for label,handler in self.buttonInfo():
            pos = (xPos,yPos)
            button = self.createOneButton(panel,label,pos,handler)
            buttonDict[label] = button
            yPos = yPos + button.GetSize().height + 1
        return buttonDict

    def createOneButton(self,parent,label,pos,handler,size=(100,30)):
        button = wx.Button(parent,wx.NewId(),label,pos)
        button.SetBackgroundColour('Medium Turquoise')
        button.Bind(wx.EVT_ENTER_WINDOW,handler,button)
        return button
    #new function start --->
    def createButtonsNew(self,panel,xPos=0):
        yPos = 0
        i = 1
        buttonDict = {}
        for label,handler in self.buttonInfo():
            pos = (xPos,yPos)
            button = self.createOneButtonNew(panel,label,pos)
            buttonDict[label] = button
            yPos = yPos + button.GetSize().height + 1
        return buttonDict

    def createOneButtonNew(self,parent,label,pos,size=(100,30)):
        button = wx.Button(parent,wx.NewId(),label,pos)
        button.SetBackgroundColour('Medium Turquoise')
        button.Bind(wx.EVT_ENTER_WINDOW,self.enterWindow,button)
        return button

    def enterWindow(self,event):
        button.SetBackgroundColour('Red')

    #new function end

    def appleEnter(self,event):
        self.buttonD['apple'].SetBackgroundColour('Cyan')
    def bananaEnter(self,event):
        self.buttonD['banana'].SetBackgroundColour('Cyan')
    def pearEnter(self,event):
        self.buttonD['pear'].SetBackgroundColour('Cyan')
    def strawberryEnter(self,event):
        self.buttonD['strawberry'].SetBackgroundColour('Cyan')
    def pineappleEnter(self,event):
        self.buttonD['pineapple'].SetBackgroundColour('Cyan')
    def peachEnter(self,event):
        self.buttonD['peach'].SetBackgroundColour('Cyan')

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = Frame()
    frame.Show()
    app.MainLoop()

