from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import credentials
import pandas as pd
import numpy as np

# Standered Output Listener class inherited from StreamListener clss

### Twitter Clients######
class TwitterClient():
	def __init__(self,twitter_user=None):
		self.auth = TwitterAuthenticator().AuthenticateTwitterApp()
		self.twitter_client = API(self.auth)
		
		self.twitter_user = twitter_user
        def GetTwitterClientAPI(self):
		return self.twitter_client		
	def GetUserTimelineTweets(self, num_tweets):
		tweets = []
		for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
			tweets.append(tweet)
		return tweets
	def GetFriendList(self, num_friends):	
		friends = []
		for friend in Cursor(self.twitter_client.friends, id = self.twitter_user).items(num_friends):
			friends.append(friend)
		return friends		
	def GetHomeTimelineTweets(self, num_tweets):
		timeline_tweets = []
		for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
			timeline_tweets.append = tweet
		return timeline_tweets
# twitter authenticator #
class TwitterAuthenticator():
	def AuthenticateTwitterApp(self):
				
		auth = OAuthHandler(credentials.CONSUMER_KEY,credentials.CONSUMER_SECRET)
		auth.set_access_token(credentials.ACCESS_TOKEN,credentials.ACCESS_TOKEN_SECRET)
		return auth 

class TwitterStreamer():
	"""
	Class for Streaming and Processing live tweets
	"""
	def __init__(self):
		self.twitter_authenticator = TwitterAuthenticator()
		
	def stream_tweets(self, fetcehd_tweets_filename, hash_tag_list):
		# This handles Twitter authentication and the Twitter Streaming API
		
							
		listener = TwitterListener(fetched_tweets_filename)

		auth = self.twitter_authenticator.AuthenticateTwitterApp()

		stream = Stream(auth, listener)
		stream.filter(track=hash_tag_list)	

class TwitterListener(StreamListener):
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
		if status == 420:
			# Returning False on_data method in case rate limit occurs
			return False	
		print(status)
class TweetAnalyzer():
	"""
	Functionality for analyzinz and categorizing twets
	"""
	def TweetsToDataFrame(self, tweets):
		df = pd.DataFrame(data = [tweet.text for tweet in tweets], columns=['Tweets'])
		df['id'] = np.array([tweet.id for tweet in tweets])
		df['len'] = np.array([len(tweet.text) for tweet in tweets])
		df['date'] = np.array([tweet.created_at for tweet in tweets])
		df['source'] = np.array([tweet.source for tweet in tweets])
		df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
		df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])

		return df
if __name__ == '__main__':
	twitter_client = TwitterClient()
	tweet_analyzer = TweetAnalyzer()
	api = twitter_client.GetTwitterClientAPI()
	
	tweets = api.user_timeline(screen_name='msdhoni', count=20)

#	print(dir(tweets[0])) # print the directory of tweets	
	
	df = tweet_analyzer.TweetsToDataFrame(tweets)

	print(df.head(10))
