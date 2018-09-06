import tweepy
from textblob import TextBlob
from tweepy.auth import OAuthHandler

consumer_key = '2Z05K2pb2jyBDphu' 
consumer_secret = 'tpKhuXXBpuoZXjdhzF78Bb' 

access_token = '1026725999TRJVoYbuv' 

access_token_secret = 'gfQlmy8eqAVIaasJrBAg' 

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search("Trump")
#print(public_tweets)

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
