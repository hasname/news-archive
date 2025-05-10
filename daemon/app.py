#!/usr/bin/env python3

from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv
import os
import requests

def SlackTestJob():
    url = os.environ.get('SLACK_WEBHOOK_URL')

def main():
    load_dotenv()

    scheduler = BlockingScheduler()
    scheduler.add_job(SlackTestJob, 'interval', minutes=1)
    scheduler.start()

if __name__ == '__main__':
    main()
