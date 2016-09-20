import wx
import wx.grid
import fonts
import common as cmm
import dateFilter as df
import dataSelection as ds

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


        self.layout(self.blackBox,self.dropDown,self.grid)

    def layout(self,blackBox,dropDownPanel,gridPanel):
        dataPanelSizer = wx.BoxSizer(wx.VERTICAL)
        dataPanelSizer.Add(blackBox,0,wx.EXPAND)
        dataPanelSizer.Add((0,2))
        dataPanelSizer.Add(dropDownPanel,0,wx.EXPAND)
        dataPanelSizer.Add((0,2))
        dataPanelSizer.Add(gridPanel,8,wx.EXPAND)
        self.SetSizerAndFit(dataPanelSizer)

    def createBlackBox(self,parent):
        blackBox = wx.TextCtrl(parent,-1,"BLACK-BOX...DO NOT TOUCH...")
        blackBox.SetBackgroundColour("TURQUOISE")
        blackBox.SetForegroundColour("CADET BLUE")
        blackBox.SetFont(fonts.Fonts.romanBold12())
        return blackBox

    def createTotal

    def __setGridAttributes(self):
        self.grid.BeginBatch()
        self.grid.SetLabelTextColour('Forest Green')
        self.grid.SetDefaultCellTextColour('Blue')
        self.grid.SetDefaultCellAlignment(wx.ALIGN_CENTER,wx.ALIGN_BOTTOM)
        self.grid.SetDefaultCellFont(fonts.Fonts.romanBold10())

        self.grid.AutoSizeRows()
        #self.grid.AutoSizeColumns()
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
        self.initYear()
        return self.cbSizer

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
        table = basicTable(tableData,rowLabel=tableLabel,colLabel=("Name","Money","Comments"))
        self.grid.SetTable(table)
        #self.grid.Refresh()
        self.__setGridAttributes()
        self.Refresh()

class tableGridFrame(wx.Frame):
    def __init__(self,parent=None,id=-1,title="test frame",pos=(0,0),size=(600,400)):
        wx.Frame.__init__(self,parent,id,title,pos,size)

        (tableData,tableLabel) = cmm.getAndConvert()
        self.panel = dataPanel(self,-1,tableData,tableLabel)

        width, height = self.GetClientSizeTuple()

        self.panel.grid.SetDefaultColSize(width/4.0,True)
        self.panel.grid.SetRowLabelSize(width/4.0)




if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = tableGridFrame()
    frame.Show()
    app.MainLoop()