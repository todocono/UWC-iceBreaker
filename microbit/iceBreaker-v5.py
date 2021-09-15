# IceBreaker game programmed for MustardTEK by Rudi @2021
import radio
import random
import speech
import music
from microbit import *

# function to play sounds according to the group number
        
def groupSound():
    if groupNumber == 1:
        speech.say('co co co') 
    elif groupNumber == 2:
        speech.say('qi qi qi')
    elif groupNumber == 3:
        speech.say('cu cu cu')
    elif groupNumber == 4:
        speech.say('cha cha cha')
    elif groupNumber == 5:
        speech.say('tweet tweet')
    elif groupNumber == 6:
        speech.say('po po')
    elif groupNumber == 7:
        speech.say('na na')
    elif groupNumber == 8:
        speech.say('mi mi')
    elif groupNumber == 9:
        speech.say('rudi')
    elif groupNumber == 10:
        speech.say('gaaabi')
    elif groupNumber == 11:
        speech.say('andy')
    elif groupNumber == 12:
        speech.say('miiinkiii')
    else:
        speech.say('no no')

# Create the "flash" animation frames. Can you work out how it's done?
flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

# we assign a random group at the beginning
totalGroups = 12
groupNumber = random.randint(1, totalGroups)
radio.config(group=groupNumber)
radio.config(power=7)
# The radio won't work unless it's switched on.
radio.on()

# Welcome message
print(str(groupNumber))
display.scroll("g=" + str(groupNumber))  # >> should comment

steps = 0

# Event loop.
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send('reset')  # makes the others in your group to flash
        steps = 0
        if (groupNumber < totalGroups):
            groupNumber += 1
        else:
            groupNumber = 1
        print("Changing to group " + str(groupNumber))
        display.scroll("g=" + str(groupNumber)) # >> should comment
        radio.off()
        sleep(1000)
        radio.config(group=groupNumber)
        radio.on()
        sleep(1000)
        display.clear()
        # break
    # Button A sends a "flash" message to find mates.
    elif button_a.is_pressed():
        steps = 0
        radio.send('flash')  # makes the others in your group to flash
        display.show(flash, delay=100, wait=False)
        # audio.play(Sound.HELLO)
        groupSound()
        sleep(500)
        display.clear()
    # Button B resets the counter of steps
    elif button_b.is_pressed():
        steps = 0
        display.show(Image.DUCK)
        audio.play(Sound.GIGGLE)
        sleep(500)
        display.clear()
    
    # Read any incoming messages.
    incoming = radio.receive()
    if incoming == 'flash':
        # If there's an incoming "flash" message display
        display.show(flash, delay=100, wait=False)
        # audio.play(Sound.HELLO)
        groupSound()
        
    elif incoming == 'reset':
        steps = 0
        display.show(Image.ALL_CLOCKS, loop=False, delay=100)
        audio.play(Sound.TWINKLE)
        display.clear()
    
    elif incoming == 'count':
        radio.send(str(steps))
        steps = 0
        display.clear()
        
    # Count Steps
    if accelerometer.was_gesture("shake"):
        speech.say('crick') # do a click
        steps += 1
        # display.scroll(steps)
        print(str(steps))
        if (steps > 25):
            music.play(music.FUNK)
            music.play(music.POWER_UP)
            display.clear()
            steps = 0
        else:
            rows = steps // 5
            print(" with rows " + str(rows))
            cols = steps - rows * 5 
            print(" and cols " + str(cols))
            for row in range(rows):
                for cel in range(5):
                    display.set_pixel(row, cel, 9)
            for cel in range(cols):
                display.set_pixel(rows, cel, 9)
            
        
