from datetime import datetime
import os
from pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__=="__main__":
    sched=BackgroundScheduler(timezone=utc)
    sched.add_job(tick,'cron',hour=10,minute=10,second=10)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        sche.start()
    except (KeyboardInterrupt, SystemExit):
        pass

    
