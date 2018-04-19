import re

from plugins.APlugin import APlugin

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Users(APlugin):
    """This class enumerates the application users.
    """

    def __init__(self, request, logger, config):
        logger.handle("\n============ Users ============\n", None)

        super().__init__(config["thread"])
        self.logger = logger
        self.request = request

        self.range = config["range"]

    def run(self):
        for i in range(1, self.range):
            self.add(self._enum, i)
        self.wait()

    def _enum(self, id):
        """Enumerates users.
        """

        r = self.request.get("/user/" + str(id))
        username = self._checkRedirect(r.url)

        if username != "":
            self.logger.handle("[+] " + username + " (id=" + str(id) + ")", None)
        elif r.status_code == 403:
            self.logger.handle("[+] ***** (id=" + str(id) + ")", None)
        elif r.status_code == 200:
            tmp = str(r.content).split("\\n")
            for line in tmp:
                if re.search("<title>", line):
                    self.logger.handle("[+] " + line.split("|")[0].split(">")[1] + "(id=" + str(id) + ")", None)

    def _checkRedirect(self, url):
        """Check if the username is disclosed in the URL.

        Parameters
        ----------
        url : str
            url

        Return
        ------
        Disclosed name
        """

        if "users" in url:
            return url.split("users/")[1]
        return ""
