import sqlite3 as sql
import common as cmm
import enDecryption as ed


class DBOperation(object) :
    DB_DIR = "d:\\dbTest.db"
    def __init__(self):
        try :
            self.conn = sql.connect(self.DB_DIR)
        except Exception as e:
            print e
        self.cursor = self.conn.cursor()
        self.createTable('user')
        #self.createTable('cost')
        #self.initialization()
    #@staticmethod

    def initialization(self):
        banana = 'sophia'
        apple = 'xfgcj1314'
        banana = ed.enDecryption.encryption(banana)
        apple = ed.enDecryption.encryption(apple)
        banana.strip()
        apple.strip()
        t = cmm.getTimeAndWeek()[0]
        initCommand = "INSERT INTO user(username,password,regDate) SELECT \'"+banana+"\',\'"+apple+"\',\'"+t+"\' WHERE NOT EXISTS (SELECT * FROM user WHERE username=\'"+banana+"\')"
        return initCommand


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
        try :
            if tableName == 'user' :
                createTBCommand = "CREATE TABLE IF NOT EXISTS "+ str(tableName)+ self.TBUserInfo
            elif tableName == 'cost':
                createTBCommand = "CREATE TABLE IF NOT EXISTS "+ str(tableName)+ self.TBCostInfo
            initCommand = self.initialization()
            print "init Command : ",initCommand
            self.cursor.execute(createTBCommand)
            #self.conn.commit()
            self.conn = sql.connect(self.DB_DIR)
            print "executing initCommand"
            #self.cursor.execute(initCommand)
            self.customizedFetch(initCommand)
            r = self.fetchAllData('user')
            print "r : ",r
        except :
            self.closeConnection(self.conn)


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

        self.conn.commit()

    #@staticmethod
    def fetchAllData(self,tableName):
        fetchAllCommand = "SELECT * FROM "+tableName
        print "fetchAllCommand : ",fetchAllCommand
        self.cursor.execute(fetchAllCommand)
        return self.cursor.fetchall()

    #@staticmethod
    def customizedFetch(self,cmd):
        self.cursor.execute(cmd)
        self.conn.commit()
        return self.cursor.fetchall()
    #@classmethod
    def getBanana(self,key):
        getBananaCommand = "SELECT password FROM user WHERE userName='"+str(key)+"'"
        self.cursor.execute(getBananaCommand)
        raw = self.cursor.fetchall()
        return raw

if __name__ == "__main__" :
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

    values1=[('lunch',11,'aaa','2015-01-10 12:12:12'),
            ('lunch',11,'aaa','2015-01-11 12:12:12'),
            ('lunch',11,'aaa','2015-01-12 12:12:12'),
            ('lunch',11,'aaa','2015-01-13 12:12:12'),
            ('lunch',11,'aaa','2015-02-10 12:12:12'),
            ('lunch',11,'aaa','2015-02-11 12:12:12'),
            ('lunch',11,'aaa','2015-02-12 12:12:12'),
            ('lunch',11,'aaa','2015-02-13 12:12:12'),
            ('lunch',11,'aaa','2015-03-10 12:12:12'),
            ('lunch',11,'aaa','2015-03-14 12:12:12'),
            ('lunch',11,'aaa','2015-03-15 12:12:12'),
            ('lunch',11,'aaa','2015-03-17 12:12:12'),
            ('lunch',11,'aaa','2015-04-17 12:12:12'),
            ('lunch',11,'aaa','2015-04-19 12:12:12'),
            ('lunch',11,'aaa','2015-04-16 12:12:12'),
            ('lunch',11,'aaa','2015-05-03 12:12:12'),
            ('lunch',11,'aaa','2015-05-11 12:12:12'),
            ('lunch',11,'aaa','2015-05-29 12:12:12'),
            ('lunch',11,'aaa','2015-05-21 12:12:12'),
            ('lunch',11,'aaa','2015-05-22 12:12:12'),
            ('lunch',11,'aaa','2015-06-10 12:12:12'),
            ('lunch',11,'aaa','2015-11-10 12:12:12'),
            ('lunch',11,'aaa','2015-11-10 12:12:12'),
            ('lunch',11,'aaa','2015-12-10 12:12:12'),
            ('lunch',11,'aaa','2015-12-18 12:12:12'),
            ('snack',22,'bbb','2016-01-10 13:13:13'),
            ('lunch',11,'aaa','2016-01-19 12:12:12'),
            ('lunch',11,'aaa','2016-01-26 12:12:12'),
            ('lunch',11,'aaa','2016-02-03 12:12:12'),
            ('lunch',11,'aaa','2016-02-11 12:12:12'),
            ('lunch',11,'aaa','2016-02-29 12:12:12'),
            ('lunch',11,'aaa','2017-02-21 12:12:12'),
            ('lunch',11,'aaa','2017-02-22 12:12:12'),
            ('lunch',11,'aaa','2017-02-10 12:12:12'),
            ('lunch',11,'aaa','2017-10-10 12:12:12'),
            ('lunch',11,'aaa','2017-10-10 12:12:12'),
            ('lunch',11,'aaa','2017-10-10 12:12:12'),
            ('lunch',11,'aaa','2017-10-18 12:12:12')]

##########################
    #dbo.dropTable('cost')
    #dbo.createTable('cost')
##########################

    #dbo.createTable('user')
    dbo.createTable('cost')
    #for item in userInfo:
   #     dbo.insertData('user',item)
    #r = dbo.fetchAllData('user')
    #print "user information : \n %s"%r
    #print "-------------------------------"

    #for value in values1 :
    #    tmp = []
    #    i = 0
    #    for i in range(0,3):
    #        var = ed.enDecryption.encryption(str(value[i]))
    #        tmp.append(var)
    #    tmp.append(value[3])
    #    dbo.insertData('cost',tmp)
    #c = dbo.fetchAllData('cost')
    #print c
    #print "cost information : \n %s"%c


    cmd1 = "SELECT costDate,costName,costValue,comments FROM cost"
    cmd2 = "SELECT * FROM cost WHERE costDate LIKE '2016-02-03%'"
    cmd3 = "SELECT * FROM cost WHERE costDate=='2017-10-10 12:12:12'"
    cmd4 = "select * from cost where costDate=='2016-09-21 13:41:02%'"
    part = '2016-01-10 13:13'
    #cmd3 = "SELECT * FROM cost WHERE costDate LIKE \'"+part+"\'%"
    a = dbo.customizedFetch(cmd3)
    result = []
    result1 = []
    for item in a :
        item = list(item)
        print "listed item : ",item
        for i in range(1,len(item)-1):
            print "item["+str(i)+"] before: ",item[i]
            item[i] = ed.enDecryption.decryption(item[i])
            print "item["+str(i)+"] after : ",item[i]
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









