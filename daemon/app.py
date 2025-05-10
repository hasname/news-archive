#!/usr/bin/env python3

from apscheduler import Scheduler

with Scheduler() as scheduler:
    scheduler.run_until_stopped()
