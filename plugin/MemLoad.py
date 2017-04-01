#!/bin/env python2.7
#coding:utf-8
##### code  by  mik ####
##### qiangchuan.wu ####
import psutil
from comm import TurnTo
from comm import SendToServer



@SendToServer 
def Mem(arg01,arg02):
    MemUsed={}
    
    mem = psutil.virtual_memory()
    MemUsed['Total'] = TurnTo(mem.total)
  
    MemUsed['Free'] = TurnTo(mem.free+mem.buffers+mem.cached)

    print 'iam memused',MemUsed
    return MemUsed