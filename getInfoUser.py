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

def getInfoUser(session,head,USERNAME):
    try:
        info=[]
        urlScraping="""https://www.instagram.com/USERNAME/?__a=1"""
        urlScraping=urlScraping.replace('USERNAME',USERNAME)
        response=session.get(urlScraping,headers=head)
        infoUser=response.json()['graphql']['user']
        try:
            print(infoUser)
            biography=infoUser['biography']
            biography= biography.replace(',', '').replace(';', ' ')
            biography= biography.replace("\n", "").replace("\r", "")

            followers=infoUser['edge_followed_by']['count']
            followings=infoUser['edge_follow']['count']
            full_name=infoUser['full_name']
            is_private=infoUser['is_private']
            username=infoUser['username']
            id=infoUser['id']

            info.append([username,id,biography,followers,followings,is_private,full_name])
        except Exception as e:
            print(e)
        df = getDataframe([['username','id','biography','followers','followings','is_private','full_name']]+info)   
        return df
    except Exception as e:
        print(e)
        return None