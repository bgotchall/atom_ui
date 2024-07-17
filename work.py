####################################################################################
# text or hack-based version of the GUI, prior to front-end dev.  
#
#
####################################################################################

from MDSocketsForPython3 import MDSocket                #for temp forcer comms



if 1:
    #socket info
    ip_addr="10.109.10.20"
    tcp_port=5000
    timeout_secs = 3
    s=MDSocket(ip_addr,tcp_port,timeout_secs)
    print('Connecting...')
    s.connect()
    #print(s.ReadMB("0020"))
    #print(s.ReadMI("0699"))
    result=s.ReadMI("0699")
    print ("result is: ", result)
    
    if "," in result:
        print ("found a comma")
        my_temp=int(result.split(",")[1])
        my_temp=my_temp/10
        print("Current set point is :" , my_temp, "C")

        new_val=input("enter the desired set point as a real (ex 25.1): ")
        new_val=float(new_val)*10
        new_val=int(new_val)
        new_val=str(new_val)
        new_val=new_val.zfill(4)
        print (new_val)
        print(s.WriteMI("0699",new_val))
        result=s.ReadMI("0699")
        my_temp=int(result.split(",")[1])
        my_temp=my_temp/10
        print("new temp set point: ", my_temp, "C")
        print(s.ReadMB("0020"))
        print("enabling run button (0=on, 1=off)")
        print(s.WriteMB("0020",0))              # a 0 is "on", a 1 is "off"


    #print(s.WriteMB("0020",0))
    #print(s.ReadMB("0020"))
    
    
    #print(s.WriteMI("0699","0250"))
    #print(s.ReadMI("0699"))
    s.disconnect()

######################################################################