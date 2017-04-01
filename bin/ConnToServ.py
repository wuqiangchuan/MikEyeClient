#!/bin/env python2.7
#coding:utf-8
##### code  by  mik ####
##### qiangchuan.wu ####
#添加设定环境变量，以免找不到(通常是Pychrm才会这样)
from conf.client_conf import ClientConfig
''' import sys 
import os 
BaseDir = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
sys.path.append(BaseDir)  '''
#用于每隔一个固定时长就去服务器端加载所监控的项目
import time
from conf import client_conf
import urllib
import urllib2
import json
import plugin


class SendMsg(object):
    def __init__(self):
        pass
''''
    def HardWare(self):
        
        req = urllib2.Request(url)  
        data = urllib.urlencode(data)  
        #enable cookie  
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())  
        response = opener.open(req, data)  
        return response.read()  
    
     
        posturl = "http://127.0.0.1:8000/HardWareInfo/msg/"  
        data = {'email':'myemail', 'password':'mypass', 'autologin':'1', 'submit':'登 录', 'type':''}  
        print post(posturl, json.dumps(data)) 
         
         
    def Stat(self):
        pass   
    '''
 
    
        
class Client(object):
    def __init__(self):
        self.ServerConf = None
    
    def LoadLatestConf(self):
        ActionType = client_conf.ClientConfig['Method']
        Url = 'http://'+client_conf.ClientConfig['Service']+":"+client_conf.ClientConfig['Port']+client_conf.ClientConfig['InteraCtion']['GetConfigs']+client_conf.ClientConfig['HostId']
        
        GetServerConf = self.UrlRequest(ActionType,Url)
        self.ServerConf = json.loads(GetServerConf)
        return self.ServerConf
        
    def Forever(self):
        FLAG=True
        
        #设定时间，每隔多久就得去获取配置，并应用其配置。
        ConfigLatesTime = 0
        while FLAG:
            if time.time() - ConfigLatesTime > client_conf.ClientConfig['ClientUpdateInterval']:
                self.LoadLatestConf()
                #time.sleep(client_conf.ClientConfig['ClientUpdateInterval'])
                print "latest conf: ",self.ServerConf
                ConfigLatesTime = time.time()
            print self.ServerConf  
            #   {"service": {"LinuxCPU": ["CPU", 60, 1479454740.208979], "LinuxLoad": ["load", 90]}}
            for ServiceName,Val in self.ServerConf['service'].items():
                if len(Val) == 2:
                    self.ServerConf['service'][ServiceName].append(time.time())
                   
                MonitorInterval = Val[1]
                LatestIntervalTime = Val[2]
                
                
                #如果当前时间减去，上次获取的时间，大于，设定的间隔时长，则重新去获取最新数据。
                #if time.time() -  ConfigLatesTime > client_conf.ClientConfig['ClientUpdateInterval']:
                if time.time() -  LatestIntervalTime > MonitorInterval:
                    print 'new get -----------------------------------------config',LatestIntervalTime,time.time()
                    print "go to monitor %s "  % ServiceName
                    #把监控情况发送写在这里。
                    FirstSite = __import__('plugin.'+ServiceName)
                    func = getattr(FirstSite, ServiceName)
                    PluginAction = getattr(func, Val[0])
                    print PluginAction('stat',ServiceName)
                    
                    self.ServerConf['service'][ServiceName][2] = time.time()
                else:
                    print "Go to monitor [%s] in [%s] " %(ServiceName,MonitorInterval - (time.time()-LatestIntervalTime))
                    
            
            time.sleep(1)
            


       
    def UrlRequest(self,action,url,**kwargs):        
        ''' action:   get|post
             url:     url
             **kwargs:somethins
             ''' 
        if action in ('get','GET'):
            print 'url is :',url
            try:
                Req = urllib2.Request(url)
                Data = urllib2.urlopen(Req, timeout=client_conf.ClientConfig['RequstTimeOut'],)
                DataText = Data.read()
                print DataText
                 #因为传过来的是json序列。这里就必须反序列化
                
                return DataText
            except Exception,e:
                print '出现错误,',e 
                return e
            
            
