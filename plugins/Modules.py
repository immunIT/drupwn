import os
import re
import sys

from plugins.APlugin import APlugin

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Modules(APlugin):
    """This class enumerates installed modules.
    """

    def __init__(self, request, logger, config):
        logger.handle("\n============ Modules ============\n", None)

        super().__init__(config["thread"])
        self.logger = logger
        self.request = request

        self.paths = ["/sites/all/modules/contrib/", "/sites/default/modules/"]
        self.files = ["README.txt", "LICENSE.txt", "CHANGELOG.txt"]

    def run(self):
        with open("plugins/wordlists/plugins.txt", "rU") as fd:
            for plugin in fd:
                self.add(self._enum, plugin)
            self.wait()

    def _enum(self, name):
        """Enumerates modules according to predefined application paths as well as files.

        Parameters
        ----------
        name : str
            Plugin name's
        """

        buf = ""
        for path in self.paths:
            s_plugin = name.replace("\n", "")
            if self.request.get(path + s_plugin + '/' + s_plugin + ".module").status_code != 404:
                buf += "[+] " + s_plugin + "\n"
                r = self.request.get(path + s_plugin + '/' + s_plugin + ".info")
                if r.status_code == 200:
                    buf += self._getVersion(r.content)
                for f in self.files:
                    if self.request.get(path + s_plugin + '/' + f).status_code == 200:
                        buf += "\t- " + f + "\n"
        if buf != "":
            self.logger.handle(buf, None)

    def _getVersion(self, content):
        """Retrieve the module version.

        Parameters
        ----------
        content : str
            Request content

        Return
        ------
        Plugin version
        """

        tmp = str(content).split("\\n")
        for line in tmp:
            if re.search("version = \"", line):
                return "\t" + line + "\n\n"
