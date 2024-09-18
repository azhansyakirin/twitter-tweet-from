import tweepy
auth = tweepy.OAuthHandler("API KEY", "API SECRET KEY")
auth.set_access_token("ACCESS KEY", "ACCESS SECRET KEY")
api = tweepy.API(auth)
print ("Tweet From Terminal")
print ("Twitter For........")
tweet = input("Tulis tweet korang kat sini, lepastu click je ENTER ")
api.update_status(status =(tweet))
print ("Setel!")