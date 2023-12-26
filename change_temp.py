from MDSocketsForPython3 import MDSocket



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
        print ("number is: ", result.split(",")[1])
    
    
    #print(s.WriteMB("0020",0))
    #print(s.ReadMB("0020"))
    
    
    #print(s.WriteMI("0699","0250"))
    #print(s.ReadMI("0699"))
    s.disconnect()

######################################################################