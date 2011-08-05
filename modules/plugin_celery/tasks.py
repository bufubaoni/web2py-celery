from datetime import timedelta
from celery.task import Task, PeriodicTask
import time
# from app.models import mytable ???

class TaskOne(Task):
    def run(self, **kwargs):
        time.sleep(5)
        print 'TaskOne'
        return True

class TaskTwo(PeriodicTask):
    """
    A periodic task that concatenates fields to form a person's full name.
    """
    run_every = timedelta(seconds=60)

    def run(self, **kwargs):
        print 'TaskTwo'
        return True
