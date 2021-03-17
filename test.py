import sched
import time

event_schedule = sched.scheduler(time.time, time.sleep)


def do_something():
    print("Hello, World!")
    event_schedule.enter(3, 1, do_something)


do_something()
event_schedule.run()
