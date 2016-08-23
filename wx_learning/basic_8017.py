import wx
import paint as pt

class logInPanel(wx.Panel):
    #def __init__(self,parent=None,id=-1,title="My Frame"):
    #    wx.Frame.__init__(self,parent,id,title)
    def __init__(self,parent,ID,pos=wx.DefaultPosition,size=(600,400),style=wx.RAISED_BORDER):
        wx.Panel.__init__(self,parent,ID,pos,size,style)

        #self.paintWindow = wx.Panel(self,-1)

        self.SetBackgroundColour("TURQUOISE")
        self.fontBold = wx.Font(18,wx.ROMAN,wx.ITALIC,wx.BOLD)
        self.bgColor = self.GetBackgroundColour()

        self.createLoginButton()
        textSizer = self.createText()
        self.layout(textSizer)

    def createLoginButton(self):
        self.loginBtn = wx.Button(self,label="Log In",size=(100,50))
        self.loginBtn.SetFont(self.fontBold)

    def textInfo(self):
        return [("User Name : ",wx.ROMAN,'static'),
                (wx.TE_NOHIDESEL,'ctrl'),
                ("Password : ",wx.ROMAN,'static'),
                (wx.TE_PASSWORD,'ctrl')]

    def layout(self,textSizer):
        boxSizer = wx.BoxSizer(wx.VERTICAL)
        boxSizer.Add(textSizer,1,wx.EXPAND|wx.ALL,5)
        boxSizer.Add(self.loginBtn,0,wx.ALIGN_CENTER|wx.ALL,5)

        self.SetSizer(boxSizer)
        self.Layout()

    def createText(self):
        sizer = wx.FlexGridSizer(cols=2,hgap=6,vgap=6)
        textList = []
        for eachItem in self.textInfo():
            if 'static' in eachItem :
                text = wx.StaticText(self,id=-1,label=eachItem[0],style=eachItem[1])
                text.SetForegroundColour('BLUE')
            else :
                text = wx.TextCtrl(self,id=-1,size=(200,-1),style=eachItem[0])
                text.SetForegroundColour('BLACK')
            text.SetFont(self.fontBold)
            text.SetBackgroundColour(self.bgColor)
            textList.append(text)
        sizer.AddMany(textList)
        #self.paintWindow.SetSizer(sizer)
        return sizer

class logInFrame(wx.Frame) :
    def __init__(self,parent=None,id=-1,title="log in window"):
        wx.Frame.__init__(self,parent,id,title)

        self.panel = logInPanel(self,-1)

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = logInFrame()
    frame.Show()
    app.MainLoop()