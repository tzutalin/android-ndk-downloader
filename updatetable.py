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

    if json_data is not None:
        print "Append a new ndk download_link if not existed:" + title
        json_data[title] = link
        with open(jsonFile, mode='w') as f:
            json.dump(json_data, f, indent=4, sort_keys=True)

if __name__=='__main__':
    print 'Getting the latest NDK version'
    soup = getSoup('https://developer.android.com/ndk/downloads/index.html')
    all_td = soup.findAll('td')

    download_os = ['linux', 'windows', 'darwin']
    for os_td in download_os:
        for each_td in all_td:
            if os_td in str(each_td):
                os_td = each_td
                break

        download_link=os_td.a.get('href')
        title=os_td.a.getText().split('.', 1)[0]
        appendToTable(title, download_link)

