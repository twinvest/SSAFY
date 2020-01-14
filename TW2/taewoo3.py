import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re
import warnings
warnings.filterwarnings("ignore")

def callectUrl():
    urlList = list()
    for i in range(1, 11):
        url = "https://finance.naver.com/item/sise_time.nhn?code=035420&thistime=20200114120635&page="
        url = url + str(i)
        urlList.append(url)
    return urlList

def datacollect(urlList):
    for url in urlList:
        response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        tag = soup.find('table', {'class': 'type2'})
        print(tag)

urlList = callectUrl()
datacollect(urlList)