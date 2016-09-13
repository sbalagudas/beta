import wx

class timeSelectionPanel(wx.Panel):
    def __init__(self,parent,id):
        wx.Panel.__init__(self,parent,id)

        self.cbxList = []
        cbSizer = wx.BoxSizer(wx.HORIZONTAL)
        for i in range(3):
            cmb = wx.ComboBox(parent=self,id=-1,value='-',choices='',style=wx.CB_DROPDOWN)
            cbSizer.Add(cmb,1,wx.EXPAND)
            self.cbxList.append(cmb)
        self.SetSizer(cbSizer)

class Frame(wx.Frame):
    def __init__(self,parent=None,id=-1,title='time selection',pos=wx.DefaultPosition,size=(600,400)):
        wx.Frame.__init__(self,parent,id,title,pos,size)
        panel = timeSelectionPanel(self,-1)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = Frame()
    frame.Show()
    app.MainLoop()