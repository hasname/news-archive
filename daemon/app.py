#!/usr/bin/env python3

from apscheduler.schedulers.blocking import BlockingScheduler
from bs4 import BeautifulSoup
from dotenv import load_dotenv

import requests
import urllib.parse

def CnaJob():
    url = 'https://www.cna.com.tw/list/aall.aspx'
    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    for e in soup.select('#jsMainList > li'):
        link_relative = e.select('a')[0]['href']
        link = urllib.parse.urljoin(url, link_relative)

        title = e.select('a h2')[0].text

        # append to /tmp/url-cna.txt
        with open('/tmp/url-cna.txt', 'a') as f:
            f.write(f'{link} {title}\n')

def main():
    load_dotenv()

    scheduler = BlockingScheduler()
    scheduler.add_job(CnaJob, 'interval', minutes=2)
    scheduler.start()

if __name__ == '__main__':
    main()
