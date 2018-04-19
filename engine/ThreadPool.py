from queue import Queue

from engine.Worker import Worker

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class ThreadPool:
    """This class is used as threading pool to add and execute jobs.
    """

    def __init__(self, nb):
        self.tasks = Queue(nb)
        for _ in range(nb):
            Worker(self.tasks)

    def add(self, func, *args, **kargs):
        """Add job in the threading pool.

        Parameters
        ----------
        func : object
            Function to execute
        *args, **kargs : array
            Function parameters
        """

        self.tasks.put((func, args, kargs))

    def map(self, func, args_list):
        """Add jobs in the threading pool.

        Parameters
        ----------
        func : object
            Function to execute
        args_list : list
            Function parameters list
        """

        for args in args_list:
            self.add(func, args)

    def wait(self):
        """Wait for threads to finish.
        """

        self.tasks.join()
