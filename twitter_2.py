import twitter



consumer_key = '2Z0N9WkHDphu' 
consumer_secret = 'tpKhuMXbxrjTWg7MXXBpuoZXjdhzF78Bb' 

access_token_key = '102672599420NyTDk9TRJVoYbuv' 

access_token_secret = 'gfQlmy8eqsJrBAg' 

api = twitter.Api(consumer_key,consumer_secret,access_token_key,access_token_secret)

#print(api.VerifyCredentials())

friends = api.GetFriends()
#print(friends)
#for u in friends:
#	print(dir(u))
#for u in friends:
#   print(u.screen_name)



#public tweet
status_string = '@RishabK77368486 Python is AMAZING when used with Internet and a mug of Coffee.......:Let '
post_update = api.PostUpdates(status = status_string)

status_length = twitter.twitter_utils.cals_expected_status_length(status = status_string)
#print(status_length)

new_message = api.PostDirectMessage(screen_name = 'RishabK77368486', text='Hello Brother....It.s Khabri')
print(new_message)



"""
api.PostUpdates(status)

api.GetUser(user)
api.GetReplies()
api.GetUserTimeline(user)
api.GetHomeTimeline()
api.GetStatus(status_id)
api.GetStatuses(status_ids)
api.DestroyStatus(status_id)
api.GetFriends(user)
api.GetFollowers()
api.GetFeatured()
api.GetDirectMessages()
api.GetSentDirectMessages()
api.PostDirectMessage(user, text)
api.DestroyDirectMessage(message_id)
api.DestroyFriendship(user)
api.CreateFriendship(user)
api.LookupFriendship(user)
api.VerifyCredentials()

"""