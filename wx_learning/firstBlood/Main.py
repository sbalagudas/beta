import wx
import timeDisplay
#from paint import Paint as pt
import costPanel as cP
import login
import time

class mainFrame(wx.Frame):
    def __init__(self,parent=None,id=wx.ID_ANY,title="Banana World",pos=(0,0),size=(800,600)):
        wx.Frame.__init__(self,parent,id,title,pos,size)

        self.panelTime = timeDisplay.timeDisplay(self,-1,'apple')
        #self.panelPaint = pt(self,-1)
        self.cost = cP.costPanel(self,-1)
        self.tstPanel = cP.testPanel(self,-1)
        self.tstPanel.SetBackgroundColour('White')
        self.layout(self.panelTime,self.cost,self.tstPanel)


    def layout(self,time,cP,tst):
        subBox = wx.BoxSizer(wx.HORIZONTAL)
        subBox.Add(cP,0)
        subBox.Add(tst,1,wx.EXPAND)

        mainBox = wx.BoxSizer(wx.VERTICAL)
        mainBox.Add(time,1,wx.EXPAND)
        mainBox.Add(subBox,10,wx.EXPAND)

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

