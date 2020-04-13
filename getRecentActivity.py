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
def getActivityRecent(session,head):
    try:
        activity=[]
        urlScraping="""https://www.instagram.com/accounts/activity/?__a=1&include_reel=true"""
        response=session.get(urlScraping,headers=head)
        activities=response.json()['graphql']['user']['activity_feed']['edge_web_activity_feed']['edges']
        for xactivities in activities:
            try:
                __typename=str(xactivities['node']['__typename'])
                id=str(xactivities['node']['user']['id'])
                username=str(xactivities['node']['user']['username'])
                activity.append([__typename,id,username])
            except Exception as e:
                print(e)
        df = getDataframe([['__typename','id','username']]+activity)   
        return df
    except Exception as e:
        print(e)
        return None