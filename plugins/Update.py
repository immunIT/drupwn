import os
import sys
import requests
import socket
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from plugins.APlugin import APlugin



__author__ = "Simone La Porta <slaporta@immunit.ch>"
__copyright__ = "Copyright 2020, ImmunIT"


class Update(APlugin):
    """This class gather Drupal CMS version.
    """

    def __init__(self,logger, config):
        logger.handle("\n============ Update ============\n", None)
        super().__init__(config["thread"])
        self.logger = logger
        self.url = "https://git.drupalcode.org/groups/project/-/children.json"

    def run(self):
        with open("plugins/wordlists/plugins.txt", "w") as fd:
            session = requests.Session()
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            i = 1
            plugins_file = open("./plugins/wordlists/plugins.txt", "w")
            while True:
                paramsGet = {"page":""+str(i)+"","sort":"created_desc"}
                headers = {"User-Agent":"curl/7.64.1","Connection":"close","Accept":"*/*"}
                response = session.get("https://git.drupalcode.org/groups/project/-/children.json", params=paramsGet, headers=headers,verify=False)
                json_st = json.loads(response.content)
                if response.status_code == 200:
                    if len(json_st) == 0:
                        plugins_file.close()
                        break
                    for name in json_st:
                        print (name['name'])
                        fd.write(str(name['name']))
                        fd.write("\n")
                i +=1
