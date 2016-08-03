import wx

class ButtonFrame(wx.Frame):
    def OnCloseMe(self,event):
        self.Close(True)

    def OnCloseWindow(self,event):
        self.Destroy()

    def OnPrintMe(self,event):
        print "hello, button"
    def __init__(self,
                 image,
                 parent=None,
                 id=100,
                 title="window with button",
                 pos=wx.DefaultPosition,
                 size=(300,100),
                 style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MINIMIZE_BOX |wx.MAXIMIZE_BOX)):
        temp = image.ConvertToBitmap()
        wx.Frame.__init__(self,parent,id,title,pos,size,style)
        self.bmp = wx.StaticBitmap(parent=self,bitmap=temp)
        panel = wx.Panel(self)
        button = wx.Button(panel,label="Close",pos=(125,10),size=(50,50))
        self.Bind(wx.EVT_BUTTON,self.OnPrintMe,button)
        self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)
        #self.bmp = wx.StaticBitmap(parent=self,bitmap=temp)

class Frame(wx.Frame):
    def OnCloseMe(self,event):
        self.Close(True)

    def OnPrintMe(self,event):
        print "hello, button"

    def OnCloseWindow(self,event):
        self.Destroy()

    def __init__(self,
                 parent,
                 id,
                 title="something",
                 pos=wx.DefaultPosition,
                 size=(300,100),
                 style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MINIMIZE_BOX |wx.MAXIMIZE_BOX)):
        wx.Frame.__init__(self,parent,id,title,pos,size,style)
        panel = wx.Panel(self)
        button = wx.Button(panel,label="Close",pos=(125,10),size=(50,50))
        self.Bind(wx.EVT_BUTTON,self.OnCloseMe,button)
        self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)
class ButtonApp(wx.App):
    def __init__(self,redirect=False,filename=None):
        wx.App.__init__(self,redirect,filename)

    def OnInit(self):
        image=wx.Image("d:\\JellyFish.jpg",wx.BITMAP_TYPE_JPEG)
        self.frame = ButtonFrame(image,None,-1)
        #self.frame = Frame(None,-1)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ =='__main__':
    app = ButtonApp()
    app.MainLoop()