import wx
import wx.grid
import fonts
import common as cmm

class basicTable(wx.grid.PyGridTableBase):
    def __init__(self,tableData,rowLabel=None,colLabel=None):
        wx.grid.PyGridTableBase.__init__(self)

        self.tableData = tableData
        self.rowLabel = rowLabel
        self.colLabel = colLabel

    def GetNumberRows(self):
        print "rows : ",len(self.tableData)
        return len(self.tableData)
    def GetNumberCols(self):
        print "cols : ",len(self.tableData[0])
        return len(self.tableData[0])
    def IsEmptyCell(self,row,col):
        if self.tableData[int(row)][int(col)]:
            return True
        else :
            return False
    def GetValue(self,row,col):
        #print "value : ",self.tableData[int(row)][int(col)]
        return self.tableData[int(row)][int(col)]
    def SetValue(self,row,col,value):
        self.tableData[int(row)][int(col)] = value
    def GetColLabelValue(self,col):
        #print "table label : ",self.tableLabel[col]
        if self.colLabel :
            return self.colLabel[col]
    def GetRowLabelValue(self,col):
        #print "table label : ",self.tableLabel[col]
        if self.rowLabel :
            return self.rowLabel[col]

class SimpleGrid(wx.grid.Grid):
    def __init__(self,parent,tableData,tableLabel):
        wx.grid.Grid.__init__(self,parent,id=-1)
        self.tableData = tableData
        self.tableLabel = tableLabel
        self.SetTable(basicTable(tableData=self.tableData,colLabel=self.tableLabel))

class gridPanel(wx.Panel):
    def __init__(self,parent,id):
        '''
        tableData = (('aa',11,'aaa','2016-01-01 11:11:11'),
                          ('bb',11,'bbb','2016-01-02 11:11:22'),
                          ('cc',11,'cccasdfasdfasdfa','2016-01-03 11:11:33'),
                          ('dd',11,'dddasdfasdfasdfasdfas','2016-01-04 11:11:44'),
                          ('ee',11,'eeeasdfasdf','2016-01-05 11:11:55'))
        tableLabel = ('cost name','value','comments','date')
        '''

        wx.Panel.__init__(self,parent,id)
        (tableData,tableLabel) = cmm.getAndConvert("select * from cost")
        self.grid = SimpleGrid(self,tableData,tableLabel)

        self.grid.SetLabelTextColour('Forest Green')
        self.grid.SetDefaultCellTextColour('Blue')
        self.grid.SetDefaultCellAlignment(wx.ALIGN_CENTER,wx.ALIGN_BOTTOM)
        self.grid.SetDefaultCellFont(fonts.Fonts.romanBold12())
        self.grid.SetDefaultColSize(1,False)
        self.grid.SetInitialSize((550,500))
        self.grid.Fit()

class tableGridFrame(wx.Frame):
    def __init__(self,parent=None,id=-1,title="test frame",pos=(0,0),size=(600,400)):
        wx.Frame.__init__(self,parent,id,title,pos,size)

        tableData = (('aa',11,'aaa','2016-01-01 11:11:11'),
                          ('bb',11,'bbb','2016-01-02 11:11:22'),
                          ('cc',11,'ccc','2016-01-03 11:11:33'),
                          ('dd',11,'ddd','2016-01-04 11:11:44'),
                          ('ee',11,'eee','2016-01-05 11:11:55'))
        tableLabel = ('cost name','value','comments','date')

        #gridPanel = gridPanel()

        #grid = SimpleGrid(self,tableData,tableLabel)
        #grid.SetFont(fonts.Fonts.romanBold18())
        #grid.SetCellTextColour(2,3,'Cyan')
        #grid.SetBackgroundColour("Cyan")
        #grid.Fit()



if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = tableGridFrame()
    frame.Show()
    app.MainLoop()