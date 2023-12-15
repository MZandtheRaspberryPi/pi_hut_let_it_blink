from machine import Pin, UART
from neopixel import NeoPixel
import time
import random

# Define the ring pin number (2) and number of LEDs (12)
ring = NeoPixel(Pin(2),12)

# Define buttons
NUM_BUTTONS = 1
BUTTON_OBJECTS = [None] * NUM_BUTTONS
MIN_DEBOUNCE_TIME_MS = 500
BUTTON_PUSH_TIMES = [0]
greenbutton = Pin(28, Pin.IN, Pin.PULL_DOWN)
GREEN_BUTTON_INDEX = 0
BUTTON_OBJECTS[GREEN_BUTTON_INDEX] = greenbutton

# UART VARS
BAUD_RATE = 9600
PAYLOAD_SIZE_BYTES = 4

uart = UART(0, baudrate=BAUD_RATE, tx=Pin(0), rx=Pin(1))
uart.init(bits=8, parity=None, stop=2)

# Define variable to hold stage of process
# stage 0 = waiting for button to be pressed to light up ring
# stage 1 = right lit up, waiting for photo to be taken
# stage 2 = photo taken, processing data and displaying results
# back to stage 0 - reset

stage_var = 0

# Turn off all LEDs before program start
ring.fill((0,0,0))
ring.write()

def is_button_pressed(button_index: int) -> bool:
    button_object = BUTTON_OBJECTS[button_index]
    button_cur_value = button_object.value()
    
    if button_cur_value == 1:
        last_push_time = BUTTON_PUSH_TIMES[button_index]
        if (time.time() - last_push_time) * 1000 >= MIN_DEBOUNCE_TIME_MS:
            BUTTON_PUSH_TIMES[button_index] = time.time()
            return True
    return False

def light_up_ring():
    ring.fill((10,10,10))
    ring.write()

def switch_off_ring():
    ring.fill((0,0,0))
    ring.write()

while True:
    if is_button_pressed(GREEN_BUTTON_INDEX):
        print("sending")
        uart.write(bytes(0x1))
        light_up_ring()
        time.sleep(2)
        switch_off_ring()
        
        #If the button is pressed
        #if stage_var == 0:
        #    # light_up_ring()
        #    stage_var = 1
        #else:
        #    switch_off_ring()
        #    stage_var = 0
    #if uart.any() > 0:
     #   data = uart.read(1)
     #   light_up_ring()
      #  time.sleep(2)
      #  switch_off_ring()
        
"""
LED_PIN = 16
NUM_LEDS = 15
SLP_TIME = 0.2

class Color:
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0
    def to_tuple(self):
        return (self.r, self.g, self.b)
    def __str__(self):
        return f"{self.r},{self.g},{self.b}"
    
COLOR_ARR = [Color() for i in range(NUM_LEDS)]

strand = NeoPixel(Pin(LED_PIN), NUM_LEDS)
strand.fill((0,0,0))


COLOR_ARR[0].r = 150
COLOR_ARR[1].g = 150
strand[0] = (COLOR_ARR[0].to_tuple())
strand[1] = (COLOR_ARR[1].to_tuple())

strand.write()
time.sleep(SLP_TIME)



while True:
    
    pass

"""
