import wx
import timeDisplay
from paint import Paint as pt
import time

class testPanel(wx.Panel):
    def __init__(self,parent,id=-1):

        self.createText()
        #self.frame = parent

    def createText(self):
        self.test = wx.StaticText(self,id=1,label="testing",style=wx.ROMAN)
        time.sleep(1)
        self.test.SetLabel("banana")



class mainFrame(wx.Frame):
    def __init__(self,parent=None,id=wx.ID_ANY,title="Banana World",pos=(0,0),size=(800,600)):
        wx.Frame.__init__(self,parent,id,title,pos,size)

        self.panelTime = timeDisplay.timeDisplay(self,-1,'apple')
        self.panelPaint = pt(self,-1)

        self.layout(self.panelTime,self.panelPaint)

    def layout(self,time,paint):

        mainBox = wx.BoxSizer(wx.VERTICAL)
        mainBox.Add(time,1,wx.EXPAND)
        mainBox.Add(paint,5,wx.EXPAND)

        self.SetSizer(mainBox)
        #mainBox.Fit(self)



class mainApp(wx.App):
    def __init__(self,redirect=False,filename=None):
        wx.App.__init__(self,redirect,filename)
    def OnInit(self):
        frame = mainFrame()
        frame.Show()

        #self.loginWindow = login.logInFrame()
        #self.SetTopWindow(self.loginWindow)
        #self.loginWindow.Show()
        return True

if __name__ == "__main__":
    mApp = mainApp()
    mApp.MainLoop()

