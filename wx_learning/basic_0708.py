import wx
import threading
import multiprocessing as mp
import time

class Frame(wx.Frame):
    def __init__(self,parent=None,id=-1,title="events",pos=wx.DefaultPosition,size=(400,200)):
        wx.Frame.__init__(self,parent,id,title,pos,size)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("Dim Grey")

        self.btnLeft = wx.Button(self.panel,label="Left Button",pos=(10,30),size=(100,30))
        self.btnLeft.SetBackgroundColour('Medium Turquoise')
        self.btnRight = wx.Button(self.panel,label="Right Button",pos=(10,60),size=(100,30))
        self.btnRight.SetBackgroundColour('Medium Turquoise')

        #button definition.
        self.btnLeft.Bind(wx.EVT_ENTER_WINDOW,self.enterWindowLeft)
        self.btnLeft.Bind(wx.EVT_LEAVE_WINDOW,self.leaveWindowLeft)
        self.btnRight.Bind(wx.EVT_ENTER_WINDOW,self.enterWindowRight)
        self.btnRight.Bind(wx.EVT_LEAVE_WINDOW,self.leaveWindowRight)
        #self.Bind(wx.EVT_BUTTON,self.countDownFunc,self.btnLeft)
        self.Bind(wx.EVT_BUTTON,self.multiThread,self.btnLeft)
        #static text definition
        self.text=wx.StaticText(self.panel,id=wx.NewId(),label = "00:00:10",pos=(120,30),size=(100,20),name='staticText')
        self.text.SetBackgroundColour('White')
        self.text.SetForegroundColour('Forest Green')
        self.panel.Refresh()

    def multiProcess(self,event):
        process = mp.Process(target=self.countDownFunc)
        process.start()
        process.join()

    def multiThread(self,event):
        print "multi thread starts..."
        thd = threading.Thread(target=self.countDownFunc)
        thd.start()
        thd.join()
        print "multi thread ended..."

    def closeWindow(self,event):
        pass

    def leftDown(self,event):
        print "left down..."
        event.Skip()

    def countDownFunc(self):
        print "for loop starts..."
        for i in range(10):
            print "value %s ..."%i
            current = str(10 - i)
            print "current : %s"%current

            self.text.SetLabel("time : "+current)
            print "set label ended..."
            time.sleep(1)
        print "for loop ended..."

    def enterWindowLeft(self,event):
        self.btnLeft.SetLabel('Lok\' Tar')
        self.btnLeft.SetBackgroundColour('Cyan')
    def leaveWindowLeft(self,event):
        self.btnLeft.SetLabel('Orgar!')
        self.btnLeft.SetBackgroundColour('Medium Turquoise')

    def enterWindowRight(self,event):
        self.btnRight.SetLabel('Glory')
        self.btnRight.SetBackgroundColour('Cyan')
    def leaveWindowRight(self,event):
        self.btnRight.SetLabel('For Sin\'dorei!')
        self.btnRight.SetBackgroundColour('Medium Turquoise')

class MyApp(wx.App):
    def __init__(self,redirect = False,filename =None):
        wx.App.__init__(self,redirect,filename)

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        #self.countDown(self.frame)
        return True
    def countDown(self,frame):
        frame.countDownFunc()

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()