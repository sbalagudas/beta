import wx
import time

class Frame(wx.Frame):
    def __init__(self,parent=None,id=-1,title="events",pos=wx.DefaultPosition,size=(400,200)):
        wx.Frame.__init__(self,parent,id,title,pos,size)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("Dim Grey")

        self.btnLeft = wx.Button(self.panel,label="Left Button",pos=(10,30),size=(100,30))
        self.btnLeft.SetBackgroundColour('Medium Turquoise')
        self.btnRight = wx.Button(self.panel,label="Right Button",pos=(10,60),size=(100,30))
        self.btnRight.SetBackgroundColour('Medium Turquoise')

        #button definition.
        self.btnLeft.Bind(wx.EVT_ENTER_WINDOW,self.enterWindowLeft)
        self.btnLeft.Bind(wx.EVT_LEAVE_WINDOW,self.leaveWindowLeft)
        self.btnRight.Bind(wx.EVT_ENTER_WINDOW,self.enterWindowRight)
        self.btnRight.Bind(wx.EVT_LEAVE_WINDOW,self.leaveWindowRight)
        self.Bind(wx.EVT_BUTTON,self.countDownFunc,self.btnLeft)

        #static text definition
        self.text=wx.StaticText(self.panel,id=wx.NewId(),label = "initiating...",pos=(120,30),size=(100,20),name='staticText')
        self.text.SetBackgroundColour('Green')
        self.text.SetForegroundColour('Forest Green')
        self.panel.Refresh()

    def closeWindow(self,event):
        pass

    def leftDown(self,event):
        print "left down..."
        event.Skip()

    def countDownFunc(self,event):
        for i in range(10):
            current = str(10 - i)
            self.text.SetLabel("time : "+current)
            time.sleep(1)

    def enterWindowLeft(self,event):
        self.btnLeft.SetLabel('Lok\' Tar')
        self.btnLeft.SetBackgroundColour('Cyan')
    def leaveWindowLeft(self,event):
        self.btnLeft.SetLabel('Orgar!')
        self.btnLeft.SetBackgroundColour('Medium Turquoise')

    def enterWindowRight(self,event):
        self.btnRight.SetLabel('Glory')
        self.btnRight.SetBackgroundColour('Cyan')
    def leaveWindowRight(self,event):
        self.btnRight.SetLabel('For Sin\'dorei!')
        self.btnRight.SetBackgroundColour('Medium Turquoise')

class MyApp(wx.App):
    def __init__(self,redirect = False,filename =None):
        wx.App.__init__(self,redirect,filename)

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        #self.countDown(self.frame)
        return True
    def countDown(self,frame):
        frame.countDownFunc()

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()