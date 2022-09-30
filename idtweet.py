import tweepy 
import pandas as pd  
# assign the values accordingly 
consumer_key = "<YOUR CONSUMER KEY" 
consumer_secret = "<YOUR CONSUMER SECRET>" 
access_token = "<YOUR ACCESS TOKEN>" 
access_token_secret = "<YOUR ACCESS TOKEN SECRET>" 
  
# authorization of consumer key and consumer secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# set access to user's access key and access secret  
auth.set_access_token(access_token, access_token_secret) 
  
# calling the api  
api = tweepy.API(auth)




def collect(screen):
    l=[]
    # screen name of the account to be fetched 
    screen_name = screen
    count = 5
    # fetching the statuses 
    statuses = api.user_timeline(screen_name,count=count) 
  
    for status in statuses:
        l.append(status.text)
        #print(status.text, end = "\n\n")
    return l

