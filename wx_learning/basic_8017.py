import wx
import paint as pt

class logInFrame(wx.Frame):
    def __init__(self,parent=None,id=-1,title="My Frame"):
        wx.Frame.__init__(self,parent,id,title)

        self.paintWindow = wx.Panel(self,-1)
        self.paintWindow.SetBackgroundColour("TURQUOISE")
        self.fontBold = wx.Font(18,wx.ROMAN,wx.ITALIC,wx.BOLD)
        self.bgColor = self.paintWindow.GetBackgroundColour()

        self.createText()
    def textInfo(self):
        return [("User Name : ",wx.ROMAN,'static'),
                (wx.TE_NOHIDESEL,'ctrl'),
                ("Password : ",wx.ROMAN,'static'),
                (wx.TE_PASSWORD,'ctrl')]

    def createText(self):
        sizer = wx.FlexGridSizer(cols=2,hgap=6,vgap=6)
        textList = []
        for eachItem in self.textInfo():
            if 'static' in eachItem :
                text = wx.StaticText(self.paintWindow,id=-1,label=eachItem[0],style=eachItem[1])
                text.SetForegroundColour('BLUE')
            else :
                text = wx.TextCtrl(self.paintWindow,id=-1,size=(200,-1),style=eachItem[0])
                text.SetForegroundColour('BLACK')
            text.SetFont(self.fontBold)
            text.SetBackgroundColour(self.bgColor)
            textList.append(text)
        sizer.AddMany(textList)
        self.paintWindow.SetSizer(sizer)

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = logInFrame()
    frame.Show()
    app.MainLoop()