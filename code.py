import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


keyboard = Keyboard(usb_hid.devices)

mute_pin = board.GP16

# Initializing Button
mute = digitalio.DigitalInOut(mute_pin)
mute.direction = digitalio.Direction.INPUT
mute.pull = digitalio.Pull.DOWN
mute_bool = False


while True:
    
    if mute.value:  
        print("Reloading")
        keyboard.press(Keycode.F5)
        time.sleep(0.15)
        keyboard.release(Keycode.F5)
        mute_bool = not mute_bool
