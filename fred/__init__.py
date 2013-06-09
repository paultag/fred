#!/usr/bin/env python

from pymongo import Connection

connection = Connection('localhost', 27017)
db = connection.fred

__appname__ = "fred"
__version__ = "1.0"
