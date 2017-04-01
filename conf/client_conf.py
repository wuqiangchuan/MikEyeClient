#!/bin/env python2.7
#coding:utf-8
##### code  by  mik ####
##### qiangchuan.wu ####

#存放mikeye 的client配置信息

ClientConfig = {
    'HostId': '1',
    'Service': '127.0.0.1',
    'Port': '8000',
    'ClientUpdateInterval': 120,            #获取server存储监控项的时间间隔。
    'Method': 'get',
    'RequstTimeOut': 30,
    'InteraCtion': {
        'GetConfigs':'/api/client/config/', #获取服务器端所定义的配置信息
        'PostMsg': 'api/client/post/',      #用于汇报客户端的信息
        }     
    }
