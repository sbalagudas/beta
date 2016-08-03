import wx
import wx.py.images as images

class ToolbarFrame(wx.Frame):
    def OnPrintMe(self,event):
        print "hello, button"

    def __init__(self,parent,id,title="Toolbars",pos=wx.DefaultPosition,size=(600,400)):
        wx.Frame.__init__(self,parent,id,title,pos,size)

        panel = wx.Panel(self)
        panel.SetBackgroundColour("Dark Green")
        statusBar = self.CreateStatusBar()
        toolBar = self.CreateToolBar()
        toolBar.AddSimpleTool(wx.NewId(),images.getPyBitmap(),"New","long Help for 'New'")
        toolBar.Realize()

        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menuBar.Append(menu1,"&File")
        menu2 = wx.Menu()
        menu2.Append(wx.NewId(),"&Copy","Copy in status bar")
        menu2.Append(wx.NewId(),"C&ut","xxx")
        menu2.Append(wx.NewId(),"Paste","yyy")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(),"&Options","Display Options")
        menuBar.Append(menu2,"Edit")
        menu3 = wx.Menu()
        menu3.Append(wx.NewId(),"apple","apple juice")
        menuBar.Append(menu3,"fruits")
        self.SetMenuBar(menuBar)

        button = wx.Button(panel,label="Hello",pos=(300,100),size=(200,200))
        self.Bind(wx.EVT_BUTTON,self.OnPrintMe,button)
        self.Bind(wx.EVT_BUTTON,self.OnPrintMe,toolBar)

        dlg = wx.MessageDialog(None,"do you want to close the window ?","Message Box",wx.OK|wx.CANCEL)
        result = dlg.ShowModal()
        dlg.Destroy()

class ButtonApp(wx.App):
    def __init__(self,redirect=False,filename=None):
        wx.App.__init__(self,redirect,filename)

    def OnInit(self):
        image=wx.Image("d:\\JellyFish.jpg",wx.BITMAP_TYPE_JPEG)
        self.frame = ToolbarFrame(None,-1)
        #self.frame = Frame(None,-1)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ =='__main__':
    app = ButtonApp()
    app.MainLoop()