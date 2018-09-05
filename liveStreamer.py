from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import credentials


# Standered Output Listener class inherited from StreamListener clss
class StdOutListener(StreamListener):
	
	def on_data(self,data):
		print(data)
		return True
	
	def on_error(self,status):
		print(status)

if __name__ == '__main__':
	listener = StdOutListener()
	auth = OAuthHandler(credentials.CONSUMER_KEY,credentials.CONSUMER_SECRET)
	auth.set_access_token(credentials.ACCESS_TOKEN,credentials.ACCESS_TOKEN_SECRET)
	
	stream = Stream(auth, listener)
	stream.filter(track=['arendra Modi','Arvind Kejriwal'])	
