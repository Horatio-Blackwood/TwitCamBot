# Author:       Adam Anderson
# Date:         January 30, 2016
# Module:       twitter.py
# Python:       3.4.2

from twython import Twython

class Tweeter(object):
	
	def __init__(self, consumer_key, consumer_secret, accessToken, accessTokenSecret):
		""" Initializes a new instance of 'Tweeter', a wrapper for the Twython API
		"""
		self.api = Twython(consumer_key, consumer_secret, accessToken, accessTokenSecret)
		
	
	def upload(self, image):
		""" Uploads the supplied image object to Twitter and returns
			a Media Status object.
		
			image object obtained thusly:
				image = open(filename, 'rb')
		"""
		return self.api.upload_media(media=image)
	
	
	def tweet(self, media_status, text):
		""" Posts a tweet with the supplied media_status (pictures etc) 
			and text.
		"""
		self.api.update_status(media_ids=[media_status['media_id']], status=text)
