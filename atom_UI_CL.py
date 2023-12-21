import telnetlib
import time
#import getpass
import subprocess
import pyvisa

 
rm=pyvisa.ResourceManager()
print(rm.list_resources())
my_instrument = rm.open_resource('GPIB0::4::INSTR')
print(my_instrument.query('*IDN?'))
print(my_instrument.query('RFT?'))          # zero means yes, a part is reaady.  1 means no
#print(my_instrument.query('BIN1'))         # this works.  tells the handler to move on.
time.sleep(1)
print(my_instrument.query('RFT?')) 
time.sleep(1)
print(my_instrument.query('RFT?')) 

if 0:
    subprocess.run(["ls","-l"])
    subprocess.run(["ateliercmd", "-getrevision"])

############################################

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

    if 1:
        print("writing the command")
        #tn.write(user.encode('ascii') + b"mMI0699?\n")
        tn.write(b"mMI0699?\n")
        #print(tn.read_all())
        print ("attempting to read")
        print(tn.read_until(b"MI0699"),4)
    


    print ("attempting to close")
    tn.close()

######################################################################