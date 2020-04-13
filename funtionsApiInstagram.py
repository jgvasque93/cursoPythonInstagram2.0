# -*- coding: utf-8 -*-
#
from datetime import datetime
import pandas as pd
import time
def getDataframe(valuesSettings):
    df = pd.DataFrame.from_records(valuesSettings)
    new_header = df.iloc[0] #grab the first row for the header
    df = df[1:] #take the data less the header row
    df.columns = new_header #set the header row as the df header
    #df['Division']=df['Division'].str.title()
    return df.reset_index(drop=True)
def unfollow(API,user):
	g = API.unfollow(user)
	time.sleep(1)

def follow(API,user):
	g = API.follow(user)
	time.sleep(1)

def likePost(API,id):
	g = API.like(id)
	time.sleep(1)

def commentPosts(API,id,text):
	g = API.comment(id,text)
	time.sleep(1)

def getTimeline(API,username,numberPosts):
    API.searchUsername(username)
    t=API.LastJson
    countPosts=0
    try:
        if(t['status']!='fail' and not t['user']['is_private']):
            user_id=str(t['user']['pk'])
            posts=[]
            next_max_id = ''
            g = API.getUserFeed(user_id,next_max_id)
            temp = API.LastJson
            if(int(temp['num_results'])>0):
                while 1:
                    try:
                        while g==False:
                            print("wait")
                            n = randint(50,90)
                            time.sleep(3*n)
                            g = API.getUserFeed(user_id,next_max_id)
                            temp = API.LastJson
                        print('reading')
                        for item in temp["items"]:
                            ite=[]
                            ite.append(username)
                            try:
                                ite.append(item['like_count'])
                            except Exception as e:
                                ite.append(0)
                            try:
                                ite.append(item['comment_count'])
                            except Exception as e:
                                ite.append(0)

                            ts=int(item['taken_at'])
                            fecha=datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                            ite.append(fecha)
                            ite.append(str(item['code']))

                            try:
                                texto=item['caption']['text'].replace(',',' ').replace('\t',' ').replace('\r',' ').replace('\n',' ').replace('\"',' ')
                                ite.append(texto)
                            except Exception as e:
                                ite.append('')
                            if(len(posts)>=numberPosts):
	                            df = getDataframe([['username','like_count','comment_count','date','shorcode','text']]+posts)   

	                            return df
                            else:
                                posts.append(ite)
                        if temp["more_available"] == False:
                            df = getDataframe([['username','like_count','comment_count','date','shorcode','text']]+posts)   

                            return df
                        next_max_id = temp["next_max_id"]
                        g = API.getUserFeed(user_id,next_max_id)
                        temp = API.LastJson
                    except ValueError:
                        print(ValueError)
        else:
            None
    except Exception as e:
        print(e)
        return None
