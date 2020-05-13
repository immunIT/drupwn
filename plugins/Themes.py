import os
import sys
import re

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
        self.exentions = [".info.yml", ".libraries.yml"]

    def run(self):
        with open("plugins/wordlists/themes.txt", "rU") as fd:
            for theme in fd:
                self.add(self._enum, theme)
            self.wait()
        self.detectCustom()

    def _enum(self, name):
        """Enumerates themes according to predefined application paths.
        """

        for path in self.paths:
            theme = name.replace("\n", "")
            if self.request.get(path + theme + "/logo.svg").status_code == 200:
                self.logger.handle("[+] " + theme, None)

    def detectCustom(self):
        self.logger.handle("\n============ Custom Themes ============\n", None)
        with self.request.get('/') as r:
            content = r.content
            cust_themes = list(set(result.lower() for result in re.findall(r'\/themes\/custom\/([^\/]*)', str(content), re.IGNORECASE)))
            buf = ""
            for cust_theme in cust_themes:
                buf +="/themes/custom/%s\n" %cust_theme
                for extension in self.exentions:
                    r = self.request.get('/themes/custom/%s/%s%s' %(cust_theme,cust_theme,extension))
                    if r.status_code == 200:
                        buf+='/themes/custom/%s/%s%s Found (200)\n' %(cust_theme,cust_theme,extension)
                    if r.status_code == 403:
                        buf+='/themes/custom/%s/%s%s Forbidden (403)\n' %(cust_theme,cust_theme,extension)
            if buf != "":
                self.logger.handle(buf, None)