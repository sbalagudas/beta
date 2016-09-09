import wx
import timeDisplay
#from paint import Paint as pt
import costPanel as cP
import login
import time
import tableGrid

class mainFrame(wx.Frame):
    tableData = (('aa',11,'aaa','2016-01-01 11:11:11'),
                          ('bb',11,'bbb','2016-01-02 11:11:22'),
                          ('cc',11,'cccasdfasdfasdfa','2016-01-03 11:11:33'),
                          ('dd',11,'dddasdfasdfasdfasdfas','2016-01-04 11:11:44'),
                          ('ee',11,'eeeasdfasdf','2016-01-05 11:11:55'))
    tableLabel = ('cost name','value','comments','date')
    def __init__(self,
                 parent=None,
                 id=wx.ID_ANY,
                 title="Banana World",
                 pos=(0,0),
                 size=(800,600),
                 style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER | wx.MINIMIZE_BOX |wx.MAXIMIZE_BOX)):
        wx.Frame.__init__(self,parent,id,title,pos,size,style)

        self.panelTime = timeDisplay.timeDisplay(self,-1,'apple')
        #self.panelPaint = pt(self,-1)
        self.cost = cP.costPanel(self,-1)
        #self.tstPanel = cP.testPanel(self,-1)
        #self.tstPanel.SetBackgroundColour('White')
        #self.tableGrid = tableGrid.SimpleGrid(self,self.tableData,self.tableLabel)
        self.tableGrid = tableGrid.gridPanel(self,-1)
        self.layout(self.panelTime,self.cost,self.tableGrid)

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
    def __init__(self,redirect=False,filename=None):
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

