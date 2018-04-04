from abc import ABC, abstractmethod

from engine.ThreadPool import ThreadPool

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class APlugin(ABC):
    """Plugin abstract class implementing threads.
    """

    def __init__(self, nb):
        self.tasks = []
        if nb is None:
            self.pool = ThreadPool(1)
        else:
            self.pool = ThreadPool(nb)

    def add(self, func, args):
        """Add job.

        Parameters
        ----------
        func : object
            Function to call
        args : object
            Function arguments
        """

        self.pool.add(func, args)

    def add_list(self, func, args):
        """Add jobs to list.

        Parameters
        ----------
        func : object
            Function to call
        args : object
            Function arguments
        """

        self.tasks.append(args)

        if len(self.tasks) > 50:
            self.pool.map(func, self.tasks)
            self.tasks = []

    def wait(self):
        """Wait for threads to finish
        """

        self.pool.wait()

    @abstractmethod
    def run(self):
        """Plugin entrypoint.
        """

        pass
