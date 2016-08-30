import wx

class Paint(wx.Window):
    def __init__(self,parent,ID,pos=(0,0),size=(400,600)):
        wx.Window.__init__(self,parent,ID,pos,size)
        self.SetBackgroundColour('White')
        self.color='Black'
        self.thickness = 1
        #1
        self.pen = wx.Pen(self.color,self.thickness,wx.SOLID)

        self.lines = []
        self.curLine = []
        self.pos = (0,0)
        self.initBuffer()

        #bind the events  2
        self.Bind(wx.EVT_LEFT_DOWN,self.onLeftDown)
        self.Bind(wx.EVT_LEFT_UP,self.onLeftUp)
        self.Bind(wx.EVT_MOTION,self.onMotion)
        self.Bind(wx.EVT_SIZE,self.onSize)
        self.Bind(wx.EVT_IDLE,self.onIdle)
        self.Bind(wx.EVT_PAINT,self.onPaint)

    def initBuffer(self):
        size = self.GetClientSize()
        #3
        self.buffer = wx.EmptyBitmap(size.width,size.height)
        dc = wx.BufferedDC(None,self.buffer)
        #4
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        #dc.SetBackground(wx.Brush('Green'))
        dc.Clear()
        self.drawLines(dc)
        self.reInitBuffer = False

    def getLinesData(self):
        return self.lines[:]

    def setLinesData(self,lines):
        self.lines = lines[:]
        self.initBuffer()
        self.Refresh()

    #event handlers definition.

    def onLeftDown(self,event):
        self.curLine = []
        #5
        self.pos = event.GetPositionTuple()
        #print "pos :",self.pos
        #6
        self.CaptureMouse()

    def onLeftUp(self,event):
        if self.HasCapture():
            self.lines.append((self.color,self.thickness,self.curLine))
            #print self.lines
            self.curLine = []
            #7
            self.ReleaseMouse()

    def onMotion(self,event):
        #8
        if event.Dragging() and event.LeftIsDown():
            #9
            dc = wx.BufferedDC(wx.ClientDC(self),self.buffer)
            self.drawMotion(dc,event)
        event.Skip()
    #10
    def drawMotion(self,dc,event):
        dc.SetPen(self.pen)
        newPos = event.GetPositionTuple()
        coords = self.pos + newPos
        self.curLine.append(coords)
        dc.DrawLine(*coords)
        self.pos = newPos
    #12
    def onIdle(self,event):
        if self.reInitBuffer :
            self.initBuffer()
            self.Refresh()
    def onSize(self,event):
        #11
        self.reInitBuffer = True

    def onPaint(self,event):
        #13
        dc = wx.BufferedPaintDC(self,self.buffer)

        #14
    def drawLines(self,dc):
        for color, thickness,line in self.lines:
            pen = wx.Pen(color,thickness,wx.SOLID)
            dc.SetPen(pen)
            for coords in line :
                dc.DrawLine(*coords)
        #pen = wx.Pen('Cyan',5,wx.SOLID)
        #dc.SetPen(pen)
        #dc.DrawCircle(150,200,100)
        #dc.DrawRectangle(150,200,50,30)
        #dc.DrawText('sbalagudas',50,50)
        #dc.DrawBitmap(wx.Bitmap('aaa'),50,50,False)

    def setColor(self,color):
        self.color = color
        self.pen = wx.Pen(self.color,self.thickness,wx.SOLID)
    def setThickness(self,num):
        self.thickness = num
        print "num : ",num
        self.pen = wx.Pen(self.color,self.thickness,wx.SOLID)

class Frame(wx.Frame):
    def __init__(self,parent=None,id=-1,title='painting...',pos=wx.DefaultPosition,size=(800,600)):
        wx.Frame.__init__(self,parent,id,title,pos,size)
        #self.pt = Paint(self,-1,(0,0),(399,600))
        self.pt = Paint(self,-1,(0,0))
        #self.ptNew = paint(self,-1,(401,0),(399,600))
        self.thicknessValue = ['1','2','3','4','5']
        self.colorValue = ['Red','Green','Blue','Purple','Pink']

        self.buttonLeft = wx.Button(self.pt,label="left")
        self.buttonRight = wx.Button(self.pt,label="right",pos=(self.buttonLeft.GetSize()[0]+1,self.buttonLeft.GetPosition()[1]))

        #self.thick = wx.ComboBox(self.pt,-1,'thickness',(20,20),(100,30),self.thicknessValue,wx.CB_DROPDOWN and wx.CB_READONLY)
        #self.color = wx.ComboBox(self.pt,-1,'color',(140,20),(100,30),self.colorValue,wx.CB_DROPDOWN and wx.CB_READONLY)

        #self.thickNew = wx.ComboBox(self.ptNew,-1,'thickness',(140,20)
        # ,(100,30),self.thicknessValue,wx.CB_DROPDOWN and wx.CB_READONLY)
        #self.colorNew = wx.ComboBox(self.ptNew,-1,'color',(260,20),(100,30),self.colorValue,wx.CB_DROPDOWN and wx.CB_READONLY)

        #self.Bind(wx.EVT_COMBOBOX,self.setColour,self.color)
        #self.Bind(wx.EVT_COMBOBOX,self.setThickness,self.thick)

        #create status bar
        self.pt.Bind(wx.EVT_MOTION,self.statusBarMethod)
        self.statusBar = self.CreateStatusBar()
        self.statusBar.SetFieldsCount(2)
        self.statusBar.SetStatusWidths([-1,-3])


    def statusBarMethod(self,event):
        self.statusBar.SetStatusText(str(event.GetPositionTuple()),0)
        if event.GetPositionTuple() == (400,400):
            msg = "ya, you got the point!!!"
            self.statusBar.SetStatusText(msg+str(event.GetPositionTuple()),1)
        event.Skip()
    def setThickness(self,event):
        newThick = self.thick.GetSelection()
        newThick = int(newThick)
        self.pt.setThickness(newThick)
    def setColour(self,event):
        #newColor = self.color.GetSelection()
        newColor = self.color.GetValue()
        self.pt.setColor(newColor)






if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = Frame()
    frame.Show()
    app.MainLoop()