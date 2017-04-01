#!/bin/env python2.7
#coding:utf-8
##### code  by  mik ####
##### qiangchuan.wu ####
import commands
import re
from comm import SendToServer



@SendToServer
def Disk(arg01,arg02):
    Disk2=[]
  
    Disk=commands.getoutput('df -h')
    
    Disk=Disk.split('\n')

    Disk=Disk[1:]
    for I in Disk:
        I = re.sub(' +',' ',I)
        Disk2.append(I)
    
    Fdisk=[]
    for i in Disk2:
        a = i.split(' ')
        Fdisk.append(a)
        
    return Fdisk


'''

def DiskUsed():
    Disk2=[]
    C=[]
    Disk=commands.getoutput('df -h')
    Disk=Disk.split('\n')
    Disk[2]=Disk[1]+Disk[2]
    Disk=Disk[2:]
    for I in Disk:
        I = re.sub(' +',' ',I)
        Disk2.append(I)
    
    Fdisk=[]
    for i in Disk2:
        a = i.split(' ')
        Fdisk.append(a)
        
    DiskInfo={}
    LEN=len(Fdisk)
    for B in range(0,LEN):
        C.append(Fdisk[B][1])
        C.append(Fdisk[B][2])
        C.append(Fdisk[B][5])

        DiskInfo[Fdisk[B][0]]=C
    
    return DiskInfo
''' 
