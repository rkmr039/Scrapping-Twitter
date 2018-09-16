
import common_classes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

if __name__ == '__main__':
	twitter_client = common_classes.TwitterClient()
	tweet_analyzer = common_classes.TweetAnalyzer()
	user_analyzer  = common_classes.UserAnalyzer() 
	api = twitter_client.GetClientAPI()
	sn = 'msdhoni'
	

	tweets = api.user_timeline(screen_name=sn, count=20)
	df = tweet_analyzer.TweetsToDataFrame(tweets) # df = pd.DataFrame 
	
		
		
	# Get Maximum retweet count
	print(tweet_analyzer.GetMaximumRetweetCount(df))

	# Get maximum likes count
	print(tweet_analyzer.GetMaximumLikesCount(df))	

	# Display Likes and retweets time series
	tweet_analyzer.GetTimeSeries(df)

	# Sentiment Analysis
	df['sentiment'] = np.array([tweet_analyzer.AnalyzeSentiment(tweet) for tweet in df['tweets']])
	print(df.head(10))
