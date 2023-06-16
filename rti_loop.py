import time
import board
import neopixel
import gphoto2 as gp
import os
import subprocess

pixels1 = neopixel.NeoPixel(board.D18, 50, brightness=1)

base_path = '/home/CameraZero/Pictures/RTI'
batchNumber = 1

def blinkAndClearPixels():
    pixels1[0] = (255,0,0)
    pixels1[1] = (0,255,0)
    pixels1[2] = (0,0,255)
    time.sleep(0.5)
    pixels1.fill((0,0,0))
    return
    
def makeBatchFolder(base_path,batchNumber):
    target_folder = os.path.join(base_path,'batch_'+str(batchNumber).zfill(3))
    print("Target folder: %s" % target_folder)
    try:
        os.makedirs(target_folder)
    except OSError as error:
        print(error)
    return 
        
def take_the_photo(batchNumber,lightNumber):
    camera = gp.Camera()
    camera.init()
    text = camera.get_summary()
    file_path = camera.capture(gp.GP_CAPTURE_IMAGE)
    print('Camera filepath: {0}/{1}'.format(file_path.folder, file_path.name))
    print("Directory %s created." % target_folder)
    target = os.path.join(target_folder,str(batchNumber).zfill(3)+'_'+str(lightNumber).zfill(2)+'_'+file_path.name)
#    target = os.path.join('/tmp','Batch'+str(batchNumber).zfill(3),str(batchNumber)+'_'+str(lightNumber)+file_path.name)
    print('Copying image to', target)
    camera_file = camera.file_get(
        file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
    camera_file.save(target)
#    subprocess.call(['xdg-open', target])
#    camera.exit()
    return

def lightAndShoot(batchNumber,lightNumber):
    blinkAndClearPixels()
    pixels1[lightNumber] = (255,255,255)
    take_the_photo(target_folder,batchNumber,lightNumber)
    blinkAndClearPixels()
    return

def batchLightAndShoot(base_path,batchNumber):
    target_folder = makeBatchFolder(base_path,batchNumber)
    for lightNumber in range (48,49):
        print('Batch: '+batchNumber+'. Image: '+str(lightNumber+1)+' .')
        lightAndShoot(target_folder,batchNumber,lightNumber)

batchLightAndShoot(base_path,batchNumber)
