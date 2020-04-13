from loginInstagram import *
from getPostsbyHashtag import *
from getCommnets_Likes_Post import *
from getRecentActivity import *
from getInfoUser import *
from funtionsApiInstagram import *
from getSuggested import *

import json
import pandas as pd
def readCredentilas():
	with open('credentials.json') as file:
		data = json.load(file)['credentials']
	return data
jsonData=readCredentilas()
session,head=login_Instagram_Session(jsonData['user'],jsonData['password'])
API=login_Instagram_Api(jsonData['user'],jsonData['password'])


results=getActivityRecent(session,head)
print(results)

results=getPostsbyHashtag(session,head,API,'tech',5)
print(results)
results=getComentsPost(session,head,'https://www.instagram.com/p/B-2DXQEJ9EK/')
print(results)
results=getLikesPost(session,head,'https://www.instagram.com/p/B-2DXQEJ9EK/')
print(results)

results=getInfoUser(session,head,'claudiananda')
print(results)
results=getSuggested(session,head)
print(results)
results=getTimeline(API,'itbearyoutube',4)
print(results)
results=getInfoUserApi(API,'nicolineenielsen')
print(results)

