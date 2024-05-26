#!/usr/bin/python3
""" Log Parsing Module """

import sys
import signal


read_format = '<IP Address> - [<date>] \"GET /projects/260 HTTP/1.1\" <status code> <file size>'

with sys.stdin as f:
    f.readlines()
