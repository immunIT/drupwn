#!/usr/env python

from __future__ import print_function

from engine.Dispatcher import Dispatcher
from engine.Logger import Logger
from engine.Parser import Parser
from engine.Request import Request

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


def welcome():
    print("""
        ____
       / __ \_______  ______ _      ______
      / / / / ___/ / / / __ \ | /| / / __ \\
     / /_/ / /  / /_/ / /_/ / |/ |/ / / / /
    /_____/_/   \__,_/ .___/|__/|__/_/ /_/
                     /_/
    """)

if __name__ == "__main__":
    welcome()

    config = Parser().parse()
    logger = Logger(config["log"])
    request = Request(config["target"], config["cookies"], config["delay"], config["userAgent"], config["bauth"])

    Dispatcher(request, logger).dispatch(config)

    logger.close()
