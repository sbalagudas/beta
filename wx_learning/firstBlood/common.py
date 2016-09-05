import wx

def createStaticTextControl(parent,textInfo,font):
    sizer = wx.FlexGridSizer(cols=2,hgap=6,vgap=6)
    #horSizer = wx.BoxSizer(wx.HORIZONTAL)
    #verSizer = wx.BoxSizer(wx.VERTICAL)

    textList = []
    for eachItem in textInfo:
        if 'static' in eachItem :
            text = wx.StaticText(parent,id=-1,label=eachItem[0],style=eachItem[1])
        else :
            text = wx.TextCtrl(parent,id=-1,size=(250,-1),style=eachItem[0])
        text.SetFont(font)
        sizer.Add(text,1,wx.EXPAND)
        textList.append(text)

    #sizer.AddMany(textList)
    #self.paintWindow.SetSizer(sizer)
    return sizer,textList
