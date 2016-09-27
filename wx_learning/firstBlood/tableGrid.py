import wx
import wx.grid
import fonts
import common as cmm
import dateFilter as df
import enDecryption as ed
import DBOperation

class basicTable(wx.grid.PyGridTableBase):
    #def __init__(self,tableData,rowLabel=None,colLabel=None):
    def __init__(self,tableData,rowLabel=None,colLabel=None):
        wx.grid.PyGridTableBase.__init__(self)

        self.tableData = tableData
        self.rowLabel = rowLabel
        self.colLabel = colLabel

    def GetNumberRows(self):
        return len(self.tableData)
    def GetNumberCols(self):
        try:
            return len(self.tableData[0])
        except IndexError:
            pass
    def IsEmptyCell(self,row,col):
        if self.tableData[int(row)][int(col)]:
            return True
        else :
            return False
    def GetValue(self,row,col):
        return self.tableData[int(row)][int(col)]
    def SetValue(self,row,col,value):
        self.tableData[int(row)][int(col)] = value
    def GetColLabelValue(self,col):
        if self.colLabel :
            return self.colLabel[col]
    def GetRowLabelValue(self,col):
        if self.rowLabel :
            return self.rowLabel[col]

class dataPanel(wx.Panel):
    def __init__(self,parent,id,tableData,tableLabel):
        wx.Panel.__init__(self,parent,id)


        #(tableData,tableLabel) = cmm.getAndConvert()
        table = basicTable(tableData,rowLabel=tableLabel,colLabel=("Name","Money","Comments"))


        #create tableGrid panel
        self.grid = wx.grid.Grid(self)
        self.grid.SetTable(table)
        self.__setGridAttributes()


        #create black box text ctrl in this panel
        self.blackBox = self.createBlackBox(self)


        #create date dropDown list panel
        #self.dropDown = ds.timeSelectionPanel(self,-1)
        self.dropDown = self.dropDownSelection()


        #create totalBox
        self.createTotalBox(self)

        self.layout(self.blackBox,self.dropDown,self.grid,self.totalBoxSizer)

    def layout(self,blackBox,dropDownPanel,gridPanel,totalBoxSizer):
        dataPanelSizer = wx.BoxSizer(wx.VERTICAL)
        dataPanelSizer.Add(blackBox,0,wx.EXPAND)
        dataPanelSizer.Add((0,2))
        dataPanelSizer.Add(dropDownPanel,0,wx.EXPAND)
        dataPanelSizer.Add((0,2))
        dataPanelSizer.Add(gridPanel,8,wx.EXPAND)
        dataPanelSizer.Add(totalBoxSizer,0,wx.EXPAND|wx.ALIGN_CENTER)
        self.SetSizerAndFit(dataPanelSizer)

    def createBlackBox(self,parent):
        self.blackBox = wx.TextCtrl(parent,id=-1,style=wx.TE_PROCESS_ENTER)
        self.blackBox.SetValue("BLACK-BOX...DO NOT TOUCH...")
        self.blackBox.SetBackgroundColour("TURQUOISE")
        self.blackBox.SetForegroundColour("CADET BLUE")
        self.blackBox.SetFont(fonts.Fonts.romanBold12())
        self.Bind(wx.EVT_TEXT_ENTER,self.blackBoxEnter,self.blackBox)

        return self.blackBox

    def blackBoxEnter(self,event):
        command = self.blackBox.GetLabelText()
        command.strip()
        if 'costDate' not in command :
            if 'like' in command or 'LIKE' in command :
                #print "command : ",command
                varOld = command[command.find('\'')+1 : command.rfind('%')]
                #print "varOld : ",varOld
            elif '=' in command :
                varOld = command[command.find('\'')+1 : command.rfind('\'')]
                #print "varOld : ",varOld
            varNew = ed.enDecryption.encryption(varOld)
            varNew.strip()
            #print "varNew : ",varNew
            command = command.replace(varOld,varNew)
        else :
            pass

        dbo = DBOperation.DBOperation()
        raw = dbo.customizedFetch(command)
        (data,label) = cmm.decryptionList(raw)
        table = basicTable(data,rowLabel=label,colLabel=("Name","Money","Comments"))
        self.grid.SetTable(table)
        self.__setGridAttributes()
        self.Refresh()

    def createTotalBox(self,parent):
        totalBoxInfo = [("Total : ",wx.ROMAN,'static'),(wx.TE_NOHIDESEL|wx.TE_READONLY,'ctrl'),]
        (self.totalBoxSizer,self.totalBoxList) = cmm.createStaticTextControl(parent,totalBoxInfo,fonts.Fonts.romanBold14())

    ###################################################################
    #basic functions for this panel
    ###################################################################
    def __setGridAttributes(self):
        self.grid.BeginBatch()
        self.grid.SetLabelTextColour('Forest Green')
        self.grid.SetDefaultCellTextColour('Blue')
        self.grid.SetDefaultCellAlignment(wx.ALIGN_CENTER,wx.ALIGN_BOTTOM)
        self.grid.SetDefaultCellFont(fonts.Fonts.romanBold10())

        self.grid.AutoSizeRows()

        self.grid.EnableEditing(False)
        self.grid.SetLabelBackgroundColour('White')

    def dropDownSelection(self):
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
        self.cbSizer = wx.BoxSizer(wx.HORIZONTAL)

        for i in range(3):
            cbx = wx.ComboBox(parent=self,id=-1,value=cbxDefaultValue[i][0],choices='',style=wx.CB_DROPDOWN,name=cbxDefaultValue[i][0])
            self.Bind(wx.EVT_COMBOBOX,cbxDefaultValue[i][1],cbx)
            self.cbSizer.Add(cbx,1,wx.EXPAND)
            self.cbxList.append(cbx)
        self.cbSizer.Add(submitButton,1)
        #self.SetSizer(self.cbSizer)
        print "self.timeList000 : ",self.timeList
        if self.timeList :
            self.initYear()
        return self.cbSizer

    def initYear(self):

        year = self.timeList.keys()
        year.sort()
        self.cbxList[0].SetItems(year)

    def dyChangeMonthValue(self,event):
        (year,month,day) = self.getYearMonthDayFromCbx()
        if year != '-':
            months = self.timeList[year].keys()
            months.sort()
            self.cbxList[1].SetItems(months)
            self.cbxList[2].SetItems("")

    def dyChangeDateValue(self,event):
        (year,month,day) = self.getYearMonthDayFromCbx()
        if month != '-' :
            days = self.timeList[year][month]
            self.cbxList[2].SetItems(days)

    def nothing(self,event):
        pass

    def getYearMonthDayFromCbx(self):
        yearIndex = self.cbxList[0].GetSelection()
        month = day = ""
        if yearIndex != wx.NOT_FOUND :
            year = self.cbxList[0].GetItems()[yearIndex]

            monthIndex = self.cbxList[1].GetSelection()
            if monthIndex != wx.NOT_FOUND :
                month = self.cbxList[1].GetItems()[monthIndex]
                dayIndex = self.cbxList[2].GetSelection()
                if dayIndex != wx.NOT_FOUND :
                    day = self.cbxList[2].GetItems()[dayIndex]
                else :
                    day = ""
            else :
                month = ""
                #print "year = %s; month = %s"%(year,month)
        else :
            #print "yearIndex : ",yearIndex
            #print "monthIndex : ",monthIndex
            year = ""
        #print "year : %s\nmonth : %s\nday : %s"%(year,month,day)
        return year,month,day

    def searchDataViaButton(self,event):
        (year,month,day) = self.getYearMonthDayFromCbx()
        dateDetail = (year,month,day)

        #getting data from db according to the specified command.
        (tableData,tableLabel) = cmm.getAndConvertCostData(dateDetail)

        #get the total number of the costs.
        total = cmm.calculatingTotalCost(tableData)
        self.totalBoxList[1].SetValue(str(total))
        table = basicTable(tableData,rowLabel=tableLabel,colLabel=("Name","Money","Comments"))
        self.grid.SetTable(table)
        self.__setGridAttributes()
        self.Refresh()
        print "self.timeList111 : ",self.timeList
        if not self.timeList:
            self.timeList = df.dateFilter.getTimeList()
            print "self.timeList222 : ",self.timeList
            self.initYear()

class tableGridFrame(wx.Frame):
    def __init__(self,parent=None,id=-1,title="test frame",pos=(0,0),size=(600,400)):
        wx.Frame.__init__(self,parent,id,title,pos,size)
        #(year,month,day) = self.getYearMonthDayFromCbx()
        #(tableData,tableLabel) = cmm.getAndConvertCostData()
        self.panel = dataPanel(self,-1,tableData,tableLabel)

        width, height = self.GetClientSizeTuple()

        self.panel.grid.SetDefaultColSize(width/4.0,True)
        self.panel.grid.SetRowLabelSize(width/4.0)




if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = tableGridFrame()
    frame.Show()
    app.MainLoop()