import random
import requests
import time

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Request:
    """This class wraps the requests module in order to setup cookies, User-Agent, etc.
    """

    def  __init__(self, url, cookies, delay, userAgent, bauth, proxies):
        self.cookies = cookies
        self.delay = delay
        self.url = url
        self.proxies = proxies

        self.headers = {
            "User-Agent": userAgent,
            "Authorization": "Basic " + bauth,
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        self.session = requests.Session()

        requests.packages.urllib3.disable_warnings()

    def _updateHeaders(self, headers):
        if not headers:
            return self.headers
        else:
            tmp = dict(self.headers)
            tmp.update(headers)
            return tmp

    def get(self, path="", headers={}, data=""):
        """Perform GET request.

        Parameters
        ----------
        headers : dict
            Request headers
        path : str
            Request path

        Return
        ------
        Request response
        """

        if self.proxies is not None:
            i = random.randint(0, len(self.proxies) - 1)
            proxies = {
                "http": self.proxies[i],
                "https": self.proxies[i]
            }
        else:
            proxies=None

        time.sleep(self.delay)
        return self.session.get(self.url + path, headers=self._updateHeaders(headers), data=data, cookies=self.cookies, proxies=proxies, verify=False)

    def post(self, data, path=""):
        """Perform POST request.

        Parameters
        ----------
        path : str
            Request path

        Return
        ------
        Request response
        """

        time.sleep(self.delay)
        return self.session.post(self.url + path, data=data, headers=self.headers, cookies=self.cookies, verify=False)
