# Author:       Adam Anderson
# Date:         January 30, 2016
# Module:       camera.py
# Python:       3.4.2


def initialize(img_width, img_height):
	
	# Initialize the camera
    cam = picamera.PiCamera()
    cam.resolution = (img_width, img_height)
    
    # Return initialized PiCamera instance.
    return cam

def take_picture(cam, filename):
    cam.capture(filename)

def cleanup_camera(cam):
    cam.close()
