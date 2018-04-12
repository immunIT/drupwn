import math

from plugins.CVEs.ACVE import ACVE

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class CVE20187600(ACVE):
    """This class checks if the given target is vulnerable to the CVE-2018-7600.
    """

    def __init__(self, request, logger):
        logger.handle("\n[+] Checking CVE-2018-7600\n")

        self.logger = logger
        self.request = request

    def check(self, version):
        if self._checkDefault():
            return

        if math.floor(version) == 7:
            self._checkDrupal7()
        elif math.floor(version) == 8:
            self._checkDrupal8()

    def _checkDefault(self):
        """Check if the CVE tested is present in the CHANGELOG default file.
        Return True if yes. False otherwise.
        """

        dfile = self.request.get("/CHANGELOG.txt")

        if dfile.status_code == 200 and "SA-CORE-2018-002" in str(dfile.content):
            self.logger.handle("\tApplication not vulnerable\n")
            return True

        return False

    def _checkDrupal7(self):
        """Check Drupal 7.x.
        """

        req = self.request.get("/includes/request-sanitizers.inc").status_code
        ref = self.request.get("/includes/LetMeGetYourStatusCode.inc").status_code

        if req != 404 and req != ref:
            self.logger.handle("\tApplication not vulnerable")
        elif req == 403 and req == ref:
            self.logger.handle("\tCannot state if the Application is vulnerable")
        else:
            self.logger.handle("\tApplication vulnerable")

    def _checkDrupal8(self):
        """Check Drupal 8.x.
        """

        req = self.request.get("/core/lib/Drupal/Core/Security/RequestSanitizer.php").status_code
        ref = self.request.get("/core/lib/Drupal/Core/Security/LetMeGetYourStatusCode.php").status_code

        if req != 404 and req != ref:
            self.logger.handle("\tApplication not vulnerable")
        else:
            self.logger.handle("\tApplication vulnerable")
