from datetime import timedelta
from celery.task import Task, PeriodicTask
import time

class TaskOne(Task):
    def run(self, **kwargs):
        time.sleep(kwargs.get('seconds',5))
        print 'TaskOne'
        return True

class TaskError(Task):
    def run(self, **kwargs):
        print 'TaskError'
        1/0
        return True

class TaskTwo(PeriodicTask):
    """
    A periodic task that concatenates fields to form a person's full name.
    """
    run_every = timedelta(seconds=60)

    def run(self, **kwargs):
        print 'TaskTwo'
        return True
