import serial
import time

arduino = serial.Serial(port='COM3',   baudrate=115200, timeout=1)



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


print ("When working properly the Arduino will have echoed back Ready to flip some switches and Firmware version number above this message.")
while num != "X" and num !="x":
    arduino.flush
    num = input("Enter a number 1 (vac on) or 0 (vac off) (x to exit): ")
    
    if 1:
        if num == "1":
            print("Vacuum is on")
            print(write_read("1"))
        elif num == "x":
            print ("Normal exit.  Vacuum line is left in previous state.")
        else:
            print("Vacuum is off")
            print(write_read("0"))
   

arduino.flush
arduino.close