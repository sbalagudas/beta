import sqlite3 as sql
import time
import enDecryption as ed


class DBOperation(object) :
    DB_DIR = "d:\\dbTest.db"
    def __init__(self):
        self.conn = sql.connect(self.DB_DIR)
        self.cursor = self.conn.cursor()
        self.createTable('user')
        self.createTable('cost')
    #@staticmethod
    def closeConnection(self,conn):
        conn.close()


    TBUserInfo = " (userId INTEGER PRIMARY KEY AUTOINCREMENT, " \
                 "userName VARCHAR(20)," \
                 "password VARCHAR(30)," \
                 "regDate DATETIME)"
    TBCostInfo = " (costId INTEGER PRIMARY KEY AUTOINCREMENT," \
                 "costName VARCHAR(20)," \
                 "costValue FLOAT," \
                 "comments VARCHAR(100)," \
                 "costDate DATETIME)"

    #@staticmethod
    def createTable(self,tableName):
        if tableName == 'user' :
            createTBCommand = "CREATE TABLE IF NOT EXISTS "+ str(tableName)+ self.TBUserInfo
        elif tableName == 'cost':
            createTBCommand = "CREATE TABLE IF NOT EXISTS "+ str(tableName)+ self.TBCostInfo
        self.cursor.execute(createTBCommand)

    #@staticmethod
    def dropTable(self,tableName):
        removeTBCommand = "DROP TABLE "+ str(tableName)
        self.cursor.execute(removeTBCommand)

    #@staticmethod
    def insertData(self,tableName,value):
        insertCommand = ""
        if "user" == tableName :
            insertCommand = "INSERT INTO " + str(tableName) + " (username,password,regDate)" + " values (?,?,?)"
        elif "cost" == tableName :
            insertCommand = "INSERT INTO " + str(tableName) + " (costName,costValue,comments,costDate)" + " values (?,?,?,?)"
        self.cursor.execute(insertCommand,value)
        print "[DBO.insertData] : command <%s> executed...[ %s ]"%(insertCommand,value)
        self.conn.commit()

    #@staticmethod
    def fetchAllData(self,tableName):
        fetchAllCommand = "SELECT * FROM "+tableName
        self.cursor.execute(fetchAllCommand)
        self.cursor.execute(fetchAllCommand)
        return self.cursor.fetchall()

    #@staticmethod
    def customizedFetch(self,cmd):
        self.cursor.execute(cmd)
        print "command <%s> executed !"%cmd
        return self.cursor.fetchall()
    #@classmethod
    def getBanana(self,key):
        getBananaCommand = "SELECT password FROM user WHERE userName='"+str(key)+"'"
        #print "command <%s> executed !"%getBananaCommand
        self.cursor.execute(getBananaCommand)
        raw = self.cursor.fetchall()
        #print "raw : ",raw
        return raw

