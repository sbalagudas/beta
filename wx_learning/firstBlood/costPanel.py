#coding=utf-8
import wx
import wx.lib.buttons as buttons
import addCostDetail as adt
import fonts

class testPanel(wx.Panel):
    COLS_NUM = 3
    def __init__(self,parent,id=-1):
        wx.Panel.__init__(self,parent,id)

class costPanel(wx.Panel):
    COLS_NUM = 3
    def __init__(self,parent,id=-1):
        wx.Panel.__init__(self,parent,id)

        costGrid = self.createCostGrid()
        costButtonGrid = self.createCostButtonGrid()

        self.oldCostType = 'Meal'
        self.layout(costGrid,costButtonGrid)

    def layout(self,costGrid,costButton):
        self.costPanelSizer = wx.BoxSizer(wx.VERTICAL)
        self.costPanelSizer.Add(costGrid,1)
        #self.costPanelSizer.Add((0,16))
        self.costPanelSizer.Add(costButton,1,wx.EXPAND)
        self.SetSizer(self.costPanelSizer)

    def costCategory(self):
        #return ["吃饭","买菜","加油","商场","网购","零食","交通","节日","其他"]
        return ["Meal","Vegetable","Fuel","Mall","On Line","Snacks","Traffic","Festival","Others"]

    def costButtonInfo(self):
        return ["Daily Data","Monthly Data","Yearly Data"]

    def createCostGrid(self):
        self.costGridDict = {}
        self.costGridToggleList = {}
        costGrid = wx.GridSizer(cols=self.COLS_NUM,hgap=5,vgap=5)
        for eachCost in self.costCategory():
            #button = wx.ToggleButton(self,id=-1,label=eachCost,size=(80,80))
            button = buttons.GenToggleButton(self,id=-1,label=str(eachCost),size=(80,80))
            button.SetBezelWidth(3)
            button.SetUseFocusIndicator(False)
            self.Bind(wx.EVT_BUTTON,self.callAddCost,button)
            button.SetFont(fonts.Fonts.romanBold14())
            costGrid.Add(button,1)
            self.costGridDict[button.GetId()] = eachCost
            self.costGridToggleList[eachCost] = button
        #self.costGridToggleList[self.costCategory()[0]]
        return costGrid

    def createCostButtonGrid(self):
        #costSizer = wx.GridSizer(cols=1)
        costSizer = wx.BoxSizer(wx.VERTICAL)
        for eachData in self.costButtonInfo():
            button  = wx.Button(self,id=-1,label=eachData)
            button.SetFont(fonts.Fonts.romanBold16())
            costSizer.Add(button,1,wx.EXPAND)
        return costSizer

    def callAddCost(self,event):
        self.selectedCostType = self.costGridDict[event.GetId()]
        if 0 == len(self.oldCostType) or self.oldCostType == self.selectedCostType:
            self.oldCostType = self.selectedCostType
            print "set"+self.oldCostType+"to true"
            self.costGridToggleList[self.selectedCostType].SetToggle(True)
        else :
            #self.selectedCostType != self.oldCostType :
            #print "set"+self.oldCostType+"to false"
            self.costGridToggleList[self.oldCostType].SetToggle(False)
            self.oldCostType = self.selectedCostType
        self.costFrame = adt.costDataFrame(costName=self.selectedCostType)
        self.costFrame.Show()


class costFrame(wx.Frame):
    def __init__(self,parent=None,id=-1,title="cost",pos=wx.DefaultPosition,size=(800,600)):
        wx.Frame.__init__(self,parent,id,title,pos,size)

        self.cost = costPanel(self,-1)


    def layout(self,panel1,panel2):
        self.bs = wx.BoxSizer(wx.HORIZONTAL)
        self.bs.Add(panel1,1)
        self.bs.Add(panel2,1,wx.EXPAND)
        self.SetSizer(self.bs)
        #self.bs.Fit(self)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = costFrame()
    frame.Show()
    app.MainLoop()

