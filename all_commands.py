#This is just a command line tool for everything that can be put on a command line.  

from MDSocketsForPython3 import MDSocket            #this is for comms with the temp unit (over ethernet)
import serial                                       #this is for comms with the ardiuno (plain com ports)
import time

#subroutines: #############################################################################################################################

#this is the routine that does I/O to the arduino, for relay control
def arduino_write_read(x):
    arduino.write(bytes(x,   'utf-8'))
    arduino.flush
    time.sleep(0.1)
    #while not arduino.read_until().decode().strip() == 'Listening.': pass
    #data = arduino.readline()                                              # old version that works for numbers, or one char
    data = arduino.readline().decode('utf-8').rstrip()                      #this is the version for text.
    return   data




#startup section.  Initialize all HW, set things up. #####################################################################################
print("setting up HW; initializing.")
arduino_present=0
if arduino_present:
    arduino = serial.Serial(port='COM3',   baudrate=115200, timeout=1)
    # This works with "Relay_control_4x_July_16_2024.ino" to program the arduino.  The attached Ardunio needs to be programmed with this code to work.

    print(arduino_write_read("hi"))             #these are to give the arduino a chance to spit out its hardcoded welcome messages.  The input here is ignored.
    print(arduino_write_read("hi"))
    print(arduino_write_read("hi"))
    print(arduino_write_read("hi"))

# now set up the port to talk to temp unit:
if 1:
    #socket info
    ip_addr="10.109.10.20"
    tcp_port=5000
    timeout_secs = 3
    s=MDSocket(ip_addr,tcp_port,timeout_secs)
    print('Connecting...')
    s.connect()



#main loop:  #########################################################################################################################
num=""
print ("When working properly the Arduino will have echoed back \"Ready to flip some switches\" above this message.")
while num != "X" and num !="x":
    if arduino_present: arduino.flush
    print("-------------------------------")
    print("Enter a command")
    print("1= Vacuum toggle")
    print("2= Test site purge air toggle")
    print("3= Send a press of the Start Button")
    print("5= status of the relays")
    print("6= Temp unit: Check Temp setpoint")
    print("6.1= Temp unit: Check Temp actual temp")
    print("6.2= Temp unit: Check Temp is converged to set point")
    print("7= Temp unit: Change the Temp setpoint")
    print("8= Temp unit: Check play on/off")
    print("9= Temp unit: play button on")
    print("9.1= Temp unit: play button off")
    num = input(" (x to exit): ")
    print("-------------------------------")
    
    if 1:
        if num == "1":
            print(arduino_write_read("1"))
        elif num =="2":
            print(arduino_write_read("2"))
        elif num =="3":
            print(arduino_write_read("3"))
        elif num =="5":
            print(arduino_write_read("5"))
            print(arduino_write_read(""))
        elif num =="6":
            result=s.ReadMI("0699")
            print ("result is: ", result)
            my_temp=int(result.split(",")[1])
            my_temp=my_temp/10
            print("Current set point is :" , my_temp, "C")
        elif num =="6.1":
            result=s.ReadMI("0006")
            print ("result is: ", result)
            my_temp=int(result.split(",")[1])
            my_temp=my_temp/10
            print("Current actual temp is :" , my_temp, "C")

        elif num =="6.2":
            result=s.ReadMB("0083")
            print ("converge result is: ", result)
           
        elif num =="7":
            new_val=input("enter the desired set point as a real (ex 25.1): ")
            new_val=float(new_val)*10
            new_val=int(new_val)
            new_val=str(new_val)
            new_val=new_val.zfill(4)
            #print (new_val)
            print(s.WriteMI("0699",new_val))
            print("Verifying new temp set point.")
            result=s.ReadMI("0699")
            my_temp=int(result.split(",")[1])
            my_temp=my_temp/10
            print("New temp set point: ", my_temp, "C")
            
        elif num == "8":
            result=print(s.ReadMB("0020"))
            print ("play button result is: ", result)
            

        elif num == "9":
            print(s.ReadMB("0020"))
            print("enabling run button (0=on, 1=off)")
            print(s.WriteMB("0020",0))              # a 0 is "on", a 1 is "off"

        elif num == "9.1":
            print(s.ReadMB("0020"))
            print("disabling run button (0=on, 1=off)")
            print(s.WriteMB("0020",1))              # a 0 is "on", a 1 is "off"

        elif num == "x":
            print ("Normal exit.  Vac and purge air are left in previous state.")
            
   
# all done.  Close down nicely:  
if arduino_present: arduino.flush
if arduino_present: arduino.close
s.disconnect()