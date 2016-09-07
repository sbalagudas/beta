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
        if "user" == tableName :
            insertCommand = "INSERT INTO " + str(tableName) + " (username,password,regDate)" + " values (?,?,?)"
        elif "cost" == tableName :
            insertCommand = "INSERT INTO " + str(tableName) + " (costName,costValue,comments,costDate)" + " values (?,?,?,?)"

        self.cursor.execute(insertCommand,value)
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
    values=[('lunch',11,'','2016-01-10 12:12:12'),
            ('snack',22,'','2016-01-10 13:13:13'),
            ('fuel',33,'','2016-01-11 14:14:14'),
            ('vegetable',22,'','2016-01-12 15:15:15'),
            ('lunch',44,'','2016-01-13 16:16:16')]

##########################
    #dbo.dropTable('cost')
    #dbo.createTable('cost')
##########################

    #dbo.createTable('user')
    #dbo.createTable('cost')
    #for item in userInfo:
    #    dbo.insertData('user',item)
    #r = dbo.fetchAllData('user')
    #print "user information : \n %s"%r
    #print "-------------------------------"
    #for value in values :
    #    dbo.insertData('cost',value)
    #c = dbo.fetchAllData('cost')
    #print "cost information : \n %s"%c


    cmd1 = "SELECT * FROM cost WHERE costDate LIKE '2016-09%'"
    cmd2 = "SELECT * FROM cost WHERE costDate LIKE '2016-09-07%'"
    #cmd3 = "SELECT * FROM cost WHERE costDate LIKE '2016-01-10 13:13%'"
    a = dbo.customizedFetch(cmd1)
    result = []
    result1 = []
    for item in a :
        item = list(item)
        for i in range(1,4):
            #print "item["+str(i)+"] before: ",item[i]
            item[i]= ed.enDecryption.decryption(item[i])
            #print "item["+str(i)+"] after : ",item[i]
            result.append(item)

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










