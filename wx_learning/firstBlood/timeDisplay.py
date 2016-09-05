import wx
import time
import threading
from paint import Paint as pt

class timeDisplay(wx.Panel):
    def __init__(self,parent,id,curUser):
        wx.Panel.__init__(self,parent,id)
        self.fontBold = wx.Font(16,wx.ROMAN,wx.ITALIC,wx.BOLD)
        self.fontBold1 = wx.Font(20,wx.ROMAN,wx.ITALIC,wx.BOLD)
        self.curUser = curUser
        self.curTime = self.getTimeAndWeek()

        #multi-threading
        thd = threading.Thread(target=self.refreshTime,args=())
        self.createStaticText()
        thd.start()

    def TextInfo(self):
        week = self.getTimeAndWeek()
        week = week[1]
        return [self.curUser,self.curTime[0],"Week   "+str(week)]

    def titleColorInfo(self):
        return ["DARK TURQUOISE","AQUAMARINE","MEDIUM TURQUOISE"]

    def createStaticText(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.textList = []
        i = 0
        for eachItem in self.TextInfo():
            text = wx.StaticText(self,id=-1,label=str(eachItem),style=wx.ROMAN)
            text.SetForegroundColour('Blue')
            text.SetBackgroundColour(self.GetBackgroundColour())
            #text.SetBackgroundColour('White')
            text.SetFont(self.fontBold)

            if 1 == i:
                sizer.Add(text,2,wx.EXPAND)
            else :
                sizer.Add(text,1,wx.EXPAND)
            i += 1
            self.textList.append(text)
        self.SetSizer(sizer)
        sizer.Layout()
        #sizer.Fit(self)

    def refreshTime(self):
        while True:
            self.curTime = self.getTimeAndWeek()[0]
            self.textList[1].SetLabel(str(self.curTime))
            time.sleep(1)

    def timeZoneLayout(self,greeting,timeBox):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(greeting,1)
        sizer.Add(timeBox,1)
        #self.SetSizer(sizer)

    def getTimeAndWeek(self):
        itf = "%Y-%m-%d %H:%M:%S"
        return (time.strftime(itf,time.localtime()),time.strftime("%W"))

class timeFrame(wx.Frame):
    def __init__(self,parent=None,id=-1,title="time display",pos=(0,0),size=(800,600)):
        wx.Frame.__init__(self,parent,id,title,pos,size)

        self.panelTime = timeDisplay(self,-1,"tester")
        self.panelTime.SetBackgroundColour('White')

        #timeSizer = self.panelTime.createStaticText()
        self.paintWindow = pt(self,-1)

        mainBox = wx.BoxSizer(wx.VERTICAL)
        mainBox.Add(self.panelTime,1,wx.EXPAND)
        mainBox.Add(self.paintWindow,10,wx.EXPAND)

        self.SetSizer(mainBox)



if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = timeFrame()
    frame.Show()
    app.MainLoop()