# -*- coding: utf-8 -*-
#

import time
import pandas as pd
import json
def getDataframe(valuesSettings):
    df = pd.DataFrame.from_records(valuesSettings)
    new_header = df.iloc[0] #grab the first row for the header
    df = df[1:] #take the data less the header row
    df.columns = new_header #set the header row as the df header
    #df['Division']=df['Division'].str.title()
    return df.reset_index(drop=True)

def busquedaInstagram(session,head,TIPO,PARAMQUERY):
    try:
        urlScraping='https://www.instagram.com/web/search/topsearch/?context=TIPO&query=PARAMQUERY'
        has_next_page = 'true'
        usersARRAY=[]
        hashtagARRAY=[]
        placesARRAY=[]
        url=urlScraping.replace('PARAMQUERY',PARAMQUERY).replace('TIPO',TIPO)
        response=session.get(url,headers=head)
        if(TIPO=='user'):
            users=response.json()['users']
            for xusers in users:
                print(xusers)
                position=xusers['position']
                infoUser=xusers['user']
                pk=infoUser['pk']
                username=infoUser['username']
                full_name=infoUser['full_name']
                usersARRAY.append([position,pk,username,full_name])
            df = getDataframe([['position','pk','username','full_name']]+usersARRAY)   
            return df
        elif(TIPO=='hashtag'):
            hashtags=response.json()['hashtags']
            for xhashtags in hashtags:
                position=xhashtags['position']
                infohashtag=xhashtags['hashtag']
                name=infohashtag['name']
                id=infohashtag['id']
                media_count=infohashtag['media_count']
                hashtagARRAY.append([position,name,id,media_count])
            df = getDataframe([['position','name','id','media_count']]+hashtagARRAY)   
            return df
        elif(TIPO=='place'):
            places=response.json()['places']
            for xplaces in places:
                position=xplaces['position']
                infoplaces=xplaces['place']['location']
                try:
                    lng=infoplaces['lng']
                except Exception as e:
                    lng=''
                try:
                    lat=infoplaces['lat']
                except Exception as e:
                    lat=''
                pk=infoplaces['pk']
                name=infoplaces['name']
                address=infoplaces['address']
                city=infoplaces['city']
                placesARRAY.append([position,pk,lng,lat,name,address,city])
            df = getDataframe([['position','pk','lng','lat','address','city']]+placesARRAY)   
            return df
    except Exception as e:
        print("Main Exception: "+str(e))
        return None
