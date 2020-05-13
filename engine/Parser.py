import argparse

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Parser:
    """This class parses the tool arguments
    """

    def __init__(self):
        self.config = {}

    def parse(self):
        """Parse Drupwn arguments.

        Return
        ------
        Configuration dictionnary
        """

        parser = argparse.ArgumentParser(description="""\
            Drupwn aims to automate drupal information gathering.
        """)

        parser.add_argument('--mode', type=str, help='enum|exploit',required=False)
        parser.add_argument('--target', type=str, help='hostname to scan',required=False)
        parser.add_argument("--users", help="user enumaration", action="store_true")
        parser.add_argument("--nodes", help="node enumeration", action="store_true")
        parser.add_argument("--modules", help="module enumeration", action="store_true")
        parser.add_argument("--dfiles", help="default files enumeration", action="store_true")
        parser.add_argument("--themes", help="theme enumeration", action="store_true")
        parser.add_argument("--version", type=float, help="Drupal version")
        parser.add_argument("--cookies", type=str, help="cookies")
        parser.add_argument("--thread", type=int, default=20, help="threads number")
        parser.add_argument("--range", type=int, help="enumeration range")
        parser.add_argument("--ua", type=str, help="User Agent")
        parser.add_argument("--bauth", type=str, help="Basic authentication")
        parser.add_argument("--delay", type=float, help="request delay")
        parser.add_argument("--log", help="file logging", action="store_true")
        parser.add_argument("--update", help="update plugins and themes", action="store_true")

        group = parser.add_mutually_exclusive_group(required=False)
        group.add_argument("--proxy", type=str, help="[http|https|socks]://host:port")
        group.add_argument("--proxies", type=str, help="Proxies file")
        

        self._loadConfig(parser.parse_args())
        if not(self.config['update']) and not(self.config['mode'] or self.config['target']):
            parser.error('the following arguments are required: --mode, --target')
        self._sanitizeConfig()

        return self.config

    def _loadConfig(self, args):
        """Load configuration from parsed arguments.

        Parameters
        ----------
        args : object
            Drupwn parsed arguments

        Return
        ------
        Configuration dictionnary
        """

        self.config = {
            "target": args.target,
            "mode": args.mode,
            "users": args.users,
            "nodes": args.nodes,
            "modules": args.modules,
            "dfiles": args.dfiles,
            "themes": args.themes,
            "version": args.version,
            "cookies": args.cookies,
            "thread": args.thread,
            "range": args.range,
            "userAgent": args.ua,
            "bauth": args.bauth,
            "delay": args.delay,
            "log": args.log,
            "proxy": args.proxy,
            "proxies": args.proxies,
            "update": args.update
        }

    def _sanitizeConfig(self):
        """Sanitize configuration.
        """

        self.config["range"] = self._setRange(self.config["range"])
        self.config["cookies"] = self._setCookies(self.config["cookies"])
        self.config["userAgent"] = self._setUserAgent(self.config["userAgent"])
        self.config["bauth"] = self._setBAuth(self.config["bauth"])
        self.config["delay"] = self._setDelay(self.config["delay"])

        self.config["proxy"] = self._setProxies(None, self.config["proxy"]) if self.config["proxy"] is not None else None
        self.config["proxies"] = self._setProxies(self.config["proxies"], None) if self.config["proxies"] is not None else None

    def _setProxies(self, proxies, proxy):
        """Set proxies.

        Parameters
        ----------
        proxies : str
            Proxies values
        proxy : str
            Proxy value

        Return
        ------
        Proxies array
        """

        p_list = []
        if proxy is not None:
            p_list.append(proxy)
        elif proxies is not None:
            with open(proxies, "rU") as fd:
                for line in fd:
                    p_list.append(line.replace("\n", ""))

        return p_list

    def _setRange(self, eRange):
        """Set enumeration range.

        Parameters
        ----------
        eRange : int
            Enumeration range

        Return
        ------
        Enumeration range
        """

        if eRange is not None:
            return eRange
        else:
            return 1000

    def _setUserAgent(self, userAgent):
        """Set User-Agent.

        Parameters
        ----------
        userAgent : str
            User-Agent string

        Return
        ------
        User-Agent string
        """

        if userAgent is not None:
            return userAgent
        else:
            return ""

    def _setBAuth(self, bauth):
        """Set basic authentication.

        Parameters
        ----------
        bauth : str
            Basic authentication string

        Return
        ------
        Basic authentication string
        """

        if bauth is not None:
            return bauth
        else:
            return ""

    def _setCookies(self, cookies):
        """Set user cookies.

        Parameters
        ----------
        cookies : str
            User cookies string

        Return
        ------
        Formated cookies string
        """

        if cookies is not None:
            cArray = cookies.split(';')
            return dict((name.strip(), value.strip()) for name, value in (cookie.split('=') for cookie in cArray))
        else:
            return ""

    def _setDelay(self, delay):
        """Set request delay.

        Parameters
        ----------
        delay : float
            Delay

        Return
        ------
        Delay
        """

        if delay is None:
            return 0
        else:
            return delay
