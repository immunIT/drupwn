from plugins.APlugin import APlugin

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Nodes(APlugin):
    """This class enumerates Drupal application nodes.
    """

    def __init__(self, request, logger, config):
        logger.handle("\n============ Nodes ============\n", None)

        super().__init__(config["thread"])
        self.logger = logger
        self.request = request

        self.range = config["range"]

    def run(self):
        for i in range(0, self.range):
            self.add(self._enum, i)
        self.wait()

    def _enum(self, id):
        """Enumerates nodes.
        """

        r = self.request.get("/node/" + str(id))
        if r.status_code == 200:
            self.logger.handle(r.url, None)
