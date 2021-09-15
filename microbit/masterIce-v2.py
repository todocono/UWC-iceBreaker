# Relay master 
# programmed for MustardTEK by Rudi @2021
import radio
import time
import random

from microbit import *

# we assign a random group at the beginning
totalGroups = 12

radio.config(group=1)
radio.config(power=7)
# The radio won't work unless it's switched on.
radio.on()

# Welcome message
display.scroll('relay')  

stepsArray = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ]

# Main loop.
while True:
    sleep(50)   #prevents buffer overflow
    '''  print(str(steps) + ',1,2,5,6,7,8,9,10,11,12,358') # dummy data 
         steps += 1
         if (steps > 100):
            steps = 0 
    '''
    
    for group in range(totalGroups):
        # shows which group are we scanning
        rows = group // 5
        cols = group - rows * 5 
        print(" and cols " + str(cols))
        for row in range(rows):
            for cel in range(5):
                display.set_pixel(row, cel, 9)
        for cel in range(cols):
            display.set_pixel(rows, cel, 9)
        
        # switches comm channel
        # radio.off()
        # sleep(1)
        radio.config(group=group)
        # radio.on()
        # sleep(1)
        
        #scan group
        radio.send('count')
        # display.show(group)
        now = time.ticks_ms()  # wait n time to collect answers
        while True:
            if int(time.ticks_ms()) > now + 250:
                break
            else:
                incoming = radio.receive()
                if (incoming):
                    stepsArray[group] = stepsArray[group] + int(incoming)
        display.clear()
    # Send over serial comm the total of all the steps
    print(','.join(str(x) for x in list(stepsArray)))   