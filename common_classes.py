from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import credentials
from textblob import TextBlob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
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
	
class TweetAnalyzer():
	"""
	Functionality for analyzinz and categorizing twets
	"""
	def CleanTweet(self, tweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\s+)"," ",tweet).split())

	def AnalyzeSentiment(self, tweet):
		analysis = TextBlob(self.CleanTweet(tweet))

		if analysis.sentiment.polarity > 0:
			return 1
		elif analysis.sentiment.polarity == 0:
			return 0
		else:
			return -1
		
	def TweetsToDataFrame(self, tweets):
		df = pd.DataFrame(data = [tweet.text for tweet in tweets], columns=['tweets'])
		df['id'] = np.array([tweet.id for tweet in tweets])
		df['len'] = np.array([len(tweet.text) for tweet in tweets])
		df['date'] = np.array([tweet.created_at for tweet in tweets])
		df['source'] = np.array([tweet.source for tweet in tweets])
		df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
		df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])

		return df

	def GetMaximumRetweetCount(self,df):
		# Get the number of Retweets for the maximum time retweeted tweet
		print("Retweet "+str(np.max(df['retweets'])))
		
	
	
	def GetMaximumLikesCount(self,df):
		# Get the number of Retweets for the maximum time retweeted tweet
		print("Likes "+str(np.max(df['likes'])))

	def GetAverageTweetLength(self,df):
		# Get average length over all tweets	
		print("Average Length of tweets "+ str(np.mean(df['len'])))	
	
	def GetLikesTimeSeries(self,df):
		# Time Series for Likes
		time_likes = pd.Series(data = df['likes'].values, index=df['date'])
		time_likes.plot(figsize=(16, 4), color='r', title='Likes')
		plt.show()
		
	def GetRetweetsTimeSeries(self,df):
		# Time Series for Retweets
		time_retweets = pd.Series(data = df['retweets'].values, index=df['date'])
		time_retweets.plot(figsize=(16, 4), color='r', title='Retweets')
		plt.show()

	def GetTimeSeries(self,df):
		# Time Series for Likes and Retweets

		time_retweets = pd.Series(data = df['retweets'].values, index=df['date'])
		time_retweets.plot(figsize=(16, 4), label='Retweets', legend=True)
		
		time_likes = pd.Series(data = df['likes'].values, index=df['date'])
		time_likes.plot(figsize=(16, 4), label='Likes', legend=True)
		
		plt.show()
			

class UserAnalyzer():
	"""
	Get User Dertails
	Functionality for analyzing Users on Twitter
	"""
	def GetScreenName(self,api,user_id):
		user = api.get_user(id = user_id)
		screen_name = user.screen_name;
		return screen_name

	def GetFollowerList(self,api,screen_name):
		for follower_id in Cursor(api.followers_ids, screen_name = screen_name).items():
			sc = self.GetScreenName(api,follower_id)	
			data = self.GetUserProfileDetails(api,sc)
			print(str(data[0]) + ' : ' + str(data[1]) + ' : ' + str(data[2]))

	def GetFriendList(self,api,screen_name):
		for friend_id in Cursor(api.friends_ids, screen_name = screen_name).items():
			sc = self.GetScreenName(api,friend_id)
			data = self.GetUserProfileDetails(api,sc)
			print(str(data[0]) + ' : ' + str(data[1]) + ' : ' + str(data[2]))
		
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

