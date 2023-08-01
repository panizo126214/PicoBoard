import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

print("Device is working!")
keyboard = Keyboard(usb_hid.devices)

terminal_pin = board.GP16

# Initializing Button
terminal = digitalio.DigitalInOut(terminal_pin)
terminal.direction = digitalio.Direction.INPUT
terminal.pull = digitalio.Pull.DOWN
terminal_bool = False


while True:
    
    if terminal.value:  
        print("Reloading")
        keyboard.press(227) #Simulate pressing Windows
        time.sleep(0.15)
        keyboard.press(21) #Simulate pressing R
        time.sleep(0.15)
        keyboard.release(227)
        time.sleep(0.15)
        keyboard.release(21)
        
        #Writting wt.exe on panel to get terminal access
        keyboard.send(26,23,55,8)
        keyboard.send(27,8,40)
        time.sleep(2) #Wait 2 secs in order to let terminal open
        print("Granted terminal access!")
        
        #Now write ls command and execute it
        keyboard.send(15,22,40)

        terminal_bool = not terminal_bool