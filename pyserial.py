#!/usr/bin/env python3
import time
import serial
from time import sleep

ser = serial.Serial(
 port='COM8',
 baudrate = 2400,
 parity=serial.PARITY_EVEN,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.SEVENBITS,
 timeout=None
)

def scaleweight():
    x=ser.readline()
    d=x.decode()    #prints out the number only    
    scale=''.join(filter(str.isdigit, d))
    scaleF=float(scale)
    scaleS=str(scaleF)
    print("You have weighed " + scaleS + " grams.")
    sleep(2)
    return(scaleF)

print(scaleweight())
