import wx
import time

class btnFrame(wx.Frame):
    def __init__(self,parent,id,title,pos=wx.DefaultPosition,size=(220,220)):
        wx.Frame.__init__(self,parent,id,title,pos,size)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('Yellow')
        self.button = wx.Button(self.panel,label="Banana",pos=(50,50),size=(100,100))
        self.button.SetBackgroundColour('Grey')
        self.Bind(wx.EVT_BUTTON,self.buttonClick,self.button,self.button)
        self.button.Bind(wx.EVT_ENTER_WINDOW,self.buttonOver,self.button)
        self.button.Bind(wx.EVT_ENTER_WINDOW,self.buttonOver1,self.button)
        self.button.Bind(wx.EVT_LEAVE_WINDOW,self.buttonLeave,self.button)
        self.button.Bind(wx.EVT_LEFT_DCLICK,self.dcClick,self.button)
        #self.button.Create(self,parent = None,id=11,label="fox",pos=wx.DefaultPosition,size=(30,30))
        #self.button.Bind(wx.EVT_MOUSE_EVENTS,self.printAll)

    def buttonClick(self,event):
        self.panel.SetBackgroundColour('Dark Green')
        self.panel.Refresh()
    def buttonOver1(self,event):
        self.panel.SetBackgroundColour('Purple')
        self.panel.Refresh()
        event.Skip()
    def buttonOver(self,event):
        self.button.SetLabel("Apple")
        self.button.SetBackgroundColour('Pink')
        event.Skip()
    def buttonLeave(self,event):
        self.button.SetLabel("Banana")
        self.button.SetBackgroundColour('Grey')
        self.panel.SetBackgroundColour('Yellow')
        self.panel.Refresh()
        event.Skip()
    def dcClick(self,event):
        self.panel.SetBackgroundColour("Green")
        self.panel.Refresh()
    def printAll(self,event):
        print "deal with all mouse events..."

    def blingBling(self,event):
        for i in range(10):
            self.panel.SetBackgroundColour('Yellow')
            self.panel.Refresh()
            time.sleep(1)
            self.panel.SetBackgroundColour('Purple')
            self.panel.Refresh()
            time.sleep(1)
        event.Skip()

class btnApp(wx.App):
    def __init__(self,redirect=False,filename=None):
        wx.App.__init__(self,redirect,filename)

    def OnInit(self):
        self.frame = btnFrame(None,-1,"test")
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == "__main__":
    app = btnApp()
    app.MainLoop()