import tweepy
# game database
members =['@TheApprentice94','@Heijligers']
rewards = {'#meditation': 500, '#consciousnessattracts': 20}
filename_id = 'last_seen.txt'
consumer_key = 'Qqewhu0mb7Gs17wWVvF2DDB1V'
consumer_secret = 'VK0fF4RiXTWw7WUw28ApXXYoSoAvfxcxyU4j1TULnAwyYS70SG'
key = '1249056320847785984-Mvw1q9pXChl1Zyrsp2hWnIG0uTMdLe'
secret = 'zRKxhAHNJpQSLTcDTrJQHtXHIJN4BnAWC4XvhR4uvjB73'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)


# Prepare Program data
def read_last_seen(filename_id):
    file_read = open(filename_id, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(filename_id,last_seen_id):
    file_write = open(filename_id,'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

last_seen_id = read_last_seen(filename_id)
print(last_seen_id)
# store_last_seen(filename_id,last_seen_id+1)

# Process Mentions
# tweets = api.mentions_timeline(read_last_seen(filename_id), tweet_mode='extended')
# for tweet in tweets:
#     if '#meditation' in tweet.full_text.lower():
#         print(str(tweet.id)+' - ' + tweet.full_text)


# Process Members
for member in members:
    tweets = api.user_timeline(member, tweet_mode = 'extended')
    for tweet in tweets:
        points = 0
        triggers = []
        for trigger in rewards:
            if trigger in tweet.full_text.lower():
                points = points + rewards[trigger]
                triggers.append(trigger)
                print(trigger)
                print(str(tweet.id) + ' - ' + tweet.full_text)
        if points != 0:
            print('Congratulations ',member ,' you have earned: ' + str(points) + ' #LifePoints', *triggers )
        # if '#meditation' in tweet.full_text.lower():
        #     print(str(tweet.id)+' - ' + tweet.full_text)