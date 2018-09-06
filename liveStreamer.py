from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import credentials


# Standered Output Listener class inherited from StreamListener clss
#make the program more modular 
class TwitterStreamer():
	"""
	Class for Streaming and Processing live tweets
	"""
	def stream_tweets(self, fetcehd_tweets_filename, hash_tag_list):
		# This handles Twitter authentication and the Twitter Streaming API
		
							
		listener = StdOutListener(fetched_tweets_filename)
		auth = OAuthHandler(credentials.CONSUMER_KEY,credentials.CONSUMER_SECRET)
		auth.set_access_token(credentials.ACCESS_TOKEN,credentials.ACCESS_TOKEN_SECRET)
		
		stream = Stream(auth, listener)
		stream.filter(track=hash_tag_list)	

class StdOutListener(StreamListener):
	"""
	This is a basic listener class that just prints the tweets received through STDOUT
	"""

	def __init__(self,fetched_tweets_filename):
		self.fetched_tweets_filename = fetched_tweets_filename
	def on_data(self,data):
		try:
			print(data)
			with open(self.fetched_tweets_filename,'a') as tf:
				tf.write(data)
			return True
		except BaseException as e:
				print("Error on data" % str(e))
		return True

	
	
	def on_error(self,status):
		print(status)

if __name__ == '__main__':
	hash_tag_list = ["Narendra Modi","Arvind Kejriwal"]
	fetched_tweets_filename = "tweets.json"

	twitter_streamer = TwitterStreamer()
	twitter_streamer.stream_tweets(fetched_tweets_filename,hash_tag_list)

