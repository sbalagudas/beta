import wx
import dateFilter as df
import common as cmm
import Main
import tableGrid

class timeSelectionPanel(wx.Panel):
    def __init__(self,parent,id):
        wx.Panel.__init__(self,parent,id)

        #local variable declaration.
        self.cbxList = []
        self.timeList = df.dateFilter.getTimeList()
        cbxDefaultValue = [('Year',self.dyChangeMonthValue),
                           ('Month',self.dyChangeDateValue),
                           ('Day',self.nothing)]

        #create the submit button.
        submitButton = wx.Button(self,id=-1,label="Submit")
        self.Bind(wx.EVT_BUTTON,self.searchDataViaButton,submitButton)
        #create combox and add them to sizer
        cbSizer = wx.BoxSizer(wx.HORIZONTAL)

        for i in range(3):
            cbx = wx.ComboBox(parent=self,id=-1,value=cbxDefaultValue[i][0],choices='',style=wx.CB_DROPDOWN,name=cbxDefaultValue[i][0])
            self.Bind(wx.EVT_COMBOBOX,cbxDefaultValue[i][1],cbx)
            cbSizer.Add(cbx,1,wx.EXPAND)
            self.cbxList.append(cbx)
        cbSizer.Add(submitButton,1)
        self.SetSizer(cbSizer)
        self.initYear()

    def initYear(self):
        year = self.timeList.keys()
        year.sort()
        self.cbxList[0].SetItems(year)

    def dyChangeMonthValue(self,event):
        (year,month) = self.getYearMonthFromCbx()
        months = self.timeList[year].keys()
        months.sort()
        self.cbxList[1].SetItems(months)

    def dyChangeDateValue(self,event):
        (year,month) = self.getYearMonthFromCbx()
        days = self.timeList[year][month]

        self.cbxList[2].SetItems(days)
    def nothing(self,event):
        pass

    def getYearMonthFromCbx(self):
        yearIndex = self.cbxList[0].GetSelection()
        year = self.cbxList[0].GetItems()[yearIndex]
        month = ""
        try :
            monthIndex = self.cbxList[1].GetSelection()
            month = self.cbxList[1].GetItems()[monthIndex]
        except IndexError:
            pass
        return year,month

    def searchDataViaButton(self,event):
        (tableData,tableLabel) = cmm.getAndConvert()
        print "1111"
        Main.mainFrame.tableGrid = tableGrid.dataPanel(self,-1,tableData,tableLabel)
        Main.mainFrame.Refresh()




class Frame(wx.Frame):
    def __init__(self,parent=None,id=-1,title='time selection',pos=wx.DefaultPosition,size=(600,400)):
        wx.Frame.__init__(self,parent,id,title,pos,size)
        panel = timeSelectionPanel(self,-1)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = Frame()
    frame.Show()
    app.MainLoop()