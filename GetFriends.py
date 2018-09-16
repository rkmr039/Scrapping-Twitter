
import common_classes
import pandas as pd
import numpy as np
# Standered Output Listener class inherited from StreamListener clss
		
		
if __name__ == '__main__':
	twitter_client = common_classes.TwitterClient()
	tweet_analyzer = common_classes.TweetAnalyzer()
	user_analyzer  = common_classes.UserAnalyzer() 
	api = twitter_client.GetClientAPI()
	
	sn = 'msdhoni'
	
	data = user_analyzer.GetUserProfileDetails(api,sn)
	for i in data:
		print(str(i[0]) + ' : ' + str(i[1]))

	print("Friends List")	
	user_analyzer.GetFriendList(api,sn)

	print("Followers List")	
	user_analyzer.GetFollowerList(api,sn)
