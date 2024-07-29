import serial
import time

arduino = serial.Serial(port='COM3',   baudrate=115200, timeout=1)
# This works with "Relay_control_4x_July_16_2024.ino" to program the arduino.


def write_read(x):
    arduino.write(bytes(x,   'utf-8'))
    arduino.flush
    time.sleep(0.1)
    #while not arduino.read_until().decode().strip() == 'Listening.': pass
    #data = arduino.readline()                                              # old version that works for numbers, or one char
    data = arduino.readline().decode('utf-8').rstrip()                      #this is the version for text.
    return   data

print(write_read("hi"))             #these are to give the arduino a chance to spit out its hardcoded welcome messages.  The input here is ignored.
print(write_read("hi"))
print(write_read("hi"))
print(write_read("hi"))


num=""


print ("When working properly the Arduino will have echoed back \"Ready to flip some switches\" above this message.")
while num != "X" and num !="x":
    arduino.flush
    print("-------------------------------")
    print("Enter a command")
    print("1= Vacuum toggle")
    print("2= Test site purge air toggle")
    print("3= Send a press of the Start Button")
    print("5= status of the relays")
    num = input(" (x to exit): ")
    print("-------------------------------")
    
    if 1:
        if num == "1":
            print(write_read("1"))
        elif num =="2":
            print(write_read("2"))
        elif num =="3":
            print(write_read("3"))
        elif num =="5":
            print(write_read("5"))
            print(write_read(""))
        elif num == "x":
            print ("Normal exit.  Vac and purge air are left in previous state.")
            
   

arduino.flush
arduino.close