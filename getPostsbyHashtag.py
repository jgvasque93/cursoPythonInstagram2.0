# -*- coding: utf-8 -*-
#
import time
import csv
import pandas as pd
import json
from datetime import datetime

def timestampToPTtime(created_utc):
    try:
        sinceDate = datetime.fromtimestamp(int(created_utc))
        datetimePT=str(sinceDate)
    except Exception as e:
        datetimePT=None
        print(e,'-')
    return datetimePT


def getPostsbyHashtag(session,head,API,hashtag,quantity):
    topics_dict = {
            "tagname":[], 
            "pk":[], 
            "idpost":[],
            "shortcode":[],
            "taken_at_timestamp":[],
            "date":[],
            "edge_media_to_comment":[],
            "edge_liked_by":[],
            "caption":[],
            "is_video":[],
            "video_view_count":[],
            }
    tamanTag=int(quantity)
    ArrayPosts=0
    lensave=1000
    try:
        urlScraping="""https://www.instagram.com/graphql/query/?query_hash=90cba7a4c91000cf16207e4f3bee2fa2&variables={"tag_name":"Hashtag","first":50,"after":"max_id"}"""
        max_id=''
        has_next_page='true'
        exit=False
        oportunity=0
        while(has_next_page=='true' and exit==False):
            try:
                url=urlScraping.replace('Hashtag',str(hashtag)).replace('max_id',max_id)
                response=session.get(url,headers=head)
                has_next_page=json.dumps(response.json()['data']['hashtag']['edge_hashtag_to_media']['page_info']['has_next_page'])
                if(has_next_page=='true'):
                    max_id=json.dumps(response.json()['data']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor'])
                    max_id=str(max_id).replace('\"','')
                Posts=response.json()['data']['hashtag']['edge_hashtag_to_media']['edges']
                print(ArrayPosts,'len',has_next_page,hashtag)
                oportunity=0
                for Post in Posts:
                    try:
                        idpost=""
                        pk=""
                        shortcode=""
                        taken_at_timestamp=""
                        edge_media_to_comment=""
                        edge_liked_by=""
                        caption=""
                        fecha=""
                        try:
                            pk=str(Post['node']['owner']['id'])
                        except Exception as e:
                            pk=""

                        try:
                            idpost=str(Post['node']['id'])
                        except Exception as e:
                            idpost=''
                        try:
                            shortcode='https://www.instagram.com/p/'+str(Post['node']['shortcode'])
                        except Exception as e:
                            shortcode=""
                        
                        try:
                            taken_at_timestamp=str(Post['node']['taken_at_timestamp'])
                        except Exception as e:
                            taken_at_timestamp=""
                        
                        try:
                            fecha=timestampToPTtime(int(taken_at_timestamp))

                        except Exception as e:
                            raise e
                        
                        try:
                            edge_media_to_comment=str(Post['node']['edge_media_to_comment']['count'])
                        except Exception as e:
                            edge_media_to_comment=""

                        try:
                            edge_liked_by=str(Post['node']['edge_liked_by']['count'])
                        except Exception as e:
                            edge_liked_by=""
                        try:
                            is_video=str(Post['node']['is_video'])
                            if(is_video=='True'):
                                video_view_count=str(Post['node']['video_view_count'])
                            else:
                                video_view_count=''
                        except Exception as e:
                            is_video=""
                            video_view_count=''

                        try:
                            caption=str(Post['node']['edge_media_to_caption']['edges'][0]['node']['text'])
                            caption= caption.replace('\n', ' ').replace('\r', ' ').replace("\t"," ")#.replace('~', ' ').replace('`', ' ') 
                        except Exception as e:
                            caption=""
                        if(ArrayPosts>=tamanTag):
                            topics_dict["tagname"].append(str(hashtag))
                            topics_dict["pk"].append(str(pk))
                            topics_dict["idpost"].append(str(idpost))
                            topics_dict["shortcode"].append(str(shortcode))
                            topics_dict["taken_at_timestamp"].append(str(taken_at_timestamp))
                            topics_dict["date"].append(str(fecha))
                            topics_dict["edge_media_to_comment"].append(str(edge_media_to_comment))
                            topics_dict["edge_liked_by"].append(str(edge_liked_by))
                            topics_dict["caption"].append(str(caption))
                            topics_dict["is_video"].append(str(is_video))
                            topics_dict["video_view_count"].append(str(video_view_count))
                            frame = pd.DataFrame(topics_dict)
                            return frame
                            
                                    #return None
                        else:
                            #pass
                            topics_dict["tagname"].append(str(hashtag))
                            topics_dict["pk"].append(str(pk))
                            topics_dict["idpost"].append(str(idpost))
                            topics_dict["shortcode"].append(str(shortcode))
                            topics_dict["taken_at_timestamp"].append(str(taken_at_timestamp))
                            topics_dict["date"].append(str(fecha))
                            topics_dict["edge_media_to_comment"].append(str(edge_media_to_comment))
                            topics_dict["edge_liked_by"].append(str(edge_liked_by))
                            topics_dict["caption"].append(str(caption))
                            topics_dict["is_video"].append(str(is_video))
                            topics_dict["video_view_count"].append(str(video_view_count))
                            ArrayPosts=ArrayPosts+1

                    except Exception as e:
                        print("Exception iter:",e)
                print('errores', oportunity)
            except Exception as e:
                print("While except:",e)
                time.sleep(10)

        frame = pd.DataFrame(topics_dict)
        return frame
    except Exception as e:
        print("Main Exception: "+str(e))
        return None
