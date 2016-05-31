#!/usr/bin/env python
__author__ = 'TzuTaLin'

import urllib2
import os
from bs4 import BeautifulSoup
import json

def getSoup(url):
  return BeautifulSoup(urllib2.urlopen(url).read().decode('utf-8'), 'html.parser')

def appendToTable(title, link):
    json_data = None
    jsonFile='table.json'
    with open(jsonFile) as json_file:
        json_data = json.load(json_file)
        print(json_data)

    if json_data is not None:
        json_data[title] = link
        with open(jsonFile, mode='w') as f:
            json.dump(json_data, f)

if __name__=='__main__':
    print 'Getting the latest NDK version'
    soup = getSoup('https://developer.android.com/ndk/downloads/index.html')
    all_td = soup.findAll('td')

    linux_td = None
    for each_td in all_td:
        if 'linux' in str(each_td):
            linux_td = each_td
            break

    download_link=linux_td.a.get('href')
    title=linux_td.a.getText().split('.', 1)[0]
    appendToTable(title, download_link)

