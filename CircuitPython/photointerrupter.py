import time
import board
from digitalio import DigitalInOut, Direction, Pull


laser = DigitalInOut(board.D2)
laser.direction = Direction.INPUT
laser.pull = Pull.UP

interruptions = 0

switch = 0


while True:
    if laser.value and switch ==0:

        switch = 1
        interruptions += 1

    elif not laser.value:
        switch = 0


    if time.monotonic() %4 == 0:
        #print(laser.value)
        print("the number of interruptions is")
        print(str(interruptions))
        #print(time.monotonic())