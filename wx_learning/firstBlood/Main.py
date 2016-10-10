import wx
import timeDisplay
import common as cmm
import costPanel as cP
import login
import os
import tableGrid

class mainFrame(wx.Frame):
    tableLabel = ('cost name','value','comments','date')
    def __init__(self,
                 parent=None,
                 id=wx.ID_ANY,
                 title="Banana World",
                 pos=(0,0),
                 size=(900,600),
                 style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER | wx.MINIMIZE_BOX |wx.MAXIMIZE_BOX)):
        wx.Frame.__init__(self,parent,id,title,pos,size,style)
        self.panelTime = timeDisplay.timeDisplay(self,-1,'Sophia')
        self.cost = cP.costPanel(self,-1)
        self.tableGrid = tableGrid.dataPanel(self,-1,'','')
        (width, height) = self.GetClientSizeTuple()
        self.tableGrid.grid.SetDefaultColSize((width-253)/4.0,True)
        self.tableGrid.grid.SetRowLabelSize((width-253)/4.6)

        #set UI colors
        #ADEAEA,'#66CCCC'
        self.colorSet = ['#CCFFCC',"#CCFFCC"]
        self.changeUIColor(self.colorSet)

        self.layout(self.panelTime,self.cost,self.tableGrid)

    def changeUIColor(self,colorSet):
        self.panelTime.SetBackgroundColour(colorSet[0])
        self.cost = cP.costPanel(self,-1,colorSet[1])
        #self.Refresh()

    def updateTableGrid(self,event):
        (tableData,tableLabel) = cmm.getAndConvert()
        self.tableGrid = tableGrid.dataPanel(self,-1,tableData,tableLabel)
        self.Refresh()

    def layout(self,time,cP,tableGrid):
        subBox = wx.BoxSizer(wx.HORIZONTAL)
        subBox.Add(cP,0)
        subBox.Add(tableGrid,1,wx.EXPAND)

        mainBox = wx.BoxSizer(wx.VERTICAL)
        mainBox.Add(time,1,wx.EXPAND)
        mainBox.Add(subBox,6,wx.EXPAND)

        self.SetSizer(mainBox)
        #mainBox.Fit(self)



class mainApp(wx.App):
    def __init__(self,redirect=False,filename=str(os.getcwd())+'main.txt'):
        wx.App.__init__(self,redirect,filename)
    def OnInit(self):
        frame = mainFrame()
        frame.Show()

        #self.loginWindow = login.logInFrame()
        #self.SetTopWindow(self.loginWindow)
        #self.loginWindow.Show()
        return True

if __name__ == "__main__":
    mApp = mainApp()
    mApp.MainLoop()

