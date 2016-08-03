import wx

class XFrame(wx.Frame): #2
    def __init__(self,
                 image,
                 parent=None,
                 id=-1,
                 pos=wx.DefaultPosition,
                 title='hello Sbalagudas'): #3
        temp = image.ConvertToBitmap()#4
        #size = temp.GetWidth(),temp.GetHeight()
        size = 800,600
        wx.Frame.__init__(self,parent,id,title,pos,size)
        self.bmp = wx.StaticBitmap(parent=self,bitmap=temp)

class MyFrame(wx.Frame):
    '''
    create my own customized Frame style
    '''
    def __init__(self,image,parent=None,id=-1,pos=wx.DefaultPosition,title='frame of MyFrame'):
        temp = image.ConvertToBitmap()
        size = 800,600
        #size = temp.GetWidth(),temp.GetHeight()
        wx.Frame.__init__(self,parent,id,title,pos,size)
        self.bmp = wx.StaticBitmap(parent=self,bitmap=temp)

class TestFrame(MyFrame):
    pass

class MyApp(wx.App):
    def OnInit(self):
        image = wx.Image('d:\\hb.jpg',wx.BITMAP_TYPE_JPEG)
        image1= wx.Image('d:\\Jellyfish.jpg',wx.BITMAP_TYPE_JPEG)
        self.frame = MyFrame(image)
        self.frame.Show()
        self.frame1 = TestFrame(image)
        self.frame1.Show()
        self.SetTopWindow(self.frame1)
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()