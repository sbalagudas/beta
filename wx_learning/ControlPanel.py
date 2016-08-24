import wx
import wx.lib.buttons as buttons

class ControlPanel(wx.Panel):
    BMP_SIZE = 16
    BMP_BORDER = 3
    NUM_COLS = 4
    SPACING = 4

    colorList=('Black','Yellow','Red','Green',
           'Cyan','Blue','Grey','Forest Green',
           'Spring Green','Purple','Pink','Light Blue',
           'Dark Green','Dark Grey','Navy','Goldenrod',
           'Brown','Aquamarine','Orange','Dim Grey',)
    maxThickness = 16
    def __init__(self,parent,ID,paint) :
        wx.Panel.__init__(self,parent,ID,style=wx.RAISED_BORDER)
        self.paint = paint

        buttonSize = (self.BMP_SIZE + 2* self.BMP_BORDER,self.BMP_SIZE + 2* self.BMP_BORDER)
        colorGrid = self.createColorGrid(self,buttonSize)
        thicknessGrid = self.createThicknessGrid(self,buttonSize)
        self.layout(colorGrid,thicknessGrid)

    def layout(self,colorGrid,thicknessGrid):
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(colorGrid,0,wx.ALL,self.SPACING)
        box.Add(thicknessGrid,0,wx.ALL,self.SPACING)
        self.SetSizer(box)
        box.Fit(self)

    def createColorGrid(self,parent,buttonSize):
        self.colorMap = {}
        self.colorButtons = {}
        colorGrid = wx.GridSizer(cols=self.NUM_COLS,hgap=2,vgap=2)
        for eachColor in self.colorList:
            b = buttons.GenToggleButton(self,-1,eachColor[:2],size=buttonSize)
            b.SetBezelWidth(1)
            b.SetUseFocusIndicator(False)
            self.Bind(wx.EVT_BUTTON,self.setColor,b)
            colorGrid.Add(b,0)
            self.colorMap[b.GetId()] = eachColor
            self.colorButtons[eachColor] = b
        self.colorButtons[self.colorList[0]].SetToggle(True)
        return colorGrid

    def createThicknessGrid(self,parent,buttonSize):
        self.thicknessMap = {}
        self.thicknessButtons = {}
        thicknessGrid = wx.GridSizer(cols=self.NUM_COLS,hgap=2,vgap=2)
        for eachThickness in range(1,self.maxThickness+1):
            eachToggleButton = buttons.GenToggleButton(self,-1,str(eachThickness),size=buttonSize)
            eachToggleButton.SetBezelWidth(10)
            eachToggleButton.SetUseFocusIndicator(False)
            self.Bind(wx.EVT_BUTTON,self.setThickness,eachToggleButton)
            thicknessGrid.Add(eachToggleButton,0)
            self.thicknessMap[eachToggleButton.GetId()] = eachThickness
            self.thicknessButtons[eachThickness] = eachToggleButton
        self.thicknessButtons[1].SetToggle(True)
        return thicknessGrid

    def setColor(self,event):
        color = self.colorMap[event.GetId()]
        if color != self.paint.color :
            self.colorButtons[self.paint.color].SetToggle(False)
        self.paint.setColor(color)
    def setThickness(self,event):
        thickness = self.thicknessMap[event.GetId()]
        if thickness != self.paint.thickness :
            self.thicknessButtons[self.paint.thickness].SetToggle(False)
        self.paint.setThickness(thickness)