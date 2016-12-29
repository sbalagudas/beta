#coding=utf-8
#qpy:console
#qpy:2
import os
import time as tm
import datetime

#file_name = "/sdcard/com.hipipal.qpyplus/cost/cost.txt"
#file_name = "/storage/emulated/0/com.hipipal.qpyplus/cost/cost.txt"
file_name = "/storage/emulated/0/com.hipipal.qpyplus/cost/tailand.txt"
#file_name = "c:\\Python27\\cost.txt"
#branch test... 
class Cost(object):
    def Check_Null(self,value):
        if 0 == len(value):
            print "input can not be empty"
            return 0
        else:
            return 1
    def Cost_Menu(self):
        print "---------------------------"
        print " [1]  吃饭    |  [2]  零食 -"
        print "---------------------------"
        print " [3]  买菜    |  [4]  加油 -"
        print "---------------------------"
        print " [5]  衣服    |  [6]  其他 -"
        print "---------------------------"
        print " [7]  其他(S) |  [0]  退出 -"              
        print "---------------------------"
    def main_menu(self):
        print "------------------------------"
        print "     1   Add cost             "
        print "     2   Daily cost sum       "
        print "     3   Monthly cost sum     "
        print "     4   Print all            "
        print "     5   Quit                 "
        print "------------------------------"
    def Time_Parse(self,p_time):
        if 0 == len(p_time):
            print "time is empty, please check..."
            return 1
        p_t = p_time.split(" ")
        p_date = p_t[0].split("-")
        p_date = map(lambda x : int(x), p_date)
        return p_date
    def Time_Cmp(self,l_t):
        c_t = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
        ct_lst = self.Time_Parse(c_t)
        c_t = datetime.datetime(ct_lst[0],ct_lst[1],ct_lst[2])
        #print "c_t : ",c_t
        
        l_t = l_t.split('==')[1]
        lg_lst = self.Time_Parse(l_t)
        lg_t = datetime.datetime(lg_lst[0],lg_lst[1],lg_lst[2])
        #print "lg_t : ",lg_t

        if (c_t - lg_t).days == 0 :
            return 0
        elif (c_t - lg_t).days > 0 :
            return 1
        else :
            return -1
    def Add_Time_Stamp(self):
        f = file(file_name,'a+')
        t = '=='+tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())+'==\n'
        print "t : ",t
        f.write(t)
        f.close()
    def Get_Latest_Time_Stamp(self):
        log_time = ""
        f = file(file_name,'r')
        for line in f:
            if line.startswith('='):
                log_time = line
        #print "log_time : ",log_time
        f.close()
        return log_time
    def Write_Costs(self,c_n,c_m):
        f = file(file_name,'a+')
        input_string = c_n+'\t:\t'+c_m+'\n'
        f.write(input_string)
        f.close()
    def Add_Cost(self,file_name):
        cost_type = ["吃饭","零食","买菜","加油","衣服","其他"]
        cost_name = ""
        log_time = ''
        #cheking if the dir is valid
        if not os.path.isfile(file_name):
            self.Add_Time_Stamp()
        l_ts = self.Get_Latest_Time_Stamp()

        flag = self.Time_Cmp(l_ts)

        if 1 == flag:
            self.Add_Time_Stamp()
        cost_money = ""
        while True:
            self.Cost_Menu()
            cost_number = raw_input("Select the cost type :")
            if (cost_number not in "1234567" or 0 == len(cost_number)) and '0' != cost_number:
                print "the number should be between 1-6"
            elif '0' == cost_number:
                break
            elif '7' == cost_number:
                cost_name = raw_input("pleasee input cost name : ")
                cost_money = raw_input("please input the money : ")
            else:
                cost_name = cost_type[int(cost_number)-1]
                cost_money = raw_input("Input Money : ")
            if not cost_money.isdigit():
                print "money should be some numbers ..."
                continue
            else :    
                self.Write_Costs(cost_name,cost_money)
    
    def Get_Certain_dt_total(self,date_string):
        daily_list = []
        null = self.Check_Null(date_string)
        if not null:
            return 0
        try :
            f = file(file_name,'r')
            for line in f:
                if date_string in line:
                    daily_list.append(line)
                    continue
                l_dl = len(daily_list)
                if 0 != l_dl and line.startswith("=="):
                    break
                if  0 != l_dl and (not line.startswith("==")) and 0 != len(line.strip()):
                    daily_list.append(line)                
            f.close()
        except IOError :
            print "can not open file : ",file_name
        i = 0
        len_daily_list = len(daily_list)
        for i in range(len_daily_list):
            temp = map(lambda x:x.split("\n")[0],daily_list)
            print "----------------------"
            print temp[i]
        #caculate the sum
        day_sum = 0
        d_c = map(lambda x:int(x.split("\t")[2].split("\n")[0]),daily_list[1:])
        for item in d_c:
            day_sum += item
        print "----------------------"
        print "TOTAL\t:\t",day_sum
        print "----------------------"
        return day_sum

    def Get_Time_List(self):
        dt_list = []
        try :
            f = file(file_name,'r')
            for line in f:
                if line.startswith('='):
                    dt_list.append(line)
            dt_list = map(lambda x:x[2:12],dt_list)
            f.close()
        except IOError:
            print "could not open file : ",file_name
        return dt_list
    def Daily_Cost_Sum(self):
        day_total = 0
        dt_list = self.Get_Time_List()
        dt_list.reverse()
        if 9 < len(dt_list):
            dt_list = dt_list[0:9]
                
        print "you can get the following dates' sum : "
        i = 0
        for i in range(len(dt_list)):
            print "-------------------"
            print [ i+1 ],' : '+dt_list[i]+' -'

        ch = ''
        while True:
            ch = raw_input("enter the date you want to check : ['0' for quit]")
            if (ch not in "123456789" or 0 == len(ch)) and '0' != ch:
                print "you should choose option from only 1 to 9 "
            elif '0' == ch:
                break
            else :
                try :
                    day_total = self.Get_Certain_dt_total(dt_list[int(ch)-1])
                except IndexError:
                    print "out of range, you should enter only from [ 1-",len(dt_list),"]"

    def Print_All(self):
        i = 0
        try :
            f = file(file_name,'r')
            for line in f:
                if 0 == i or "==" not in line:
                    i = 1
                    print line
                    continue
                elif "==" in line :
                    ch = raw_input("Press enter to continue...['0' for quit]")
                    print line
                    if '0' == ch:
                        break
                    else:
                        continue
            f.close()     
        except IOError:
            print "can not open file : ",file_name
    
    def Get_Certain_Mon_Cost(self,dt_string):
        lst_mon = []
        null = self.Check_Null(dt_string)
        if not null:
            return 0
        try :
            f = file(file_name,'r')
            for line in f:
                if dt_string in line:
                    lst_mon.append(line)
                    continue
                elif 0 != len(lst_mon) and line.startswith("=") and dt_string not in line:
                    break
                elif 0 != len(lst_mon):
                    lst_mon.append(line)
            #print "lst_mon : ",lst_mon
            f.close()
        except IOError: 
            print "can not open file : ",file_name
        
        map(lambda x:lst_mon.remove(x),[n for n in lst_mon if n.startswith("=")])
        map(lambda x:lst_mon.remove(x),[n for n in lst_mon if n == '\n'])
        lst_mon = map(lambda x:int(x.split("\t")[2].split("\n")[0]),lst_mon)

        monthly_cost = 0
        monthly_cost = sum(lst_mon)
        print "----------------------"
        print "TOTAL\t:\t", monthly_cost
        print "----------------------"
        
        
    def Get_Monthly_Total_Cost(self):
        lst_mon = []
        mon = []
        t_mon = self.Get_Time_List()
        t_mon = map(lambda x:x[:-3],t_mon)
        #print "t_mon : %s"%t_mon

        #map(lambda x:mon.append(x),[n for n in t_mon if n not in mon])
        mon = list(set(t_mon)) #remove the duplicated values from the list

        mon.sort()
        mon.reverse()
        #print "mon : ",mon
        print "now you can check the monthly cost listed below : "
        i = 0
        for i in range(len(mon)):
            print "-------------------"
            print [ i+1 ],' : '+mon[i]+'    -'

        ch = " "
        while True:
            ch = raw_input("enter the date you want to check : ['0' for quit]")
            if (ch not in "123456789" or 0 == len(ch)) and '0' != ch:
                print "you should choose option from only 1 to 9 "
            elif '0' == ch:
                break
            else :
                try :
                    day_total = self.Get_Certain_Mon_Cost(mon[int(ch)-1])
                except IndexError:
                    print "out of range, you should enter only from [ 1-",len(mon),"]"
            

if __name__ == "__main__":
    cost = Cost()
    ch = ""
    while ch != "5":
        cost.main_menu()
        ch = raw_input("Input your choice:")
        if ch not in "12345":
            print "you could only enter 1-5"
            continue
        if '1' == ch:
            cost.Add_Cost(file_name)
        elif '2' == ch :
            cost.Daily_Cost_Sum()
        elif '3' == ch :
            cost.Get_Monthly_Total_Cost()
        elif '4' == ch :
            cost.Print_All()
        

        
