import time
import board
import neopixel
import gphoto2 as gp
import os
import subprocess

pixels1 = neopixel.NeoPixel(board.D18, 41, brightness=1) #there are only four acceptable pins for the data. I am using 18.

base_path = '/home/CameraZero/Pictures/RTI'
batchNumber = 7  #make this increment automatically based upon the current highest-numbered batch -- perhaps the user passes a name (presumably of the object), and then each subsequent call with that name increments?

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
    camera = gp.Camera()
    camera.init()
    text = camera.get_summary()
    file_path = camera.capture(gp.GP_CAPTURE_IMAGE)
    print('Camera filepath: {0}/{1}'.format(file_path.folder, file_path.name))
#    print("Directory %s created." % target_folder)
#    target = os.path.join(target_folder,str(batchNumber).zfill(3)+'_'+str(lightNumber).zfill(2)+'_'+file_path.name)
    target = os.path.join('/home/CameraZero/Pictures/RTI/batch_007',str(batchNumber).zfill(3)+'_'+str(lightNumber).zfill(2)+'_'+file_path.name)
#    target = os.path.join('/tmp','Batch'+str(batchNumber).zfill(3),str(batchNumber)+'_'+str(lightNumber)+file_path.name)
    print('Copying image to', target)
    camera_file = camera.file_get(
        file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
    camera_file.save(target)
#    subprocess.call(['xdg-open', target]) #this was in the gphoto2 example, but was causing the script to hang after the image opened.
#    camera.exit() #apparently un-needed
    return

def lightAndShoot(target_folder,batchNumber,lightNumber): 
    clearPixels()
    pixels1[lightNumber] = (255,255,255)
    take_the_photo(target_folder,batchNumber,lightNumber)
    clearPixels()
    return

def batchLightAndShoot(base_path,batchNumber): #figure out how to ensure the camera is awake // can gphoto2 wake the camera?
    target_folder = makeBatchFolder(base_path,batchNumber)
    for lightNumber in range (0,40):
        print('Batch: '+str(batchNumber)+'. Image: '+str(lightNumber)+' .')
        lightAndShoot(target_folder,batchNumber,lightNumber)

batchLightAndShoot(base_path,batchNumber)
