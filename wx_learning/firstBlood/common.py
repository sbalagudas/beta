import wx
import time
import enDecryption as ed
import DBOperation

def createStaticTextControl(parent,textInfo,font):
    sizer = wx.FlexGridSizer(cols=2,hgap=6,vgap=6)
    textList = []
    for eachItem in textInfo:
        if 'static' in eachItem :
            text = wx.StaticText(parent,id=-1,label=eachItem[0],style=eachItem[1]|wx.ALIGN_CENTER)
        else :
            text = wx.TextCtrl(parent,id=-1,size=(250,-1),style=eachItem[0])
        textList.append(text)
        text.SetFont(font)
        sizer.Add(text,0,wx.EXPAND|wx.ALL,10)
    return sizer,textList

def getTimeAndWeek():
    itf = "%Y-%m-%d %H:%M:%S"
    return (time.strftime(itf,time.localtime()),time.strftime("%W"))

def getAndConvert(sqlCommand):
    dbo = DBOperation.DBOperation()
    rawData = dbo.customizedFetch(sqlCommand)
    print "raw data : ",rawData
    gridData = []
    gridLabel = []
    for item in rawData :
        item = list(item)
        print "item :",item
        for i in range(1,4):
            print "item before : ",item[i]
            item[i]= ed.enDecryption.decryption(item[i].strip())
            print "item after : ",item[i]
            gridData.append(item[1:3])
            gridLabel.append(item[len(item)-1:])
    print "gridData : ",gridData
    print "gridLabel : ",gridLabel
    return gridData,gridLabel



