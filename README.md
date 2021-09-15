# UWC-iceBreaker

## Requirements
This repo contains an activity to run using micro:bit v2. iceBreaker inside of the microbit folder should be uploaded for each participant. One micro:bit should be uploaded masterIce and it should be connected to a server computer through USB. Both of these files were programmed on https://python.microbit.org/v/2. On the server computer, after adjusting the USB serial name of the micro:bit on the server.py, from the terminal run node server.js and look at a Chrome browser at the page http://localhost:5000

## Description
Participants will be assigned in radio groups randomly and they need to find each other.  The "game" consists initially in filling in the whole screen by shaking the board. By pressing A, you let others find you. By pressing B, you let the counters reset. 

## Notes for the instructor

Each of the micro:bit with the iceBreaker can be changed from one group to another by pressing A + B. If the masterIce is on (it's connected to a USB), it will automatically erase the displays every time it polls the score acumulated by the team.

## Credits
IceBreaker game programmed for MustardTEK by Rudi @2021 during the icebreaker exercise at United World College in Changshu. Many little bits from here and there, under Open Source AFAIK. Big kudos to the examples and the P5 Sketch from Prof. Stavros Didakis and his workshop Connected Systems. 

## License
All materials in here are under MIT licence
