import tweepy
from datetime import datetime, timedelta, timezone
import time
import pytz

consumer_key = "WRITEYOURS"
consumer_secret = "WRITEYOURS"
access_token = "WRITE-YOURS"
access_token_secret = "WRITEYOURS"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

istanbul_timezone = pytz.timezone("Europe/Istanbul")

user = "WRITEUSERNAME"

following = []
for friend in tweepy.Cursor(api.get_friends, screen_name=user).items():
    following.append(friend.screen_name)

print("FOLLOWING COUNT: " + str(len(following)))

skip_users = ["FINANCIALJUICE", "ELONMUSK"]

print("SKIP USER COUNT: " + str(len(skip_users)))

not_engaging_users = []

for username in following:
    if username in skip_users:
        continue
    try:
        user_favorites = api.get_favorites(screen_name=username, count=1)
        time.sleep(5)

        if len(user_favorites) > 0:
            favorite = user_favorites[0]
            favorite_time = favorite.created_at.replace(tzinfo=pytz.utc).astimezone(istanbul_timezone)
            print(username + " favorite_time: " + str(favorite_time))
            #print("IST TIME: " + str(datetime.now(istanbul_timezone)))
            time_difference = datetime.now(istanbul_timezone) - timedelta(days=31)
            #print(time_difference)
            if favorite_time > time_difference:
                continue
            else:
                not_engaging_users.append(username)
        else:
            not_engaging_users.append(username)
    except tweepy.TweepyException:
        not_engaging_users.append(username)
        #print(f"{username} ERROR.")

print("----------USERS----------")
print("USER COUNT: " + str(len(not_engaging_users)))
print()
for username in not_engaging_users:
    print(username)
