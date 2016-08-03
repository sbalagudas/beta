import wx

class TextEntryBox(wx.Frame):
    def __init__(self,parent=None,id=wx.NewId(),title="Text Practising",pos=wx.DefaultPosition,size=(800,600)):
        wx.Frame.__init__(self,parent,id,title,pos,size)
        panel = wx.Panel(self)
        panel.SetBackgroundColour("Dark Green")
        button1 = wx.Button(panel,label="favourite",pos=(20,20),size=(100,30))
        button1.SetBackgroundColour("Green")
        button2 = wx.Button(panel,label="favourite",pos=(20,50),size=(100,30))
        button2.SetBackgroundColour("Red")
        button3 = wx.Button(panel,label="favourite",pos=(20,80),size=(100,30))
        button4 = wx.Button(panel,label="favourite",pos=(20,110),size=(100,30))
        button4.SetBackgroundColour("Orange")
        self.Bind(wx.EVT_BUTTON,self.addMsg,button1)
        self.Bind(wx.EVT_RIGHT_DOWN,self.simplePrint,button1)
        self.Bind(wx.EVT_BUTTON,self.dlgTest,button2)
        self.Bind(wx.EVT_BUTTON,self.singleChoiceDlg,button3)
    def addMsg(self,event):
        ted = wx.TextEntryDialog(None,"what is your favourite ? ","question box","type something")
        if ted.ShowModal() == wx.ID_OK:
            resp = ted.GetValue()
        if ted.ShowModal() == wx.ID_CANCEL:
            ted.Destroy()
        if resp == "apple":
            dlg = wx.MessageDialog(None,"so do I","congratulations!",wx.OK)
        else :
            dlg = wx.MessageDialog(None,"Different with mine...","sorry!",wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def dlgTest(self,event):
        dlg = wx.MessageDialog(None,'do you want to quit ?','dialogTest',wx.YES_NO|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        if result == wx.ID_YES:
            print "wx.EVT_LEFT_UP : ",wx.EVT_LEFT_UP.typeId
            #print "type of wx.EVT_LEFT_UP : ",type(wx.EVT_LEFT_UP.typeId)
            #print "help of wx.EVT_LEFT_UP : ",help(wx.EVT_LEFT_UP)
            dlg.Destroy()
        else :
            self.addMsg(self)

    def singleChoiceDlg(self,event):
        scdlg = wx.SingleChoiceDialog(None,"what you like","single choice",["apple","banana","pear","lichi","strawberry"])
        if scdlg.ShowModal() == wx.ID_OK:
            resp = scdlg.GetStringSelection()
            print "resp : %s"%resp

    def simplePrint(self,event):
        #statusbar = self.CreateStatusBar()
        print "mouse entered ..."

class MyApp(wx.App) :
    def __init__(self,redirect=False,filename=None):
        wx.App.__init__(self,redirect,filename)

    def OnInit(self):
        self.frame = TextEntryBox(None,-1)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
