#!/usr/bin/env python3

from apscheduler.schedulers.blocking import BlockingScheduler
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from readability import Document

import datetime
import requests
import urllib.parse

def CnaJob():
    all_url = 'https://www.cna.com.tw/list/aall.aspx'
    res = requests.get(all_url)
    soup = BeautifulSoup(res.text)
    for e in soup.select('#jsMainList > li'):
        link_url_relative = e.select('a')[0]['href']
        link_url = urllib.parse.urljoin(all_url, link_url_relative)

        link_title = e.select('a h2')[0].text

        # append to /tmp/url-cna.txt
        with open('/tmp/url-cna.txt', 'a') as f:
            res = requests.get(link_url)
            soup = BeautifulSoup(res.text)

            article_title = soup.select('.centralContent h1')[0].text
            article_content = soup.select('.centralContent')[0].text

            # arc90's readability
            doc = Document(res.text)
            readability_title = doc.title()
            readability_summary = doc.summary()

            now = datetime.datetime.now()

            f.write(f'* cna_aall.aspx: {now} {link_url} {link_title}\n')
            f.write(f'* DOM-based: {now} {link_url} {article_title} {article_content}\n')
            f.write(f'* Readability-based: {now} {link_url} {readability_title} {readability_summary}\n')

def main():
    load_dotenv()

    scheduler = BlockingScheduler()
    scheduler.add_job(CnaJob, 'interval', minutes=2)
    scheduler.start()

if __name__ == '__main__':
    main()
