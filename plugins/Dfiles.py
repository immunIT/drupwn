from plugins.APlugin import APlugin

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Dfiles(APlugin):
    """This class enumerates default files present in the Drupal installation
    """

    def __init__(self, request, logger, config):
        logger.handle("\n============ Default files ============\n", None)

        super().__init__(config["thread"])
        self.logger = logger
        self.request = request

        self.files = ["README.txt", "LICENSE.txt", "web.config", "update.php", "robots.txt", "install.php", "xmlrpc.php"]

    def run(self):
        for f in self.files:
            self.add(self._enum, "/" + f)
        self.wait()

    def _enum(self, path):
        """Enumerate default files.
        """

        r = self.request.get(path)
        if r.status_code != 404:
            self.logger.handle("[+] " + path + " (" + str(r.status_code) + ")", None)
