import wx
import wx.grid
import fonts
import common as cmm

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
        return len(self.tableData[0])
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

class gridPanel(wx.Panel):
    def __init__(self,parent,id):
        wx.Panel.__init__(self,parent,id)
        (tableData,tableLabel) = cmm.getAndConvert()
        table = basicTable(tableData,rowLabel=tableLabel,colLabel=("Name","Money","Comments"))
        self.grid = wx.grid.Grid(self)
        self.grid.SetTable(table)
        self.__setGridAttributes()
        panelSizer = wx.BoxSizer()
        panelSizer.Add(self.grid,1,wx.EXPAND)
        self.SetSizer(panelSizer)
        #width, height = self.GetClientSizeTuple()
        #print "w,h : %s,%s"%(width,height)
        #grid.SetDefaultColSize(width/3.5)

    def createTimeCbx(self):
        cbxSizer = wx.BoxSizer(wx.HORIZONTAL)

    def __setGridAttributes(self):
        self.grid.BeginBatch()
        self.grid.SetLabelTextColour('Forest Green')
        self.grid.SetDefaultCellTextColour('Blue')
        self.grid.SetDefaultCellAlignment(wx.ALIGN_CENTER,wx.ALIGN_BOTTOM)
        self.grid.SetDefaultCellFont(fonts.Fonts.romanBold10())

        self.grid.AutoSizeRows()
        self.grid.EnableEditing(False)
        #grid.SetDefaultCellBackgroundColour("Cyan")
        #grid.SetDefaultColSize(300,True)
        #grid.SetDefaultRowSize(200,True)



class tableGridFrame(wx.Frame):
    def __init__(self,parent=None,id=-1,title="test frame",pos=(0,0),size=(600,400)):
        wx.Frame.__init__(self,parent,id,title,pos,size)

        self.panel = gridPanel(self,-1)

        width, height = self.GetClientSizeTuple()

        self.panel.grid.SetDefaultColSize(width/4.0,True)
        self.panel.grid.SetRowLabelSize(width/4.0)
        #frameSizer = wx.BoxSizer(wx.VERTICAL)
        #frameSizer.Add(self.panel,1,wx.EXPAND)

        #self.panel.Layout()
        self.Layout()


    def layout(self,blackBox,gridPanel):
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(blackBox,1,wx.EXPAND)
        mainSizer.Add(gridPanel,9,wx.EXPAND)
        self.SetSizer(mainSizer)

    def createBlackBox(self,parent):
        blackBox = wx.TextCtrl(parent,-1,"BLACK-BOX...DO NOT TOUCH...")
        blackBox.SetBackgroundColour("TURQUOISE")
        blackBox.SetForegroundColour("CADET BLUE")
        blackBox.SetFont(fonts.Fonts.romanBold12())
        return blackBox

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = tableGridFrame()
    frame.Show()
    app.MainLoop()