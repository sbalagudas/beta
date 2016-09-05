#coding=utf-8
import wx
import wx.lib.buttons as buttons
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

        self.layout(costGrid,costButtonGrid)

    def layout(self,costGrid,costButton):
        self.costPanelSizer = wx.BoxSizer(wx.VERTICAL)
        self.costPanelSizer.Add(costGrid,1)
        self.costPanelSizer.Add(costButton,1,wx.EXPAND)
        self.SetSizer(self.costPanelSizer)

    def costCategory(self):
        #return ["吃饭","买菜","加油","商场","网购","零食","交通","节日","其他"]
        return ["Meal","Vegetable","Fuel","Mall","On Line","Snacks","Traffic","Festival","Others"]

    def costButtonInfo(self):
        return ["Daily Data","Monthly Data","Yearly Data"]

    def createCostGrid(self):
        costGrid = wx.GridSizer(cols=self.COLS_NUM,hgap=5,vgap=5)
        for eachCost in self.costCategory():
            button = buttons.GenToggleButton(self,id=-1,label=eachCost,size=(80,80))
            button.SetBezelWidth(3)
            button.SetUseFocusIndicator(False)
            button.SetFont(fonts.Fonts.romanBold14())
            costGrid.Add(button,1)
        #self.SetSizer(costGrid)
        #costGrid.Fit(self)
        return costGrid

    def createCostButtonGrid(self):
        costSizer = wx.GridSizer(cols=1,hgap=5)
        for eachData in self.costButtonInfo():
            button  = wx.Button(self,id=-1,label=eachData)
            button.SetFont(fonts.Fonts.romanBold16())
            costSizer.Add(button,1,wx.EXPAND)
        #self.SetSizer(costSizer)
        #costSizer.Fit(self)
        return costSizer

class costFrame(wx.Frame):
    def __init__(self,parent=None,id=-1,title="cost",pos=wx.DefaultPosition,size=(800,600)):
        wx.Frame.__init__(self,parent,id,title,pos,size)

        self.cost = costPanel(self,-1)
        #self.testPanel = testPanel(self,-1)

        #self.layout(self.cost,self.testPanel)

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

