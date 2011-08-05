from datetime import timedelta
from celery.task import Task, PeriodicTask
import time

class DemoTaskFast(Task):
    def run(self, **kwargs):
        t = 1
        print 'DemoTaskFast sleeping %i seconds' % t
        time.sleep(t)
        return True

class DemoTaskSlow(Task):
    def run(self, **kwargs):
        t = 30
        print 'DemoTaskSlow sleeping %i seconds' % t
        time.sleep(t)
        return True

class DemoTaskError(Task):
    def run(self, **kwargs):
        print 'DemoTaskError'
        1/0
        return True

class DemoTaskPeriodic(PeriodicTask):
    """
    A periodic task that concatenates fields to form a person's full name.
    """
    run_every = timedelta(seconds=60)

    def run(self, **kwargs):
        print 'DemoTaskPeriodic'
        return True
