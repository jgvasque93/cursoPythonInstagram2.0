# -*- coding: utf-8 -*-
#
from InstagramAPI import InstagramAPI
import requests


def login_Instagram_Session(usernameD,paswordD):
    baseUrl='https://www.instagram.com/'
    loginUrl=baseUrl+'accounts/login/ajax/'
    username=usernameD
    pasword=paswordD
    session = requests.Session()
    head = {'Content-type':'application/json','Accept':'application/json'}
    userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
    session.headers={'user-agent':userAgent}
    session.headers.update({'Referer':baseUrl})
    req=session.get(baseUrl)
    session.headers.update({'X-CSRFToken':req.cookies['csrftoken']})
    login_data={'username':username,'password':pasword}
    login=session.post(loginUrl,data=login_data,allow_redirects=True)
    session.headers.update({'X-CSRFToken':login.cookies['csrftoken']})
    cookies=login.cookies
    return session,head
def login_Instagram_Api(usernameD,paswordD):
    API = InstagramAPI(usernameD,paswordD)
    API.login()
    return API

