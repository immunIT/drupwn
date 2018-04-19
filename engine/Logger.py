from __future__ import print_function

import tempfile

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Logger:
    """This class allows displaying logs to the user as well as saving the tool output.
    """

    def __init__(self, status):
        self.RED = '\033[91m'
        self.GREEN = '\033[92m'
        self.ENDC = '\033[0m'
        self.ERROR = 0
        self.SUCCESS = 1

        self.fd = None
        if status:
            self.fd = tempfile.NamedTemporaryFile(prefix="drupwn-", suffix=".txt", mode="w", dir='/tmp/', delete=False)
            print(self.GREEN + "\n[+] Logging file created => [" + self.fd.name + "]\n" + self.ENDC)

    def handle(self, out, code):
        """Handle the message to print.

        Parameters
        ----------
        out : str
            String to handle
        """

        if code == self.SUCCESS:
            print(self.GREEN + out + self.ENDC)
        elif code == self.ERROR:
            print(self.RED + out + self.ENDC)
        else:
            print(out)
        if self.fd is not None:
            self.fd.write(out + "\n")

    def close(self):
        """Close the file descriptor.
        """

        if self.fd is not None:
            self.fd.close()
