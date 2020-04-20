from loginInstagram import *
from getPostsbyHashtag import *
from getCommnets_Likes_Post import *
from getRecentActivity import *
from getInfoUser import *
from funtionsApiInstagram import *
from getSuggested import *
from busquedaInstagram import *

import json
import pandas as pd

def readCredentilas():
	with open('credentials.json') as file:
		data = json.load(file)['credentials']
	return data

#lee las credenciales del file credentials
jsonData=readCredentilas()
session,head=login_Instagram_Session(jsonData['user'],jsonData['password'])
API=login_Instagram_Api(jsonData['user'],jsonData['password'])
#Buscar followers
hashtag=['pythoncode','programing','tech','cursopython','programingpython']
results=[]
for xhashtag in hashtag:
	result=getPostsbyHashtag(session,head,API,xhashtag,15)
	results.append(result)
resultsHashtags=pd.concat(results)
print(resultsHashtags)
pastPosts=[]
for indice_fila, fila in resultsHashtags.iterrows():
	posts=fila['shortcode']
	if(posts not in pastPosts):
		pastPosts.append(posts)
		print(posts)
		likePost(API,fila['idpost'])
		#importante esperar 120 segundos para que instgram no te bloquee esta opcion
		time.sleep(120)

try:
	dataOld=pd.read_csv("idsOld.csv", sep=';')
	idsFollow=dataOld['id'].astype(str).tolist()
except Exception as e:
	print(e)
	idsFollow=[]

results=getSuggested(session,head)
ids=results['id'].tolist()
ids=list(set(ids))
for xids in ids:
	if(xids not in idsFollow):
		idsFollow.append(xids)
		follow(API,xids)
		#importante esperar 120 segundos para que instgram no te bloquee esta opcion
		time.sleep(120)
results=getActivityRecent(session,head)
results=results[(results['__typename']!='GraphFollowAggregatedStory')].copy().reset_index(drop=True)
ids=results['id'].tolist()
ids=list(set(ids))
for xids in ids:
	if(str(xids) not in idsFollow):
		idsFollow.append(str(xids))
		follow(API,xids)
		#importante esperar 120 segundos para que instgram no te bloquee esta opcion
		time.sleep(120)


results=getTimeline(API,jsonData['user'],5)
shorcode=results['shorcode'].tolist()
resultsEngagers=[]
for xshorcode in shorcode:
	resultLike=getLikesPost(session,head,xshorcode)
	resultLike=resultLike['ids'].tolist()
	resultComments=getComentsPost(session,head,xshorcode)
	resultComments=resultComments['ids'].tolist()
	resultsEngagers=resultsEngagers+resultComments
	resultsEngagers=resultsEngagers+resultLike

ids=list(set(resultsEngagers))
for xids in ids:
	if(str(xids) not in idsFollow):
		idsFollow.append(str(xids))
		follow(API,xids)
		time.sleep(60)

idsOld = pd.DataFrame()   
idsOld['id']=idsFollow
idsOld['id']=idsOld['id'].astype(str)
idsOld.to_csv('idsOld.csv', sep=';', encoding='utf-8',index=False)
