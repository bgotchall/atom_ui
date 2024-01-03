import serial
import time

arduino = serial.Serial(port='COM4',   baudrate=9600, timeout=.1)



def write_read(x):
    arduino.write(bytes(x,   'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return   data

print(write_read("hi"))
print(write_read("hi"))
print(write_read("hi"))
print(write_read("hi"))
print(write_read("hi"))




num=""
print ("When working properly the Arduino will have echoed back Ready to flip some switches and Firmware version number above this message.")
while num != "X" and num !="x":
    #num=""
    value=""
    num = input("Enter a number 1 (vac on) or 0 (vac off) (x to exit): ")
    #num=num.strip()
    if num != "X" and num !="x": value   = write_read(num)

    if num == "1":
        print("Vacuum is on")
    elif num == "x":
        print ("Normal exit.  Vacuum line is left in previous state.")
    else:
        print("Vacuum is off")
    #time.sleep(0.5)
    #print(value.strip())
    #print(arduino.readline())

