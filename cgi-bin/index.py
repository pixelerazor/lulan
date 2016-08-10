#!/usr/bin/python3
import cgi
import os
import re
from printOperations import *

indent = printHeader()
_ = printNav(indent)
args = cgi.FieldStorage()
_ = printSite(indent, args)
printFooter()
