import wx
import login

class costDataFrame(wx.Frame):
    def __init__(self,parent=None,id=-1,title="Add Cost",pos=wx.DefaultPosition,size=(400,500)):
        wx.Frame.__init__(self,parent,id,title,pos,size)
        (sizer,textList) = login.logInPanel.createText(self.costDataInfo())

    def costDataInfo(self):
        return ["Cost Name","Value","Comments"]

class costDataApp(wx.App):
    def __init__(self,redirect=False,filename=None):
        wx.App.__init__(self,redirect,filename)
    def OnInit(self):
        self.frame = costDataFrame()
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == '__main__':
    app = costDataApp()
    app.MainLoop()