from twitter_scraper import get_tweets, Profile
from datetime import date
import pandas as pd
from urllib.request import urlopen 

column_names = ["Link", "Retweet", "Text", "Time", "Replies", "Retweets", "Likes", "Username", "P_Location", "P_Name", "P_Followers", "P_Photo"]
df=pd.DataFrame(columns=column_names)
def searcher(hashes, pgcount):
    #Each page has 20 tweets
    global df
    for tweet in get_tweets(hashes, pages=pgcount):
        dic={}
        dic['Link']="twitter.com/anyuser/status/"+tweet['tweetId']
        dic['Retweet']=tweet['isRetweet']
        dic['Text']=tweet['text']
        dic['Time']=str(tweet['time'])
        dic['Replies']=tweet['replies']
        dic['Retweets']=tweet['retweets']
        dic['Likes']=tweet['likes']
        dic['Hashtags']=''.join(tweet['entries']['hashtags'])
        dic['Photos']=''.join(tweet['entries']['photos'])
        dic['Urls']=''.join(tweet['entries']['urls'])
        dic['Videos']=str(tweet['entries']['videos'])
        page = urlopen("https://twitter.com/anyuser/status/"+tweet['tweetId'])
        uname=page.geturl()[20:].split("/",1)[0]
        dic['Username']=uname
        profile=Profile(uname)
        dic['P_Location']=profile.location
        dic['P_Name']=profile.name
        dic['P_Followers']=profile.followers_count
        dic['P_Photo']=profile.profile_photo
        
        df=df.append(dic, ignore_index=True)

def setup(hashes, pgcount):
    global df
    searcher(hashes, pgcount)
    df.to_csv('Tweets-{}-{}.csv'.format(str(date.today()),str(hashes)), index=False)