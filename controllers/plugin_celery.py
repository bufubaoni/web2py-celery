from gluon.serializers import json
from plugin_celery import actions

def submit_task():
    name = request.args(0)
    args = request.vars
    response.headers['Content-Type'] = "application/json"
    return json(actions.submit_task(name,**args))

def registered_tasks():
    response.headers['Content-Type'] = "application/json"
    return json(actions.registered_tasks())

def task_status():
    """Returns task status and result in JSON format."""
    task_id = request.args(0)
    response.headers['Content-Type'] = "application/json"
    return json(actions.task_status(task_id))

