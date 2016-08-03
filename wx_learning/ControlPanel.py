import wx

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

class ControlPanel(wx.Panel):
    def __init__(self) :
