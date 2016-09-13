import DBOperation
import common as cmm

def getAllRawData():
    dbo = DBOperation.DBOperation()
    dbo.fetchAllData('cost')
    cmm.getAndConvert()