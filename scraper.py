from facebook_scraper import get_posts
from datetime import date
import pandas as pd

column_names = ["Post ID", "Time", "Text", "Image", "URL", "Likes", "Comments", "Link"]
df=pd.DataFrame(columns=column_names)
def searcher(pgname, pgcount):
    #per page carries a set of 4 posts
    #page 1 is rate-limited to 2 posts
    global df
    pgname=str(pgname)
    print(pgname)
    for post in get_posts(pgname,sleep=0, pages=pgcount, credentials=None, extra_info=True):
        dic={}
        dic['Post ID']=post['post_id']
        dic['Time']=str(post['time'])
        dic['Text']=post['text']
        dic['Image']=post['image']
        dic['URL']=post['post_url']
        dic['Likes']=post['likes']
        dic['Comments']=post['comments']
        dic['Link']=post['link']   
        print(dic)
        df=df.append(dic, ignore_index=True)

def start(pgname, pgcount):
    searcher(pgname, pgcount)
    df.to_csv('FB-Posts-{}-{}.csv'.format(str(date.today()), str(pgname)), index=False)
    print(df)