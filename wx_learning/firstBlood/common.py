import wx
import time
import enDecryption as ed
import DBOperation
import fonts

def createStaticTextControl(parent,textInfo,font):
    sizer = wx.FlexGridSizer(cols=2,hgap=6,vgap=6)
    textList = []
    for eachItem in textInfo:
        if 'static' in eachItem :
            text = wx.StaticText(parent,id=-1,label=eachItem[0],style=eachItem[1]|wx.ALIGN_CENTER)
        else :
            text = wx.TextCtrl(parent,id=-1,size=(250,-1),style=eachItem[0])
        textList.append(text)
        text.SetFont(fonts.Fonts.swissArial10())
        sizer.Add(text,0,wx.EXPAND|wx.ALL,10)
    return sizer,textList

def getTimeAndWeek():
    itf = "%Y-%m-%d %H:%M:%S"
    return (time.strftime(itf,time.localtime()),time.strftime("%W"))

def makeCommand(dateDetail):
    if dateDetail[0] != "" :
        if dateDetail[1] !=  "" :
            if dateDetail[2] != "" :
                return "SELECT * FROM cost WHERE costDate LIKE \'"+str(dateDetail[0])+"-"+str(dateDetail[1])+"-"+str(dateDetail[2])+"%\'"
            else :
                return "SELECT * FROM cost WHERE costDate LIKE \'"+str(dateDetail[0])+"-"+str(dateDetail[1])+"%\'"
        else :
            return "SELECT * FROM cost WHERE costDate LIKE \'"+str(dateDetail[0])+"%\'"

    else :
        return "SELECT * FROM cost"

def getAndConvertCostData(dateDetail):
    dbo = DBOperation.DBOperation()
    #rawData = dbo.customizedFetch(sqlCommand)
    #rawData = dbo.fetchAllData('cost')
    cmd = makeCommand(dateDetail)
    rawData = dbo.customizedFetch(cmd)

    (gridData,gridLabel) = decryptionList(rawData)
    return gridData,gridLabel

def decryptionList(rawData):
    #print "raw data : ",rawData
    gridData = []
    gridLabel = []

    for item in rawData :
        item = list(item)
        #print "listed item : ",item
        for i in range(1,len(item)-1):
            item[i] = ed.enDecryption.decryption(item[i])
        gridData.append(item[1:-1])
        gridLabel.append(item[-1:][0])
    #print "result : ",gridData
    #print "gridLabel : ",gridLabel
    return gridData,gridLabel

def unicodeToUTF(string):
    return unicode.encode(string)

def calculatingTotalCost(costList):
    moneyList = []
    #print "costList : ",costList
    for item in costList:
        #print "item : ",item
        moneyList.append(int(item[1]))
    return sum(moneyList)
def getCurUser():
    command = "select * from user"
    pass

