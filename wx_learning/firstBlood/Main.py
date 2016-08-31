import wx
import login
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
    def __init__(self,parent=None,id=wx.ID_ANY,title="Banana World"):
        wx.Frame.__init__(self,parent,id,title)

        #self.panel = testPanel(self,-1)
        self.panel = wx.Panel(self,-1)
        self.test = wx.StaticText(self.panel,id=1,label="testing",style=wx.ROMAN)



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

