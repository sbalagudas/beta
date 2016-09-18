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

def getAndConvert():
    dbo = DBOperation.DBOperation()
    #rawData = dbo.customizedFetch(sqlCommand)
    rawData = dbo.fetchAllData('cost')
    #print "raw data : ",rawData
    gridData = []
    gridLabel = []
    result1 = []

    for item in rawData :
        item = list(item)
        #print "listed item : ",item
        for i in range(1,len(item)):
            item[i] = ed.enDecryption.decryption(item[i])
        gridData.append(item[1:-1])
        gridLabel.append(item[-1:][0])
    #print "result : ",gridData
    #print "gridLabel : ",gridLabel
    return gridData,gridLabel

def unicodeToUTF(string):
    return unicode.encode(string)



