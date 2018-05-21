import serial.tools.list_ports
import serial
import sys
import time
import struct
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

MDT693a=serial.Serial("COM5",baudrate=115200,bytesize=8,stopbits=1,parity='N',timeout=5)
MDT693a.setDTR(True)
MDT693a.setRTS(True)
MDT693a.setRTS(False)
MDT693a.setDTR(False)
MDT693a.write(bytes().fromhex('050000002101'))
result=MDT693a.readall()
serial_number=struct.unpack('<L', bytes(result[6:10]))[0]
print(serial_number)
MDT693a.close()