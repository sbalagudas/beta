import wx
from DBOperation import DBOperation as dbo
import time
import common as cmm
import fonts
import Main
import enDecryption as ed

class logInPanel(wx.Panel):
    def __init__(self,
                 parent,
                 ID,
                 pos=wx.DefaultPosition,
                 size=(600,400)):
        wx.Panel.__init__(self,parent,ID,pos,size)
        self.frame = parent

        #self.backgroundImage()
        self.fontBold = wx.Font(18,wx.ROMAN,wx.ITALIC,wx.BOLD)
        self.bgColor = self.GetBackgroundColour()

        self.createLoginButton()
        self.createPromptText()

        (textSizer,self.textList) = cmm.createStaticTextControl(self,self.textInfo(),fonts.Fonts.romanBold16())
        for item in self.textList:
            item.SetForegroundColour('Blue')
        self.SetBackgroundColour('#CCFFCC')
        self.layout(textSizer)

    def createLoginButton(self):
        self.loginBtn = wx.Button(self,label="Log In",size=(100,50))
        self.loginBtn.SetFont(fonts.Fonts.romanBold18())
        self.loginBtn.SetForegroundColour('Blue')
        self.loginBtn.Bind(wx.EVT_BUTTON,self.authentication,self.loginBtn)
    def createPromptText(self):
        self.pmt = wx.StaticText(self,id=-1,label="",size=(400,50))
        self.pmt.SetFont(self.fontBold)
        self.pmt.SetForegroundColour('RED')

    def textInfo(self):
        return [("User Name : ",wx.ROMAN,'static'),
                (wx.TE_NOHIDESEL,'ctrl'),
                ("Password : ",wx.ROMAN,'static'),
                (wx.TE_PASSWORD|wx.TE_PROCESS_ENTER,'ctrl')]

    def layout(self,textSizer):
        boxSizer = wx.BoxSizer(wx.VERTICAL)
        boxSizer.Add((0,20))
        boxSizer.Add(textSizer,1,wx.EXPAND|wx.ALL,5)
        boxSizer.Add(self.pmt,0,wx.ALIGN_CENTER|wx.EXPAND,5)
        boxSizer.Add(self.loginBtn,0,wx.ALIGN_CENTER|wx.ALL,5)
        boxSizer.Add((0,20))

        self.SetSizer(boxSizer)
        self.Layout()

    def authentication(self,event):
        db = dbo()
        #db.initialization()
        #print "self.textList : ",self.textList
        self.userName = self.textList[1].GetLabelText()
        #print "user name : ",self.userName
        password = self.textList[3].GetLabelText()
        #print "password : ",password
        enUserName = ed.enDecryption.encryption(self.userName)
        enUserName.strip()
        dbPwd = db.getBanana(enUserName)

        #need decryption process, will add later.
        if dbPwd :
            #print "ed.enDecryption.decryption(dbPwd[0][0])",ed.enDecryption.decryption(dbPwd[0][0])
            if ed.enDecryption.decryption(dbPwd[0][0]) == password:
                self.pmt.SetLabel("log in success!")
                time.sleep(1)
                self.frame.Destroy()
                self.mainFrame = Main.mainFrame()
                self.mainFrame.Show()
            else :
                self.pmt.SetLabel("invalid username or password.")
        else :
            self.pmt.SetLabel("invalid username or password.")

class loginApp(wx.App):
    def __init__(self,redirect=False,filename=None):
        wx.App.__init__(self,redirect,filename)
    def OnInit(self):
        self.loginFrame = logInFrame()
        self.SetTopWindow(self.loginFrame)
        self.loginFrame.Show()

        return True

class logInFrame(wx.Frame) :
    def __init__(self,
                 parent=None,
                 id=-1,
                 title="log in window",
                 pos=wx.DefaultPosition,
                 size=(400,300),
                 style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER | wx.MINIMIZE_BOX |wx.MAXIMIZE_BOX)):
        wx.Frame.__init__(self,parent,id,title,pos,size,style)

        self.panel = logInPanel(self,-1)

if __name__ == "__main__":
    app = loginApp()
    app.MainLoop()