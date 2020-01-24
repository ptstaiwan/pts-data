#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:54:39 2019

@author: tynnie
"""

import requests
import pandas as pd


#column = ['地區', '姓名', '號次', '性別', '出生年次', '推薦政黨', '得票數', '得票率', '當選註記', '是否現任','選舉', '區域']
columnName = ['region', 'name', 'number', 'gender', 'birthYear', 'party', 'number of votes', 'percentage of votes', 'elected', 'incumbent','type of election','identity']
#主要網址
mainurl='https://db.cec.gov.tw/'

#事先蒐集各年份區域、平原與山原立委票數詳細資料位置（網址），資料順序為「（第幾屆立委）,（網址）,（區域、平原或山原）」
f = open('urlLink0114.csv','r')

#將蒐集好、要整理的資料位置（網址）讀出來
data_list = []
for row in f:
    data_list.append(tuple(row.strip().split(',')))

#開一個整理的dataframe
df = pd.DataFrame()

#開始倒資料
for data in data_list: 
    if '立法委員' in data[0]:
        #因為本資料不使用不分區資料，透過這個步驟把不需要的資料處理掉
        if data[1] != "不分區政黨":
            res = requests.get(mainurl+data[2],verify=False)
            #拿所需要的立委選舉資料（table）
            dfs = pd.read_html(res.text)      
            dfs =dfs[0]
            #為了後續整理方便，加入屆數與類型（區域、平原或山原）的資料
            dfs['type of election'] = data[0]
            dfs['identity'] = data[1]
            #為了自行設定名稱，把原本的表格（table）ㄊ首列（欄位名稱）移除
            dfs = dfs.iloc[1:]
            #併入dataframe
            df = df.append(dfs) 
#設定自己喜歡的欄位名稱
df.columns = columnName
#把dataframe存起來
df.to_csv('LegislatorAll0122（除不分區）.csv',index = None)