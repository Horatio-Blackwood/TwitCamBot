# Author:       Adam Anderson
# Date:         January 30, 2016
# Module:       configuration.py
# Python:       3.4.2

import configparser

config = configparser.RawConfigParser()
config.read('app.config')


class TwitterConfig(object):
    """ A class that holds the twitter app configuration.
    """
    consumer_key        = config.get('twitter', 'consumer_key')
    consumer_secret     = config.get('twitter', 'consumer_secret')
    access_token        = config.get('twitter', 'access_token')
    access_token_secret = config.get('twitter', 'access_token_secret')


class GpioConfig(object):
    """ A class that holds the GPIO pin configuration
    """
    cam_button_pin = config.getint('gpio', 'cam_button_pin')
    ready_pin      = config.getint('gpio', 'ready_pin')
    busy_pin       = config.getint('gpio', 'busy_pin')


class CamConfig(object):
    """ A class that holds the Camera configuration
    """
    img_width  = config.getint('cam', 'img_width')
    img_height = config.getint('cam', 'img_height')
    img_name   = config.get('cam', 'img_name')
    img_ext    = config.get('cam', 'img_ext')


class MessageConfig(object):
	""" A class for the message configuration.
	"""
	msg = config.get('message', 'msg')
