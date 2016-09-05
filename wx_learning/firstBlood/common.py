import wx

def createStaticTextControl(parent,textInfo):
    sizer = wx.FlexGridSizer(cols=2,hgap=6,vgap=6)
    textList = []
    for eachItem in textInfo:
        if 'static' in eachItem :
            text = wx.StaticText(parent,id=-1,label=eachItem[0],style=eachItem[1])
        else :
            text = wx.TextCtrl(parent,id=-1,size=(200,-1),style=eachItem[0])
        textList.append(text)
    sizer.AddMany(textList)
    #self.paintWindow.SetSizer(sizer)
    return (sizer,textList)
