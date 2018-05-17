import serial.tools.list_ports
import serial
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Initialize plot
length=1500
plt.axis([0,length,0.8,1.4])
#fig = plt.gcf()
#fig.set_size_inches(9.5, 6.5)
#plt.axis([0,200,0,60])
#plt.ion()
temp_array=np.zeros(100)
temp_array=temp_array+20
plt.figure(figsize=(15,10)) 
#plt.plot(temp_array)
""" temp_array2=temp_array
fig,ax=plt.subplots()
line,=ax.plot(temp_array)
ax.set_ylim(0,100)
plt.grid(True)
ax.set_xlabel("time: s")
ax.set_ylabel("temperature") """

"""def update(frame):
    global temp_array
    global temp_array2
    global line
    global temperature

    temp_array[0:-1]=temp_array2[1:]
    temp_array[-1]=temperature
    temp_array2=temp_array
    line.set_ydata(temp_array)
    return line
    """

plist= list(serial.tools.list_ports.comports())
if len(plist)<=0:
    print("No serial port founded!")
else:
    serial_port=list(plist[0])[0]
    USART=serial.Serial(serial_port,baudrate=9600,bytesize=8,stopbits=1,parity='N',timeout=None)
    USART.setDTR(True)
    USART.setRTS(True)
    USART.setRTS(False)
    USART.setDTR(False)
    print("Serial port found: "+USART.name)
"""while 1:
#USART.open()
    humi_str=bytes.decode(USART.read(10))
    humidity=float(humi_str[5:])
    temp_str=bytes.decode(USART.read(10))
    temperature=float(temp_str[5:])
    #sys.stdout.write(humi_str+' '+temp_str)
    #sys.stdout.write("\r")
    temp_array[0:-1]=temp_array[1:]
    temp_array[-1]=humidity
    plt.clf()
    plt.plot(temp_array)
    plt.pause(0.1)
#USART.close()"""
adc_count=0
adc_array=np.zeros(length)
dac_array=np.zeros(length)
for adc_count in range(0,length):
    adc_str=bytes.decode(USART.read(10))
    dac_str=bytes.decode(USART.read(9))
    print(adc_count)
    print(adc_str)
    #print(dac_str)
    adc_array[adc_count]=float(adc_str[5:])
    dac_array[adc_count]=int(dac_str[5:])*3.3/4096
plt.plot(adc_array,label="Cavity transmission")
plt.plot(dac_array,label="Piezo feedback")
#plt.plot(adc_array,label="Humidity %RH")
plt.legend()
#plt.pause(1)
plt.savefig('test2png.png')
USART.close()
