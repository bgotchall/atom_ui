import wx
from MDSocketsForPython3 import MDSocket


class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='EVA100 UI')
        
        #panel = wx.Panel(self)      

        #my_sizer = wx.BoxSizer(wx.VERTICAL)   
        def on_press(event):
            set_point=s.ReadMI("0699")
            self.my_text_ctrl_set.SetLabel(set_point)
            actual_temp=s.ReadMI("0006")
            self.my_text_ctrl_actual.SetLabel(actual_temp)
       
        def onClose(event):
            print ("closing the app")
            s.disconnect()
            self.Close()    
#####
        splitter=wx.SplitterWindow(self,-1)
        splitter.SetMinimumPaneSize(20)
        panel1 = wx.Panel(splitter, -1)
        panel1.SetBackgroundColour(wx.LIGHT_GREY)
        
        self.static_text_set_temp=wx.StaticText(panel1, -1,
                       "Set Temp:",
                        (1,1), style=wx.ALIGN_LEFT)
        panel2 = wx.Panel(splitter, -1)
        panel2.SetBackgroundColour(wx.YELLOW)

        splitter.SplitVertically(panel1, panel2,150)

######
        #self.text_ctrl = wx.TextCtrl(panel1,pos=(5,25))
        self.my_text_ctrl_set= wx.TextCtrl(panel1,pos=(5,25),value="null")   
        my_btn = wx.Button(panel1, label='update', pos=(5,135))
        my_btn.Bind(wx.EVT_BUTTON, on_press)

        self.static_text_set_temp=wx.StaticText(panel1, -1,
                       "Actual temp:",
                        (1,60), style=wx.ALIGN_LEFT)
        self.my_text_ctrl_actual= wx.TextCtrl(panel1,pos=(5,80),value="null") 
        self.my_text_ctrl_actual.SetBackgroundColour(wx.LIGHT_GREY)
        
        closeBtn = wx.Button(panel1, label="Close", pos=(5,165))

        closeBtn.Bind(wx.EVT_BUTTON, onClose)


        self.Show()


        



class MyApp(wx.App):
    def OnInit(self):
        frame=MyFrame()
        frame.Show(True)
        self.SetTopWindow(frame)
        return True
    
    



if __name__ == '__main__':
    app = MyApp(0)
    #frame = MyFrame()
    print("doing stuff in main app")
    ip_addr="10.109.10.20"
    tcp_port=5000
    timeout_secs = 3
    s=MDSocket(ip_addr,tcp_port,timeout_secs)
    print('Connecting...')
    s.connect()


    app.MainLoop()