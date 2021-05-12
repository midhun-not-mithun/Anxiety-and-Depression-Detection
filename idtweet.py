import tweepy 
import pandas as pd  
# assign the values accordingly 
consumer_key = "fiOWhFmuBtdb91LAYG4Qb9P30" 
consumer_secret = "Id8Xjz0WBP4SEDr6nDZFWaw9AaZN71nx6qMTkclKFiDOYfJnL4" 
access_token = "893138211135934464-kqZOl6DpyCtEpomOpeEA58Cn3KsU9Ot" 
access_token_secret = "9aodXffH6zIoWz7mZ8RI1CnJ8aIGIOVyOMaH0hrPROdYG" 
  
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

