# -*- coding: utf-8 -*-
#
import time
import pandas as pd
import json
import codecs
import unicodedata
from datetime import datetime

def getComentsPost(session,head,post):
    try:
        urlScraping='https://www.instagram.com/graphql/query/?query_hash=33ba35852cb50da46f5b5e889df7d159&variables={"shortcode":"codeSHORT","include_reel":true,"first":50,"after":"max_id"}'
        url = post
        media_id=url.split('/')[-1]
        if(media_id==''):media_id=url.split('/')[-2]
        print("shorcode: "+str(media_id))
        max_id = ''
        has_next_page = 'true'
        usernames=[]
        ids=[]
        text=[]
        dates=[]
        ids=[]
        while has_next_page=='true':
            try:
                url=urlScraping.replace('codeSHORT',media_id).replace('max_id',max_id)
                response=session.get(url,headers=head)
                has_next_page=json.dumps(response.json()['data']['shortcode_media']['edge_media_to_comment']['page_info']['has_next_page'])
                if(has_next_page):
                    max_id=json.dumps(response.json()['data']['shortcode_media']['edge_media_to_comment']['page_info']['end_cursor'])
                    max_id=str(max_id).replace('\"','')
                comments_=response.json()['data']['shortcode_media']['edge_media_to_comment']['edges']
                print(len(comments_),'len',has_next_page)
                for comment in comments_:
                    try:
                        info=str(comment['node']['owner']['username'])
                        usernames.append(info)
                    except Exception as e:
                        usernames.append('')
                    try:
                        id=str(comment['node']['id'])
                        ids.append(id)
                    except Exception as e:
                        ids.append('')
                    
                    try:
                        info=comment['node']['owner']['text']
                        info= info.replace(',', '').replace(';', ' ')
                        info= info.replace("\n", "").replace("\r", "")
                        text.append(info)
                    except Exception as e:
                        info=comment['node']['text']
                        info= info.replace(',', '').replace(';', ' ')
                        info= info.replace("\n", "").replace("\r", "")
                        text.append(info)
                    try:
                        info=str(comment['node']['owner']['created_at'])
                        dates.append(datetime.utcfromtimestamp(int(info)).strftime('%Y-%m-%d %H:%M:%S'))
                    except Exception as e:
                        info=str(comment['node']['created_at'])
                        dates.append(datetime.utcfromtimestamp(int(info)).strftime('%Y-%m-%d %H:%M:%S'))
            except Exception as e:
                print(e)
                time.sleep(10)
        print(len(usernames))
        df = pd.DataFrame()   
        df['usernames']=usernames
        df['ids']=ids
        df['text']=text
        df['date']=dates
        return df

    except Exception as e:
        print("Main Exception: "+str(e))
        return None

def getLikesPost(session,head,post):
    try:
        urlScraping='https://www.instagram.com/graphql/query/?query_hash=d5d763b1e2acf209d62d22d184488e57&variables={"shortcode":"codeSHORT","include_reel":true,"first":50,"after":"max_id"}'
        url = post
        print("url: "+str(url))
        media_id=url.split('/')[-1]
        if(media_id==''):media_id=url.split('/')[-2]
        max_id = ''
        has_next_page = 'true'
        full_names=[]
        usernames=[]
        ids=[]
        while has_next_page=='true':
            try:
                url=urlScraping.replace('codeSHORT',media_id).replace('max_id',max_id)
                response=session.get(url,headers=head)
                has_next_page=json.dumps(response.json()['data']['shortcode_media']['edge_liked_by']['page_info']['has_next_page'])
                if(has_next_page):
                    max_id=json.dumps(response.json()['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor'])
                    max_id=str(max_id).replace('\"','')
                likers=response.json()['data']['shortcode_media']['edge_liked_by']['edges']
                print(len(usernames),'len',has_next_page)
                for like in likers:
                    try:
                        info=str(like['node']['username'])
                        usernames.append(info)
                    except Exception as e:
                        usernames.append('')
                    id=str(like['node']['id'])
                    ids.append(id)
            except Exception as e:
                print(e,like)
                time.sleep(10)
        print(len(usernames))
        df = pd.DataFrame()   
        df['usernames']=usernames
        df['ids']=ids

        return df
    except Exception as e:
        print("Main Exception: "+str(e))
        return None
