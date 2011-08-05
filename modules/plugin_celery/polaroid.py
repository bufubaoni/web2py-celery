from pprint import pformat

from celery.events.snapshot import Polaroid

class Web2pyCamera(Polaroid):
    def shutter(self,state=None):
        if not state: state = self.state # for backward compatibility
        if not state or not state.event_count:
            # No new events since last snapshot.            
            print '...'
            return        
        print("Workers: %s" % (pformat(state.workers, indent=4), ))
        print("Tasks: %s" % (pformat(state.tasks, indent=4), ))
        print("Total: %s events, %s tasks" % (
            state.event_count, state.task_count))
