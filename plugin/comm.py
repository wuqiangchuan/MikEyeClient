#!/bin/env python2.7
#coding:utf-8
##### code  by  mik ####
##### qiangchuan.wu ####

# sum/1024/1024 = 

import urllib2
import json
import time 
from conf.client_conf import ClientConfig

def half(arg01,arg02):
    return (arg01 + arg02)/2


def TurnTo(arg01):
    arg01=arg01/1024/1024
    return arg01


def StrToInt(arg01):
    if type(arg01) == 'int':
        return arg01
    elif type(arg01) == 'str':
        return int(arg01)
    else:
        print  'StrToInt  func error.'
        return 'StrToInt  func error.'
    
    
#作为一个Wapper，使用在把数据发送服务器端
def SendToServer(func):
    def wapper(arg01,arg02):
        data = func(arg01,arg02)
        url='http://'+ClientConfig['Service'] + ':' + ClientConfig['Port'] + '/' + arg01 + '/' + arg02+'/'
                
        try:
            a=urllib2.urlopen(url,json.dumps(data))
            for i in a:
                print i
                if i != 'ok':
                    time.sleep(1)
                    a=urllib2.urlopen(url,json.dumps(data))
        except Exception,e:
            print 'url data post error..'
        
        
        return data
    return wapper 
         
        
        
        
