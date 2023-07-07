import time
import board
import neopixel

pixels1 = neopixel.NeoPixel(board.D18, 41, brightness=1)


pixels1.fill((0,0,0))

# myPixels = [40,38,36] #for focusing, three at the top
myPixels = [9] #for exposure, one on the bottom


for lightNum in myPixels:
    pixels1[lightNum] = (255, 255, 255)

time.sleep(120)

pixels1.fill((0,0,0))