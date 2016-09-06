import wx
import login
import common as cmm
import fonts

class costDataFrame(wx.Frame):
    def __init__(self,parent=None,id=-1,title="Add Cost",pos=(350,150),size=(400,300),costName=""):
        wx.Frame.__init__(self,parent,id,title,pos,size)

        (sizer,self.textDict) = cmm.createStaticTextControl(self,self.costDataInfo(costName),fonts.Fonts.romanBold12())
        print "dict : ",self.textDict
        buttonSizer = self.costDataButtons()
        #self.SetSizer(sizer)
        self.SetBackgroundColour("White")
        self.layout(sizer,buttonSizer)


    def layout(self,textSizer,buttonSizer):
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(textSizer,4,wx.EXPAND)
        mainSizer.Add(buttonSizer,1,wx.EXPAND)
        self.SetSizer(mainSizer)

    def customizeSizer(self,sizer):
        for item in sizer:
            item.SetFont(fonts.Fonts.romanBold14())
            item.SetForegroundColour('Blue')

    def costDataInfo(self,costName):
        return [("Cost Name : ",wx.ROMAN,'static'),
                (costName,wx.ROMAN,'static'),
                ("Value : ",wx.ROMAN,'static'),
                (wx.TE_NOHIDESEL,'ctrl'),
                ("Comments : ",wx.ROMAN,'static'),
                (wx.TE_MULTILINE,'ctrl')]

    def costDataButtons(self):
        costDataSizer = wx.BoxSizer(wx.HORIZONTAL)

        costDataBtnAdd = wx.Button(self,label="Add",size=(100,50))
        self.Bind(wx.EVT_BUTTON,self.onAddCost,costDataBtnAdd)

        costDataBtnCancel = wx.Button(self,label="Cancel",size=(100,50))
        self.Bind(wx.EVT_BUTTON,self.onCancel,costDataBtnCancel)

        costDataSizer.Add(costDataBtnAdd,1,wx.ALIGN_BOTTOM|wx.EXPAND,10)
        costDataSizer.Add((50,0))
        costDataSizer.Add(costDataBtnCancel,1,wx.ALIGN_BOTTOM|wx.EXPAND,10)
        return costDataSizer

    def onAddCost(self,event):
        pass
    def onCancel(self,event):
        self.Destroy()

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