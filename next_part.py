import telnetlib
#import asyncio, telnetlib3
import time
#import getpass
import subprocess
import pyvisa

rm=pyvisa.ResourceManager()
print(rm.list_resources())
my_instrument = rm.open_resource('GPIB0::4::INSTR')
print(my_instrument.query('*IDN?'))
print(my_instrument.query('RFT?'))          # zero means yes, a part is ready.  1 means no
print(my_instrument.query('BIN1'))         # this works.  tells the handler to move on.
time.sleep(1)

