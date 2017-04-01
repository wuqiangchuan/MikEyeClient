#!/bin/env python2.7
#coding:utf-8
##### code  by  mik ####
##### qiangchuan.wu ####
from comm import SendToServer




@SendToServer
def load(arg01,arg02):
    LinuxLoad={}
    f = open("/proc/loadavg") 
    con = f.read().split() 
    f.close() 
    LinuxLoad['lavg_1']=con[0] 
    LinuxLoad['lavg_5']=con[1] 
    LinuxLoad['lavg_15']=con[2] 
    
    return LinuxLoad
    