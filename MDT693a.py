import serial.tools.list_ports
import serial
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plist= list(serial.tools.list_ports.comports())
if len(plist)<=0:
    print("No serial port founded!")
else:
    serial_port=list(plist[0])[0]
    MDT693a=serial.Serial(serial_port,baudrate=115200,bytesize=8,stopbits=1,parity='N',timeout=2)
    MDT693a.setDTR(True)
    MDT693a.setRTS(True)
    MDT693a.setRTS(False)
    MDT693a.setDTR(False)
    print("Serial port found: "+MDT693a.name)
MDT693a.write("ZV?".encode())
print(bytes.decode(MDT693a.read_all()))
MDT693a.close()