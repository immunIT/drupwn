import os
import sys

from plugins.APlugin import APlugin

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Themes(APlugin):
    """This class enumerates installed themes.
    """

    def __init__(self, request, logger, config):
        logger.handle("\n============ Themes ============\n", None)

        super().__init__(config["thread"])
        self.logger = logger
        self.request = request

        self.paths = ["/core/themes/"]

    def run(self):
        with open("plugins/wordlists/themes.txt", "rU") as fd:
            for theme in fd:
                self.add(self._enum, theme)
            self.wait()

    def _enum(self, name):
        """Enumerates themes according to predefined application paths.
        """

        for path in self.paths:
            theme = name.replace("\n", "")
            if self.request.get(path + theme + "/logo.svg").status_code == 200:
                self.logger.handle("[+] " + theme, None)
