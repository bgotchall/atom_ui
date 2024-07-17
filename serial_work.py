import serial
import time

arduino = serial.Serial(port='COM3',   baudrate=115200, timeout=.1)


def write_read(x):
    arduino.write(bytes(x,   'utf-8'))
    time.sleep(0.05)
    #data = arduino.readline()
    data = arduino.readline().decode('utf-8').rstrip()                      #this is the version for text.
    return   data


while True:
    this_thing=write_read("")
    if this_thing !="":
        print(this_thing)
    
