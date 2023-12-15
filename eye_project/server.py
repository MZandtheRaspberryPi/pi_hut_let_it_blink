import os
import time
import serial

INT_SIZE_BYTES = 1
ENDIANNES = "big"
BAUD_RATE = 9600
PAYLOAD_SIZE_BYTES = 4
STOPBITS = serial.STOPBITS_TWO

serial_port = "COM6"
ser_obj = serial.Serial(serial_port, BAUD_RATE, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=STOPBITS)

RUN_TIME = 10

start_time = time.time()

while True:
    if ser_obj.inWaiting() > 0:
        print("received byte")
        data = ser_obj.read(1)
        # ser_obj.write(1)
        
    if time.time() - start_time > RUN_TIME:
        break

ser_obj.close()