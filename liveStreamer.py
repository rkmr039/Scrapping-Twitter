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
        def GetClientAPI(self):
		return self.twitter_client		
	def GetClientTimelineTweets(self, num_tweets):
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

class UserAnalyzer():
	"""
	Get User Dertails
	Functionality for analyzing Users on Twitter
	"""
	def GetScreenName(self,api,user_id):
		user = api.get_user(id = user_id)
		screen_name = user.screen_name;
		return screen_name;

	def GetUserFollowerDetails():
		pass
	
	def GetUserProfileDetails(self,api,screen_name):
		user_profile = api.get_user(screen_name=screen_name)
		data = []
		data.append(['ID         ',user_profile.id]);
		data.append(['Screen Name',user_profile.screen_name]);
		data.append(['Name       ',user_profile.name]);
		data.append(['Followers  ',user_profile.followers_count]);
		data.append(['Location   ',user_profile.location])
		data.append(['Description',user_profile.description])
		data.append(['FriendCount',user_profile.friends_count])
		data.append(['Joined At  ',user_profile.created_at])
		return data		
		
if __name__ == '__main__':
	twitter_client = TwitterClient()
	tweet_analyzer = TweetAnalyzer()
	user_analyzer  = UserAnalyzer() 
	api = twitter_client.GetClientAPI()
	sn = 'msdhoni'

	data = user_analyzer.GetUserProfileDetails(api,sn)
	for i in data:
		print(str(i[0]) + ' : ' + str(i[1]))
	
	tweets = api.user_timeline(screen_name=sn, count=20)
	df = tweet_analyzer.TweetsToDataFrame(tweets) # df = pd.DataFrame 
	print(df.head(10))
	
	"""
	# Get  Client's Friend List
	friend_ids = []
	friends = []
	friend_ids = api.friends_ids()
	for friend_id in friend_ids:
		sn = user_analyzer.GetScreenName(api,friend_id)
		data = user_analyzer.GetUserProfileDetails(api,sn)
		print(str(data[0])  + ' : ' + str(data[2]))
		
	"""	
	# Get User's Friend List

