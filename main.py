from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = "4OpxHIoIs8zBdIj3QolIkiwuP"
csecret = "Z7zMiz8Zj8Mo6TwuflwHUHcXTrIW2txQKjKVQYk7QxiFrqoTUZ"
atoken = "4769508458-3dooIe2BcwwOTyT3dqyZx919S8AdHq2Vs1SLBFs"
asecret = "mFfFQ6QzE21z5S9sj9c56Srkt4VqT9VglskH0Xa1W9fLB"


class listener(StreamListener):
    try:
        def on_data(self, data):
            print(data)
            saveFile = open("twitDB2.csv", "a")
            saveFile.write(data)
            saveFile.write("\n")
            saveFile.close()
            return True
    except Exception as e:
        print("Failed on data,", str(e))
        time.sleep(5)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["SuperBowlAds", "SuperBowlCommercials", "SuperBowl"])