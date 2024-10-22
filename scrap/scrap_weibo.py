from lxml import etree
import requests
import random
import time
import csv
import urllib.parse
import pandas as pd 
import numpy as np
import re


#set the headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
           "cookie": "_T_WM=70826633062; XSRF-TOKEN=91898a; WEIBOCN_FROM=1110006030; MLOGIN=0; mweibo_short_token=0091bb7c26; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%25E6%259C%25BA%26fid%3D100103type%253D1%2526q%253D%25E6%259C%25BA%26uicode%3D10000011"}


columns = ['username', 'country', 'province', 'city', 'phone_terminal', 'content']
df = pd.DataFrame(columns=columns)
keyWord = "股票"
parse_keyWord = urllib.parse.quote(keyWord)
for num in range(15): 
    # 首页网址URL
    url = f'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D61%26q%3D{parse_keyWord}%26t%3D&page_type=searchall&page='+str(num+1)
    print(url)
    response = requests.get(url=url, headers=headers).json()
    card_list = response.get('data').get('cards')
    print("******************Start scrap page ",str(num+1),"******************")
    for i in range(len(card_list)):
        values = []
        if 'card_group' in card_list[i] and 'mblog' in card_list[i]:
            dict1 = card_list[i].get('card_group')[0].get('mblog')
            values.append(dict1.get('user').get('screen_name')) #username
            values.append(dict1.get('status_country')) #country
            values.append(dict1.get('status_province')) #province
            values.append(dict1.get('status_city')) #city
            values.append(dict1.get('source')) #phone_terminal
            values.append(re.sub("[A-Za-z0-9\!\%\[\]\,\。\<\=\"\:\/\.\/\?\&\-\>]", "", dict1.get('text'))) #content
            df = pd.concat([df,pd.DataFrame([values], columns=df.columns)],ignore_index=True)
            # print(values)
            
        elif 'mblog' in card_list[i]:
            dict1 = card_list[i].get('mblog')
            values.append(dict1.get('user').get('screen_name')) #username
            values.append(dict1.get('status_country')) #country
            values.append(dict1.get('status_province')) #province
            values.append(dict1.get('status_city')) #city
            values.append(dict1.get('source')) #phone_terminal
            values.append(re.sub("[A-Za-z0-9\!\%\[\]\,\。\<\=\"\:\/\.\/\?\&\-\>\_\; \_\ ; \']", "", dict1.get('text'))) #content
            df = pd.concat([df,pd.DataFrame([values], columns=df.columns)],ignore_index=True)
            # print(values)
    print("******************page",str(num+1),"srapped******************")

    df.to_csv(f'./scrapped_{keyWord}.csv')