import wx
import time

class timeDisplay(wx.Panel):
    def __init__(self,parent,id,curUser):
        wx.Panel.__init__(self,parent,id)
        self.fontBold = wx.Font(16,wx.ROMAN,wx.ITALIC,wx.BOLD)
        self.fontBold1 = wx.Font(20,wx.ROMAN,wx.ITALIC,wx.BOLD)
        self.curUser = curUser
        self.curTime = self.getTimeAndWeek()

        self.createStaticText()
        self.refreshTime()

    def TextInfo(self):
        week = self.getTimeAndWeek()
        week = week[1]
        return ["Hi,",self.curUser,"Today is ",self.curTime[0],"Week ",week]

    def createStaticText(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.textList = []
        i = 0
        for eachItem in self.TextInfo():
            text = wx.StaticText(self,id=-1,label=str(eachItem),style=wx.ROMAN)
            text.SetFont(self.fontBold)
            if 0 == i%2:
                text.SetForegroundColour('Blue')
                sizer.Add((25,0))
            else :
                text.SetForegroundColour('Red')
            i = i + 1
            sizer.Add(text,0,wx.EXPAND|wx.ALL,5)
            self.textList.append(text)
            self.SetSizer(sizer)
            sizer.Fit(self)

    def refreshTime(self):
        while True:
            self.curTime = self.getTimeAndWeek()[0]
            print "current time : ",self.curTime
            print "self.textList[3]",self.textList[3]
            self.textList[3].SetLabel(str(self.curTime))
            time.sleep(1)

    def timeZoneLayout(self,greeting,timeBox):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(greeting,1)
        sizer.Add(timeBox,1)
        self.SetSizer(sizer)

    def getTimeAndWeek(self):
        itf = "%Y-%m-%d %H:%M:%S"
        return (time.strftime(itf,time.localtime()),time.strftime("%W"))

class timeFrame(wx.Frame):
    def __init__(self,parent=None,id=-1,title="time display",size=(800,600)):
        wx.Frame.__init__(self,parent,id,title,size)

        self.panel = timeDisplay(self,-1,"tester")

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = timeFrame()
    frame.Show()
    app.MainLoop()