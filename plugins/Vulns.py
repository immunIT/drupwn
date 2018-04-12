import importlib

from os import walk

from plugins.APlugin import APlugin

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Vulns(APlugin):
    """This class enumerates the application users.
    """

    def __init__(self, request, logger, config):
        logger.handle("\n============ CVE checker ============\n")

        super().__init__(config["thread"])
        self.logger = logger
        self.request = request
        self.version = config["version"]

    def run(self):
        cves = []
        for (dirpath, dirnames, filenames) in walk("./plugins/CVEs"):
            cves.extend(filenames)
            break

        for cve in cves:
            if cve != "__init__.py" and cve != "ACVE.py":
                cve = cve.replace(".py", "")
                self.add(getattr(importlib.import_module("plugins.CVEs." + cve), cve)(self.request, self.logger).check, self.version)
        self.wait()
