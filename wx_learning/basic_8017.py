import wx
import paint as pt

class logInFrame(wx.Frame):
    def __init__(self,parent=None,id=-1,title="My Frame"):
        wx.Frame.__init__(self,parent,id,title)

        self.paintWindow = wx.Panel(self,-1)
        self.paintWindow.SetBackgroundColour("TURQUOISE")

        self.fontBold = wx.Font(18,wx.ROMAN,wx.ITALIC,wx.BOLD)
        bgColor = self.paintWindow.GetBackgroundColour()

        self.userNameText = wx.StaticText(self.paintWindow,-1,label="User Name : ",pos=(200,-1),style=wx.ROMAN)
        self.userNameText.SetFont(self.fontBold)
        self.userNameInput = wx.TextCtrl(self.paintWindow,-1,size=(200,-1),style=wx.TE_NOHIDESEL|wx.TE_PROCESS_ENTER)
        self.userNameInput.SetFont(self.fontBold)
        self.userNameInput.SetBackgroundColour(bgColor)

        self.userPwdText = wx.StaticText(self.paintWindow,-1,label="Password : ",style=wx.ROMAN)
        self.userPwdText.SetFont(self.fontBold)
        self.userPwdInput = wx.TextCtrl(self.paintWindow,-1,size=(200,-1),style=wx.TE_PASSWORD|wx.TE_NOHIDESEL)
        self.userPwdInput.SetBackgroundColour(bgColor)
        self.userPwdInput.SetFont(self.fontBold)

        sizer = wx.FlexGridSizer(cols=2,hgap=6,vgap=6)
        sizer.AddMany([self.userNameText,self.userNameInput,self.userPwdText,self.userPwdInput])
        self.paintWindow.SetSizer(sizer)
        sizer.Fit(self)
        #mainSizer = wx.BoxSizer(wx.VERTICAL)
        #mainSizer.Add(userNameSizer)
        #mainSizer.Add(userPwdSizer)
        #self.paintWindow.SetSizer(mainSizer)

        #userNameSizer.Fit(self)
        #self.SetSizer(userNameSizer)


if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = logInFrame()
    frame.Show()
    app.MainLoop()