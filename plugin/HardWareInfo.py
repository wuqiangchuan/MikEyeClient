#!/bin/env python2.7
#coding:utf-8
##### code  by  mik ####
##### qiangchuan.wu ####

import platform
#from __future__ import print_function
import psutil
import uuid
import socket
import re
import commands

from comm import SendToServer






class HardWare(object):
    SysTem=platform.linux_distribution()
    #get hostname
    HostName=platform.uname()[1] 
    #架构
    Arch=platform.uname()[4]+'__'+platform.architecture()[0]

    #获取cpu逻辑数
    CpuLogical=psutil.cpu_count()
    CpuPhysics=psutil.cpu_count(logical=False)
    
    def cpu(self):
        with open('/proc/cpuinfo') as f:
            for line in f:
                # Ignore the blank line separating the information between
                # details about two processing units
                if line.strip():
                    if line.rstrip('\n').startswith('model name'):
                        model_name = line.rstrip('\n').split(':')[1]
                        return(model_name)
 
                    
# GetMac In Centos6.X
    def GetMacCentos6(self):
        ab=commands.getoutput('ifconfig')
        ab=ab.split('\n')
        s=[]
        MacInfo={}
        for i in ab:
                Str=re.findall('^eth.*',i)
                if Str != []:
                    s.append(Str)
                   
        #['eth0      Link encap:Ethernet  HWaddr 00:0C:29:B5:62:F0  ']
        for i in s[0]:
           MacGroup=re.search('(eth\d).*HWaddr(.*)',i)
           #print sb.group(1),"-->",sb.group(2)
           Str=MacGroup.group(2)
           Str=re.sub(' +','',Str)
           MacInfo[MacGroup.group(1)] = Str
           return MacInfo
    
    
    def GetMacCento7(self):
        
        a=commands.getoutput('ip add| grep -A 1 "^[0-9]:[[:space:]]en.*"|tail -1')
        b = re.match('^ +link', a)
        c = b.string
        c = re.sub('^ +', ' ', c)
        return c.split(' ')[2]


@SendToServer
def HardWareInfo(arg01,arg02):
    HW = {}
    obj = HardWare()
    A = obj.SysTem[1]
    if re.match('^6', A, ):
        MacInfo = obj.GetMacCentos6()
        #print 'centis6',MacInfo
    elif re.match('^7', A):
        MacInfo = obj.GetMacCento7()
        #print MacInfo
        
    HW['System'] = obj.SysTem[0] + '__' +obj.SysTem[1]
    HW['Host'] = obj.HostName
    HW['Arch'] = obj.Arch
    
    HW['CpuLogical'] = obj.CpuLogical
    HW['CpuPhysics'] = obj.CpuPhysics
    HW['Cpu'] = obj.cpu()
    
    HW['Mac'] = MacInfo
    print HW
    return HW


        