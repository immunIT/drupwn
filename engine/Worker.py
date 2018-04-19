from threading import Thread

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Worker(Thread):
    """This class represents worker that will handle tasks.
    """

    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        """Run jobs.
        """

        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except:
                pass
            finally:
                self.tasks.task_done()
