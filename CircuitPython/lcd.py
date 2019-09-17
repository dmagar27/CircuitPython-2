import board
import time
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode

switch = DigitalInOut(board.D7)
button = DigitalInOut(board.D2)
switch.direction = Direction.INPUT
button.direction = Direction.INPUT
switch.pull = Pull.DOWN
button.pull = Pull.DOWN
presses = 0
direction = 1
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)
toggle1 = 0


while True:
    lcd.set_cursor_pos(0,0)
    lcd.print("Switch: ")
    lcd.set_cursor_pos(1,0)
    lcd.print("Presses:")
    if switch.value and not button.value:
        direction =1
        lcd.clear()
        lcd.set_cursor_pos(0,8)
        lcd.print("UP")
        print("UP")
    if button.value and toggle1 ==0 and not switch.value:
        toggle1 = 1
        presses += direction
        lcd.set_cursor_pos(1,9)
        lcd.print(str(presses))
        lcd.print("       ")
        print(str(presses))
    if not button.value:
        toggle1 = 0
    if switch.value and presses > 1:
        direction = -1
        lcd.set_cursor_pos(0,8)
        lcd.print("DOWN")
        print("DOWN")
        if button.value and lcd.print("DOWN"):
            presses += direction
            lcd.set_cursor_pos(1,9)
            lcd.print(str(presses))
            print(str(presses))






time.sleep(0.01)