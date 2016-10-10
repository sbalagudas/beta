import wx
import login
import common as cmm
import fonts
import DBOperation as dbo
import enDecryption as ed

class costDataFrame(wx.Frame):
    def __init__(self,parent=None,id=-1,title="Add Cost",pos=(350,150),size=(400,300),costName="",style=wx.STAY_ON_TOP):
        wx.Frame.__init__(self,parent,id,title,pos,size)
        self.costNameForDB = costName
        (sizer,self.textList) = cmm.createStaticTextControl(self,self.costDataInfo(costName),fonts.Fonts.romanBold12())
        self.textList[3].SetBackgroundColour('#CCFFCC')
        self.textList[5].SetBackgroundColour('#CCFFCC')
        self.textList[5].SetBackgroundColour('#CCFFCC')
        for i in range(0,6):
            self.textList[i].SetForegroundColour('Blue')
        self.textList[6].SetForegroundColour('Red')
        buttonSizer = self.costDataButtons()
        self.SetBackgroundColour("White")
        self.SetBackgroundColour('#CCFFCC')
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
                (wx.TE_MULTILINE,'ctrl'),
                ("",wx.ALIGN_CENTER,'static')]

    def costDataButtons(self):
        costDataSizer = wx.BoxSizer(wx.HORIZONTAL)

        costDataBtnAdd = wx.Button(self,label="Add",size=(100,50))
        costDataBtnAdd.SetForegroundColour('Blue')
        costDataBtnAdd.SetBackgroundColour('#CCFFCC')
        costDataBtnAdd.SetFont(fonts.Fonts.romanBold12())
        self.Bind(wx.EVT_BUTTON,self.onAddCost,costDataBtnAdd)

        costDataBtnCancel = wx.Button(self,label="Cancel",size=(100,50))
        self.Bind(wx.EVT_BUTTON,self.onCancel,costDataBtnCancel)
        costDataBtnCancel.SetForegroundColour('Blue')
        costDataBtnCancel.SetBackgroundColour('#CCFFCC')
        costDataBtnCancel.SetFont(fonts.Fonts.romanBold12())

        costDataSizer.Add(costDataBtnAdd,1,wx.ALIGN_BOTTOM|wx.EXPAND,10)
        costDataSizer.Add((50,0))
        costDataSizer.Add(costDataBtnCancel,1,wx.ALIGN_BOTTOM|wx.EXPAND,10)
        return costDataSizer

    def onAddCost(self,event):
        value = self.textList[3].GetLabelText()
        comments = self.textList[5].GetLabelText()
        if '.' in str(value):
            value = value[:str(value).rfind('.')]
        if not str(value).isdigit() or 0 == len(str(value)):
            self.textList[6].SetLabel("value should be numbers...")

        else :
            name = ed.enDecryption.encryption(self.costNameForDB)
            value = ed.enDecryption.encryption(value)
            comments = ed.enDecryption.encryption(comments)
            curTime = cmm.getTimeAndWeek()[0]

            insertValue = (name,value,comments,curTime)

            db = dbo.DBOperation()
            db.insertData('cost',insertValue)
            self.Destroy()

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