from __future__ import print_function

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Logger:
    """This class allows displaying logs to the user as well as saving the tool output.
    """
    def __init__(self, status):
        self.fd = None
        if status:
            self.fd = open("/tmp/drupwn.txt", "w")

    def handle(self, out):
        """Handle the message to print.

        Parameters
        ----------
        out : str
            String to handle
        """

        print(out)
        if self.fd is not None:
            self.fd.write(out + "\n")

    def close(self):
        """Close the file descriptor.
        """

        if self.fd is not None:
            self.fd.close()
