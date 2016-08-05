import wx

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
        colorGrid =

    def createColorGrid(self,parent,buttonSize):
        self.colorMap = {}
        self.colorButtons = {}
        colorGrid = wx.GridSizer(cols=self.NUM_COLS,)