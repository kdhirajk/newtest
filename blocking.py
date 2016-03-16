from datetime import datetime
import os
from pytz import utc,timezone
import time
import tzlocal
import pytz


from apscheduler.schedulers.blocking import BlockingScheduler



def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    #tzone=tzlocal.get_localzone()
    tzone = pytz.timezone('Australia/Tasmania')
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    #give the current time to schedule the trigger
    loc=tzone.localize(datetime(2016, 03, 16, 21, 53, 00))
    utc_time=pytz.utc.normalize(loc.astimezone(pytz.utc))
    fmtd_time=utc_time.strftime(fmt)
    print "utc time %s"%(fmtd_time)

    #extract the date time 
    year=fmtd_time.split()[0].split('-')[0]
    month=fmtd_time.split()[0].split('-')[1]
    day=fmtd_time.split()[0].split('-')[2]
    hour=fmtd_time.split()[1].split(':')[0]
    mins=fmtd_time.split()[1].split(':')[1]
    sec=fmtd_time.split()[1].split(':')[2]
    
    scheduler = BlockingScheduler(timezone=utc)
    #scheduler.add_job(tick, 'cron',year=2016,month=03,day=16,hour=10,minute=28)
    scheduler.add_job(tick, 'cron',year=year,month=month,day=day,hour=hour,minute=mins,second=sec)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
