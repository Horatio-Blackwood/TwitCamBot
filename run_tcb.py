# Author:       Adam Anderson
# Date:         January 30, 2016
# Module:       run_tcb.py
# Python:       3.4.2

import camera
from twitter import Tweeter

import RPi.GPIO as GPIO


from configuration import CamConfig
from configuration import GpioConfig
from configuration import TwitterConfig
from configuration import MessageConfig


def configure_gpio():
	# Read in GPIO Configuration
	gpio_config = GpioConfig()
	
	# Set GPIO Mode
	GPIO.setmode(GPIO.BCM)
	
	# Set up LED pins for GPIO Output
	GPIO.setup(gpio_config.ready_pin, GPIO.OUT) 
	GPIO.setup(gpio_config.busy_pin, GPIO.OUT) 
	
	# Set up Button pins for GPIO Input
	GPIO.setup(gpio_config.button_pin, GPIO.IN, GPIO.PUD_UP)
	
	return gpio_config
	
def get_next_pic_name(cam_cfg, pic_number):
	name = cam_cfg.img_name + pic_number + "." + cam_cfg.img_ext
	pic_number += 1
	return name


def main():
	# Read in Configurables
	# - Initialize Camera
	cam_config = CamConfig()
	cam = camera.initialize(cam_config.img_width, cam_config.img_height)
	pic_number = 0
	
	# - Initialize GPIO
	gpio_config = configure_gpio()
	
	# - Initialize Twitter Parameters
	tw_config = TwitterConfig()
	tweeter = Tweeter(tw_config.consumer_key, tw_config.consumer_secret, tw_config.access_token, tw_config.access_token_secret)
	
	# - Initialize message configuration
	msg_config = MessageConfig()
	
	# Listen for Button Presses
	while True:
		# When Button is Pressed
		GPIO.wait_for_edge(gpio_config.button_pin, GPIO.RISING)
		GPIO.output(gpio_config.ready_pin, False)
		GPIO.output(gpio_config.busy_pin, True)
		
		# Capture Image
		pic_file = get_next_pic_name(cam_config, pic_number)
		camera.take_picture(cam, pic_file)
		pic = open(pic_file, 'rb')
		
		# Upload picture to Twitter
		media_status = tweeter.upload(pic)
		
		# Once Image is uploaded, Post to Twitter
		tweeter.tweet(media_status, msg_config.msg)
		
		# When finished, reset LEDs.
		GPIO.output(gpio_config.ready_pin, True)
		GPIO.output(gpio_config.busy_pin, False)
		
	# Cleanup/Disconnect the Camera (The code should never get here tho)
	camera.cleanup_camera()

# Run Main Method
if __name__ == "__main__":
	main()
