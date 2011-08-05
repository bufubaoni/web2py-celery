from celery.app import default_app
from celery.utils import get_full_cls_name
from celery.result import AsyncResult
from celery.registry import tasks
from celery.utils.functional import wraps

# Ensure built-in tasks are loaded for task_list view                           
import celery.task
from tasks import *

task = TaskOne().delay()
print task

from time import sleep
sleep(5)
status = default_app.backend.get_status(task.task_id)
res = default_app.backend.get_result(task.task_id)
print status, res
