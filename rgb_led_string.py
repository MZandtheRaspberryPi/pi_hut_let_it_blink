from machine import Pin
from neopixel import NeoPixel
import time
import random

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

for i in range(6):
    if i % 2 == 0:
        COLOR_ARR[i].r = 100 + random.randint(0, 100)
        COLOR_ARR[i].g = 0
    else:
        COLOR_ARR[i].r = 0
        COLOR_ARR[i].g = 100 + random.randint(0, 100)
    color = COLOR_ARR[i]
    strand[i] = (color.to_tuple())

COLOR_ARR[0].r = 150
COLOR_ARR[1].g = 150
strand[0] = (COLOR_ARR[0].to_tuple())
strand[1] = (COLOR_ARR[1].to_tuple())

strand.write()
time.sleep(SLP_TIME)


while True:
    
    first_color = COLOR_ARR[-1]
    prior_color = COLOR_ARR[0]

    for i in range(1, NUM_LEDS):
        prior_color_tmp = COLOR_ARR[i]
        
        COLOR_ARR[i] = prior_color
        
        prior_color = prior_color_tmp
    COLOR_ARR[0] = first_color
    for i in range(NUM_LEDS):
        strand[i] = (COLOR_ARR[i].to_tuple())
    strand.write()
    time.sleep(SLP_TIME)
