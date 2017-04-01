#!/bin/env python2.7
#coding:utf-8
##### code  by  mik ####
##### qiangchuan.wu ####
import psutil
import time 
from comm import SendToServer
from comm import half



@SendToServer
def CPU(arg01,arg02):
    LinuxCPU={}
    
    CpuIdle01 = psutil.cpu_times_percent().idle
    CpuIowait01 = psutil.cpu_times_percent().iowait
    CpuUser01 = psutil.cpu_times_percent().user
    CpuSystem01 = psutil.cpu_times_percent().system
    time.sleep(30)
    
    CpuIdle02 = psutil.cpu_times_percent().idle
    CpuIowait02 = psutil.cpu_times_percent().iowait
    CpuUser02 = psutil.cpu_times_percent().user
    CpuSystem02 = psutil.cpu_times_percent().system
    
    CpuIdle = half(CpuIdle01, CpuIdle02)
    CpuIowait = half(CpuIowait01, CpuIowait02)
    CpuUser  = half(CpuUser01, CpuUser02)
    CpuSystem = half(CpuSystem01, CpuSystem02)
    
    LinuxCPU['Idle'] = CpuIdle
    LinuxCPU['Iowait'] = CpuIowait
    LinuxCPU['User'] = CpuUser
    LinuxCPU['System'] = CpuSystem
    print LinuxCPU
    return LinuxCPU