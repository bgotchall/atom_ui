import telnetlib
#import asyncio, telnetlib3
import time
#import getpass
import subprocess
import pyvisa




#################################################
# actual rudimentary UI that just runs the tester for the one "tray".  pseudocode below:
#Load program
#(operator hits the start button)
#If (RFT=0):
#               Start test flow
#               Get test result
#               Set bin1 or bin 2
#End if
rm=pyvisa.ResourceManager()
print("attempting to open GPIB")
try:

    print("GPIB resources available:      ",rm.list_resources())
    my_instrument = rm.open_resource('GPIB0::4::INSTR')
    
    print("Handler ID query:       " + my_instrument.query('*IDN?'))
    print("UI starting.  The program should be loaded and the correct temperature set.  Enter to continue")
    a=input()
    print("Enter name of .STDF logfile")
    a=input()
    
    name=a + ".stdf"
    print(name)
    subprocess.run(["ls","-l"])
    #subprocess.run(["ateliercmd", "-getrevision"])
    #subprocess.run(["ateliercmd", "-stdf open " + name])

    a=my_instrument.query('RFT?')       # RFT=0 means, yes there is a part ready.
    if a==0:
        subprocess.run(["ateliercmd", "-start"])     #start the flow.  might need to do a connect command first
        temp=subprocess.run(["ateliercmd", "-getdutstatus"])                                       # -getdutstatus
        print("output of dut status was:   ", temp)

    




except:
    print("No GPIB or some other error.")



######################################################

if 0: 
    rm=pyvisa.ResourceManager()
    print(rm.list_resources())
    my_instrument = rm.open_resource('GPIB0::4::INSTR')
    print(my_instrument.query('*IDN?'))
    print(my_instrument.query('RFT?'))          # zero means yes, a part is ready.  1 means no
    #print(my_instrument.query('BIN1'))         # this works.  tells the handler to move on.
    time.sleep(1)
    print(my_instrument.query('RFT?')) 
    time.sleep(1)
    print(my_instrument.query('RFT?')) 

if 0:
    subprocess.run(["ls","-l"])
    subprocess.run(["ateliercmd", "-getrevision"])

############################################
#HOST ="www.sigmasense.com"
#tn=telnetlib.Telnet(HOST,"80")
#tn.write(b"ping\n")
#print(tn.read_all())





if 0:
    HOST = "10.109.10.20, port=5000"
    #user = input("USERNAME: ")
    #password = getpass.getpass()
    
    tn = telnetlib.Telnet()
    tn.open("10.109.10.20",5000,5)
    time.sleep(0.5)
    #tn.read_until(b"login: ")
    #tn.write(user.encode("ascii")+b"\n")
    #tn.read_until(b"Password: ")
    #tn.write(password.encode("ascii")+b"\n")
    #tn.write(b"exit\n")
    #print("interact")
    #tn.interact()

    if 0:
        print("writing the command")
        #tn.write(user.encode('ascii') + b"mMI0699?\n")
        tn.write(b"mMI0699?\n")
        
        print ("attempting to read")
        print(tn.read_all())
        #print(tn.read_until(b"MI0699"),4)
    


    print ("attempting to close")
    tn.close()

######################################################################