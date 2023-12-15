print("hello world!")
import time
from machine import Pin

MIN_DEBOUNCE_TIME_MS = 200
NUM_BUTTONS = 2
BUTTON_PUSH_TIMES = [0] * NUM_BUTTONS

BUTTON_OBJECTS = [None] * NUM_BUTTONS

# Set up our button name and GPIO pin number
# Set the pin as an input and use a pull down
redbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenbutton = Pin(3, Pin.IN, Pin.PULL_DOWN)
RED_BUTTON_INDEX = 0
GREEN_BUTTON_INDEX = 1
BUTTON_OBJECTS[RED_BUTTON_INDEX] = redbutton
BUTTON_OBJECTS[GREEN_BUTTON_INDEX] = greenbutton
trigger_flash = False
flash_freq = 0.3

def is_button_pressed(button_index: int) -> bool:
    button_object = BUTTON_OBJECTS[button_index]
    button_cur_value = button_object.value()
    
    if button_cur_value == 1:
        last_push_time = BUTTON_PUSH_TIMES[button_index]
        if (time.time() - last_push_time) * 1000 >= MIN_DEBOUNCE_TIME_MS:
            BUTTON_PUSH_TIMES[button_index] = time.time()
            return True
    return False 


redLED = Pin(14, Pin.OUT)

count = 0

while True:
    if is_button_pressed(RED_BUTTON_INDEX): #If the red button is pressed
        print("Red button pressed")
        count = count + 1
        trigger_flash = True
        print(count)
        
    if is_button_pressed(GREEN_BUTTON_INDEX): #If the green button is pressed
        print("Green button pressed")
        if count == 0:
            count = 0
        else:
            count = count - 1
        trigger_flash = True
        print(count)
    
    if trigger_flash:
        for i in range(count):
            redLED.value(1)
            time.sleep(flash_freq)
            redLED.value(0)
            time.sleep(flash_freq)
            
        trigger_flash = False
            



