#!/bin/env python2.7
#coding:utf-8
##### code  by  mik ####
##### qiangchuan.wu ####
from comm import TurnTo
import psutil
from comm import SendToServer



@SendToServer 
def Swap(arg01,arg02):
    SwapUsed={}

    swap=psutil.swap_memory()
    SwapUsed['Total'] = TurnTo(swap.total)
    SwapUsed['Free'] = TurnTo(swap.free)
    print SwapUsed
    return SwapUsed
