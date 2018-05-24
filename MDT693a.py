import serial.tools.list_ports
import serial
import sys
import time
import struct
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

MDT693a=serial.Serial("COM6",baudrate=115200,bytesize=8,stopbits=1,parity='N',timeout=1)
#MDT693a.setDTR(True)
#MDT693a.setRTS(True)
#MDT693a.setRTS(False)
#MDT693a.setDTR(False)
result=0
MDT693a.write(bytes().fromhex('050000002101'))
result=MDT693a.readline()
serial_number=struct.unpack('<L', bytes(result[6:10]))[0]
print(serial_number)
#MDT693a.write(bytes().fromhex('400601032101'))
MDT693a.write(bytes().fromhex('410601002101'))
result=MDT693a.readline()
print([hex(x) for x in result])
#time.sleep(1)
MDT693a.write(bytes().fromhex('43060400D00101001717'))
#time.sleep(1)
MDT693a.write(bytes().fromhex('440601002101'))
result=MDT693a.readline()
print([hex(x) for x in result])
MDT693a.close()