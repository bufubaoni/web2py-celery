from celery.app import default_app
from celery.utils import get_full_cls_name
from celery.registry import tasks
from celery.execute import send_task
from celery.result import AsyncResult

def submit_task(name,*args,**kwargs):
    """ submits a new task by name """
    result = send_task(name,*args,**kwargs)
    return {"ok": "true", "task_id": result.task_id}

def registered_tasks():
    """ returns registered tasks """
    return {"regular": tasks.regular().keys(),
            "periodic": tasks.periodic().keys()}

def task_status(task_id):
    """ returns task status and result """
    status = default_app.backend.get_status(task_id)
    res = default_app.backend.get_result(task_id)
    response_data = dict(id=task_id, status=status, result=res)
    if status in default_app.backend.EXCEPTION_STATES:
        traceback = default_app.backend.get_traceback(task_id)
        response_data.update({"result": repr(res),
                              "exc": get_full_cls_name(res.__class__),
                              "traceback": traceback})
    return {"task": response_data}

def main_test():
    import sys
    import time
    if len(sys.argv)<2 or sys.argv[1] in ('-h','--help','-help','help'):
        print """
Module to be imported from controller to perform basic actions
Can also be used interactively from shell
usage:
        %(name)s demo
        %(name)s registered_tasks
        %(name)s submit_task <name>
        %(name)s task_status <id>
        (for demo <name> is 'tasks.TaskOne' or 'tasks.TaskTwo')
        """ % dict(name=sys.argv[0])
    elif sys.argv[1]=='submit_task':
        task = submit_task('tasks.TaskOne')
        print task['task_id']
    elif sys.argv[1]=='task_status' and len(sys.argv)>2:
        status = task_status(sys.argv[2])
        print status
    elif sys.argv[1]=='registered_tasks':
        print registered_tasks() 
    elif sys.argv[1] == 'demo':
        print registered_tasks()
        task = submit_task('tasks.TaskOne')        
        from time import sleep
        while True:
            status = task_status(task['task_id'])    
            print status
            if status['task']['status']==u'SUCCESS': break
            sleep(1)
    else:
        print 'try: %s help' % sys.argv[0]

if __name__=='__main__':    
    main_test()
