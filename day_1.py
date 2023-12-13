print("hello world!")
import time
from machine import Pin

SLEEP_TIME = 0.5

onboardLED = Pin(14, Pin.OUT)
while True:
    onboardLED.value(1)
    time.sleep(SLEEP_TIME)
    onboardLED.value(0)
    time.sleep(SLEEP_TIME)
print('done')