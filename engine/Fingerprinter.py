import re

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Fingerprinter():
    """This class gather Drupal CMS version.
    """

    def __init__(self, request, logger):
        self.request = request
        self.logger = logger

    def fingerprint(self, config):
        if config["version"] is None:
            self.logger.handle("[-] Version not specified, trying to identify it", self.logger.ERROR)

            config["version"] = self._getDefaultFilesVersion()
            config["version"] = self._getMetaVersion() if config["version"] is None else config["version"]
            config["version"] = self._getHeaderVersion() if config["version"] is None else config["version"]

            if config["version"]:
                if re.match(r'[+-]?([0-9]*[.])?[0-9]+', config["version"]):
                    version = re.search(r'[+-]?([0-9]*[.])?[0-9]+', config["version"])
                    config["version"] = float(version.group(0))
                else:
                    config["version"] = '8.x'

    def _getHeaderVersion(self):
        """Get CMS version from returned header.

        Return
        ------
        Return True if the version is detected. False otherwise.
        """

        r = self.request.get()

        try:
            if r.status_code == 200 and r.headers["X-Generator"]:
                return r.headers["X-Generator"]
        except:
            pass

        return None


    def _getDefaultFilesVersion(self):
        """Get CMS version from bootstrap include.

        Return
        ------
        Return True if the version is detected. False otherwise.
        """

        dfiles = {"/CHANGELOG.txt", "/core/CHANGELOG.txt", "/includes/bootstrap.inc", "/core/includes/bootstrap.inc"}

        for dfile in dfiles:

            r = self.request.get(dfile)

            if r.status_code == 200:
                content = str(r.content.decode("utf-8"))
                lines = content.split("\n")
                for line in lines:
                    if "Drupal " in line:
                        match = re.search('Drupal (.*),', line)
                        if match:
                            return match.group(1)

        return None

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
                            return token

        return None
