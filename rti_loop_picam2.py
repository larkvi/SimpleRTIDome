import time
import board
import neopixel
from picamera2 import Picamera2
from libcamera import controls
import os
import subprocess
import sys
import argparse



#import the args here: height of object in mm; exposure compensation if needed; anything else?
#temp: set the user-config values here
base_path = '/home/CameraZero/Pictures/RTI'
batchNumber = 18  #make this increment automatically based upon the current highest-numbered batch -- perhaps the user passes a name (presumably of the object), and then each subsequent call with that name increments?
object_height = 1.95 #height of photographed object in mm

#values below here configure the camera
pixels1 = neopixel.NeoPixel(board.D18, 41, brightness=1) #there are only four acceptable pins for the data. I am using 18.

picam2 = Picamera2()
picam2.configure("capture")
picam2.controls.ExposureTime = 100000
picam2.controls.AnalogueGain = 1.0
picam2.controls.AfMode = controls.AfModeEnum.Manual
picam2.controls.LensPosition = 1000/(110-object_height)
picam2.controls.AwbMode = controls.AwbModeEnum.Daylight

#begin the actual code
def clearPixels():
    pixels1.fill((0,0,0)) #is there a better way to turn the neopixels off?
    return
    
def makeBatchFolder(base_path,batchNumber):
    target_folder = os.path.join(base_path,'batch_'+str(batchNumber).zfill(3))
    print("Target folder: " + target_folder)
    try:
        os.makedirs(target_folder) #makedirs is the plural(recursive) of mkdir for some reason.
    except OSError as error:
        print(error)
    return 
        
def take_the_photo(target_folder,batchNumber,lightNumber):
    target = os.path.join(base_path,'batch_'+str(batchNumber).zfill(3),str(batchNumber).zfill(3)+'_'+str(lightNumber).zfill(2)+'_'+"rti.jpg")
    picam2.capture_file(target)
    print('Writing image to', target)
    return

def lightAndShoot(target_folder,batchNumber,lightNumber):
    picam2.start()
    clearPixels()
    pixels1[lightNumber] = (255,255,255)
    take_the_photo(target_folder,batchNumber,lightNumber)
    clearPixels()
    picam2.stop()
    return

def batchLightAndShoot(base_path,batchNumber): #figure out how to ensure the camera is awake // can gphoto2 wake the camera?
    target_folder = makeBatchFolder(base_path,batchNumber)
    for lightNumber in range (0,41):
        print('Batch: '+str(batchNumber)+'. Image: '+str(lightNumber)+' .')
        lightAndShoot(target_folder,batchNumber,lightNumber)

batchLightAndShoot(base_path,batchNumber)