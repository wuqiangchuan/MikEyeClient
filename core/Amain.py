#!/bin/env python2.7
#coding:utf-8
##### code  by  mik ####
##### qiangchuan.wu ####

#将会调用bin目录中的方法与服务器端进行交互。
import  sys
from bin import ConnToServ

class CommandArgv(object):
    def __init__(self,SysArgv):
        self.argv = SysArgv
       
       
    def Command(self):
        print self.argv[1]  
        
        if hasattr(self, self.argv[1]):
            func = getattr(self, self.argv[1])
            return func()
        else:
            print self.HelpMsg()
    
    def HelpMsg(self):
        print "Usage:  MikeyeStart {start | stop} "
        
        
    def start(self):
        print "Start MikeyeClient....."
        FLAG =True
        while FLAG:
            RunClient = ConnToServ.Client()
            RunClient.Forever()    
        
        
    
    def stop(self):
        print "Stop  MikeyeClient....."