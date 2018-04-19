import requests
import time

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Request:
    """This class wraps the requests module in order to setup cookies, User-Agent, etc.
    """

    def  __init__(self, url, cookies, delay, userAgent, bauth):
        self.cookies = cookies
        self.delay = delay
        self.url = url

        self.headers = {
            "User-Agent": userAgent,
            "Authorization": "Basic " + bauth,
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        self.session = requests.Session()

        requests.packages.urllib3.disable_warnings()

    def get(self, path=""):
        """Perform GET request.

        Parameters
        ----------
        path : str
            Request path

        Return
        ------
        Request response
        """

        time.sleep(self.delay)
        return self.session.get(self.url + path, headers=self.headers, cookies=self.cookies, verify=False)

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
