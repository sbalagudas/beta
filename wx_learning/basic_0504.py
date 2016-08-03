import wx
import sys

class Frame(wx.Frame):
    def __init__(self,parent,id,title):
        print "Frame initialized..."
        wx.Frame.__init__(self,parent,id,title)

class MyFrame(wx.Frame):
    def __init__(self,image,parent=None,id=-1,pos=wx.DefaultPosition,title='frame of MyFrame'):
        print "Frame initialized..."
        temp = image.ConvertToBitmap()
        size = 800,600
        #size = temp.GetWidth(),temp.GetHeight()
        wx.Frame.__init__(self,parent,id,title,pos,size)
        self.bmp = wx.StaticBitmap(parent=self,bitmap=temp)

class App(wx.App):
    def __init__(self,redirect=False,filename='d:\\python_redirect.txt'):
        print "App initialized..."
        wx.App.__init__(self,redirect,filename)

    def OnInit(self):
        image = wx.Image('d:\\Jellyfish.jpg',wx.BITMAP_TYPE_JPEG)
        print "OnInit called..."
        #self.frame = Frame(parent=None,id=-1,title="frame in app")
        self.frame = Frame(None,-1,"frame in app")
        #self.frame = MyFrame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print >> sys.stderr, "pretended error message..."
        return True

    def OnExit(self):
        print "OnExit called..."

if __name__ == '__main__':
    app = App(redirect=True)
    print "before main loop"
    app.MainLoop()
    print "after main loop"