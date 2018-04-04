import re

from plugins.APlugin import APlugin

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Fingerprinting(APlugin):
    """This class gather Drupal CMS version.
    """

    def __init__(self, request, logger, config):
        logger.handle("\n============ Fingerprinting ============\n")

        super().__init__(config["thread"])
        self.logger = logger
        self.request = request

    def run(self):

        if not self._getBootstrapVersion() and not self._getMetaVersion():
            self._getHeaderVersion()

    def _getHeaderVersion(self):
        """Get CMS version from returned header.

        Return
        ------
        Return True if the version is detected. False otherwise.
        """

        r = self.request.get()

        if r.status_code == 200 and r.headers["X-Generator"]:
            self.logger.handle("[+] Version: " + r.headers["X-Generator"])

            return True

        return False


    def _getBootstrapVersion(self):
        """Get CMS version from bootstrap include.

        Return
        ------
        Return True if the version is detected. False otherwise.
        """

        r = self.request.get("/includes/bootstrap.inc")

        if r.status_code == 200:
            tmp = str(r.content).split("\\n")
            for line in tmp:
                if re.search("VERSION", line):
                    if "define(" in line:
                        self.logger.handle("[+] Version: " + line.split("\\")[3] + "'\n")

                        return True

        return False

    def _getMetaVersion(self):
        """Get CMS version from the index page.

        Return
        ------
        Return True if the version is detected. False otherwise.
        """

        r = self.request.get()

        if r.status_code == 200:
            tmp = str(r.content).split("\\n")
            for line in tmp:
                if re.search("Generator", line):
                    tokens = line.split("\"")
                    for token in tokens:
                        if "Drupal" in token:
                            self.logger.handle("[+] Version: " + token + "\n")
                            self.logger.handle("The exact version can be found in several locations depending on the modules installed. CF: Modules enumeration")

                            return True

        return False
