#!/bin/env python2.7
#coding:utf-8
##### code  by  mik ####
##### qiangchuan.wu ####
import urllib
import urllib2
import json
from conf import client_conf
#from bin import ConnToServ
''' Conf = ConnToServ.Client()
Conf.LoadLatestConf()

def post(url, data):  
    req = urllib2.Request(url)  
    data = urllib.urlencode(data)  
    #enable cookie  
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())  
    response = opener.open(req, data)  
    return response.read()  
  
def main():  
    posturl = "http://127.0.0.1:8000/HardWareInfo/msg/"  
    data = {'email':'myemail', 'password':'mypass', 'autologin':'1', 'submit':'登 录', 'type':''}  
    print post(posturl, json.dumps(data))  
  
if __name__ == '__main__':  
    main()   '''
    
data = {'name':'aname'}   
a=urllib2.urlopen('http://192.168.56.1:8000/HardWareInfo/msg/',json.dumps(data))
b=a.read()
for i in b:
    print i