from apscheduler.schedulers.blocking import BlockingScheduler
#importing our messaging function from main.py
from main import send_msg 

sched = BlockingScheduler()

# Schedule job_function to be called every 8 hours 
sched.add_job(send_msg, 'interval', hours=8)

sched.start()