if __name__ == "__main__":
    #pass

    itf = "%Y-%m-%d %H:%M:%S"
    dbo = DBOperation()

    userInfo = [('apple','apple123',"2016-01-01 12:12:12"),
                ('pear','pear123',"2016-01-02 12:12:12"),
                ('banana','banana123',"2016-01-03 12:12:12"),
                ('peach','peach123',"2016-01-02 14:14:14")]
    values=[('lunch',11,'aaa','2015-01-10 12:12:12'),
            ('lunch',11,'aaa','2015-01-11 12:12:12'),
            ('lunch',11,'aaa','2015-01-12 12:12:12'),
            ('lunch',11,'aaa','2015-01-13 12:12:12'),
            ('lunch',11,'aaa','2015-02-10 12:12:12'),
            ('lunch',11,'aaa','2015-02-11 12:12:12'),
            ('lunch',11,'aaa','2015-02-12 12:12:12'),
            ('lunch',11,'aaa','2015-02-13 12:12:12'),
            ('lunch',11,'aaa','2015-03-10 12:12:12'),
            ('lunch',11,'aaa','2015-04-14 12:12:12'),
            ('lunch',11,'aaa','2015-04-15 12:12:12'),
            ('lunch',11,'aaa','2015-05-17 12:12:12'),
            ('lunch',11,'aaa','2015-05-17 12:12:12'),
            ('lunch',11,'aaa','2015-05-19 12:12:12'),
            ('lunch',11,'aaa','2015-06-01 12:12:12'),
            ('lunch',11,'aaa','2015-06-03 12:12:12'),
            ('lunch',11,'aaa','2015-06-11 12:12:12'),
            ('lunch',11,'aaa','2015-06-29 12:12:12'),
            ('lunch',11,'aaa','2015-07-21 12:12:12'),
            ('lunch',11,'aaa','2015-07-22 12:12:12'),
            ('lunch',11,'aaa','2015-08-10 12:12:12'),
            ('lunch',11,'aaa','2015-10-10 12:12:12'),
            ('lunch',11,'aaa','2015-10-10 12:12:12'),
            ('lunch',11,'aaa','2015-12-10 12:12:12'),
            ('lunch',11,'aaa','2015-12-18 12:12:12'),
            ('snack',22,'bbb','2016-01-10 13:13:13'),
            ('lunch',11,'aaa','2016-01-19 12:12:12'),
            ('lunch',11,'aaa','2016-01-26 12:12:12'),
            ('lunch',11,'aaa','2016-02-03 12:12:12'),
            ('lunch',11,'aaa','2016-02-11 12:12:12'),
            ('lunch',11,'aaa','2016-02-29 12:12:12'),
            ('lunch',11,'aaa','2017-07-21 12:12:12'),
            ('lunch',11,'aaa','2017-07-22 12:12:12'),
            ('lunch',11,'aaa','2017-08-10 12:12:12'),
            ('lunch',11,'aaa','2017-10-10 12:12:12'),
            ('lunch',11,'aaa','2017-10-10 12:12:12'),
            ('lunch',11,'aaa','2017-12-10 12:12:12'),
            ('lunch',11,'aaa','2017-12-18 12:12:12')]

##########################
    #dbo.dropTable('cost')
    #dbo.createTable('cost')
##########################

    #dbo.createTable('user')
    dbo.createTable('cost')
    #for item in userInfo:
    #    dbo.insertData('user',item)
    #r = dbo.fetchAllData('user')
    #print "user information : \n %s"%r
    #print "-------------------------------"

    #for value in values :
    #    tmp = []
    #    for item in value:
    #        var = ed.enDecryption.encryption(str(item))
    #        tmp.append(var)
    #    dbo.insertData('cost',tmp)
    #c = dbo.fetchAllData('cost')
    #print c
    #print "cost information : \n %s"%c


    cmd1 = "SELECT costDate,costName,costValue,comments FROM cost"
    cmd2 = "SELECT * FROM cost WHERE costDate LIKE '2016-09-07%'"
    #cmd3 = "SELECT * FROM cost WHERE costDate LIKE '2016-01-10 13:13%'"
    a = dbo.customizedFetch(cmd1)
    result = []
    result1 = []
    for item in a :
        item = list(item)
        print "listed item : ",item
        for i in range(len(item)):
            #print "item["+str(i)+"] before: ",item[i]
            item[i] = ed.enDecryption.decryption(item[i])
            #print "item["+str(i)+"] after : ",item[i]
        result.append(item)
    print "result : ",result
'''
    b = dbo.customizedFetch(cmd2)
    for item in b :
        item = list(item)
        for i in range(1,4):
            item[i]= ed.enDecryption.decryption(item[i])
            result1.append(item)

    print "result : ",result
    print "result1 : ",result1
    #a = ed.enDecryption.decryption(b)
    #c = dbo.customizedFetch(cmd3)
    #print "a : ",a
    #print "b : ",b
    #print "c : ",c
'''









