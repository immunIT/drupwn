import importlib

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Dispatcher():
    """This class instantiates and executes selected plugins passed as paramaters to Drupwn.
    """

    def __init__(self, request, logger):
        self.logger = logger
        self.request = request

        self.plugins = {"users", "nodes", "modules", "dfiles", "themes"}

    def dispatch(self, config):
        """Instantiate and run selected plugins.

        Parameters
        ----------
        config : dict
            Drupwn parameters
        """

        dispatched = False
        for plugin in self.plugins:
            if config[plugin]:
                try:
                    self._factory(str.capitalize(plugin))(self.request, self.logger, config).run()
                except:
                    pass
                dispatched = True

        if not dispatched:
            for plugin in self.plugins:
                try:
                    self._factory(str.capitalize(plugin))(self.request, self.logger, config).run()
                except:
                    pass

    def _factory(self, name):
        """Dynamicaly import plugins.

        Parameters
        ----------
        name : str
            Plugin name's

        Return
        ------
        Plugin instance's
        """

        return getattr(importlib.import_module("plugins." + name), name)
