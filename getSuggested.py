# -*- coding: utf-8 -*-
#
import time
import json
import pandas as pd
def getDataframe(valuesSettings):
    df = pd.DataFrame.from_records(valuesSettings)
    new_header = df.iloc[0] #grab the first row for the header
    df = df[1:] #take the data less the header row
    df.columns = new_header #set the header row as the df header
    #df['Division']=df['Division'].str.title()
    return df.reset_index(drop=True)
def getSuggested(session,head):
    try:
        suggesteds=[]
        urlScraping="""https://www.instagram.com/graphql/query/?query_hash=bd90987150a65578bc0dd5d4e60f113d&variables={"fetch_media_count":0,"fetch_suggested_count":50,"ignore_cache":true,"filter_followed_friends":true,"seen_ids":[],"include_reel":true}"""
        response=session.get(urlScraping,headers=head)
        suggested=response.json()['data']['user']['edge_suggested_users']['edges']
        for xsuggested in suggested:
            try:
                username=xsuggested['node']['user']['username']
                id=xsuggested['node']['user']['id']

                suggesteds.append([id,username])
            except Exception as e:
                print(e)
        df = getDataframe([['id','username']]+suggesteds)   
        return df
    except Exception as e:
        print(e)
        return None