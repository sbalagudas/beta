import DBOperation
import common as cmm

class dateFilter():
    @classmethod
    def getAllRawData(self):
        cleanedTimeList = []
        dbo = DBOperation.DBOperation()
        try :
            dbo.fetchAllData('cost')
            (gridData,gridLabel) = cmm.getAndConvertCostData(("","","",))
        except :
            gridLabel = ""

        for item in gridLabel:
            #print "item : >%s<"%item
            cleanedTimeList.append(item[:item.rfind(' ')])

        cleanedTimeList = list(set(cleanedTimeList))
        #print "cleanedTimeList : ",cleanedTimeList
        return cleanedTimeList

    @classmethod
    def getTimeList(self):
        timeList = self.getAllRawData()
        if 0 == len(timeList):
            return 0
        mainTimeDict = {}

        for item in timeList:
            year = item[:4]
            month = item[5:7]
            day = item[8:10]

            #print "---------------------------------------------------"
            #print "year : ",year
            #print "month : ",month
            #print "day : ",day
            #print "---------------------------------------------------"

            if not mainTimeDict.has_key(year):
                #print "<year> : <%s> don't exist in list %s,creating..."%(year,mainTimeDict)
                mainTimeDict[year]={}
            if not mainTimeDict[year].has_key(month):
                #print "<month> : <%s> don't exist in list %s, creating..."%(month,mainTimeDict[year])
                mainTimeDict[year][month]=[]

            if day not in mainTimeDict[year][month]:
                #print "key <day> : <%s> not in list %s, append!"%(day,mainTimeDict[year][month])
                mainTimeDict[year][month].append(day)
                #not recommended for this sort. but if data mount is not huge, it is ok.
                mainTimeDict[year][month].sort()
            else :
                #print "key <day> : <%s> is in list %s, abort!"%(day,mainTimeDict[year][month])
                continue

        #print "mainTimeDict : ",mainTimeDict
        return mainTimeDict


#data = dateFilter.getAllRawData()
#timeList = dateFilter.getTimeList(data)






