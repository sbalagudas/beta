import wx
import time


def createStaticTextControl(parent,textInfo,font):
    sizer = wx.FlexGridSizer(cols=2,hgap=6,vgap=6)
    #horSizer = wx.BoxSizer(wx.HORIZONTAL)
    #verSizer = wx.BoxSizer(wx.VERTICAL)

    #textDict = {}
    textList = []
    for eachItem in textInfo:
        if 'static' in eachItem :
            text = wx.StaticText(parent,id=-1,label=eachItem[0],style=eachItem[1]|wx.ALIGN_CENTER)
        else :
            text = wx.TextCtrl(parent,id=-1,size=(250,-1),style=eachItem[0])
        textList.append(text)
        text.SetFont(font)
        sizer.Add(text,0,wx.EXPAND|wx.ALL,10)

        #textDict[text.GetId()] = eachItem

    #sizer.AddMany(textList)
    #self.paintWindow.SetSizer(sizer)
    return sizer,textList

def getTimeAndWeek():
    itf = "%Y-%m-%d %H:%M:%S"
    return (time.strftime(itf,time.localtime()),time.strftime("%W"))
