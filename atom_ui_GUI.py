import wx
import time
#import os
from MDSocketsForPython3 import MDSocket


class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='EVA100 UI')
        
        #panel = wx.Panel(self)      

        #my_sizer = wx.BoxSizer(wx.VERTICAL)   
        def on_update_press(event):
            self.static_text_status.SetLabel("Working.....")

            text_in_set=self.my_text_ctrl_set.Value
            if text_in_set=="update for value":         # for the first ime just read
                result=s.ReadMI("0699")
                set_point=int(result.split(",")[1])
                set_point=str(set_point/10)
            else:
                new_val=float(text_in_set)*10
                new_val=int(new_val)
                new_val=str(new_val)
                new_val=new_val.zfill(4)
                print (new_val)
                print(s.WriteMI("0699",new_val))
                result=s.ReadMI("0699")
                set_point=int(result.split(",")[1])
                set_point=str(set_point/10)



            self.my_text_ctrl_set.SetLabel(set_point)
            result=s.ReadMI("0006")

            actual_temp=int(result.split(",")[1])
            actual_temp=str(actual_temp/10)

            self.my_text_ctrl_actual.SetLabel(actual_temp)
            self.static_text_status.SetLabel("Updated.")
       
        def onClose(event):
            print ("closing the app")
            s.disconnect()
            self.Close()

        def timer_update(event):
            print("timer went off")
            self.static_text_status.SetLabel("Working.....")

            converged=s.ReadMB("0083")             # see if it is converged
            print(converged)

            if 0:
                result=s.ReadMI("0699")
                set_point=int(result.split(",")[1])
                set_point=str(set_point/10)
                self.my_text_ctrl_set.SetLabel(set_point)

                result=s.ReadMI("0006")
                actual_temp=int(result.split(",")[1])
                actual_temp=str(actual_temp/10)
                self.my_text_ctrl_actual.SetLabel(actual_temp)

            self.static_text_status.SetLabel("Updated. temp is converged")

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
        self.my_text_ctrl_set= wx.TextCtrl(panel1,pos=(5,25),value="update for value")   
        my_btn = wx.Button(panel1, label='update', pos=(5,135))
        my_btn.Bind(wx.EVT_BUTTON, on_update_press)

        self.static_text_set_temp=wx.StaticText(panel1, -1,
                       "Actual temp:",
                        (1,60), style=wx.ALIGN_LEFT)
        self.my_text_ctrl_actual= wx.TextCtrl(panel1,pos=(5,80),value="update for value") 
        self.my_text_ctrl_actual.SetBackgroundColour(wx.LIGHT_GREY)
        
        self.static_text_status=wx.StaticText(panel1, -1,
                        "",
                        (1,110), style=wx.ALIGN_LEFT)

        closeBtn = wx.Button(panel1, label="Close", pos=(5,165))

        closeBtn.Bind(wx.EVT_BUTTON, onClose)
########  add a timer ############
        if 0:
            self.myTimer=wx.Timer(self)
            self.Bind(wx.EVT_TIMER,timer_update)
            self.myTimer.Start(10000)

#################################

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