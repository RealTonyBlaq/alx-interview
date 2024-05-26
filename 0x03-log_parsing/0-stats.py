#!/usr/bin/python3
""" Log Parsing Module """

import sys
import signal


read_format = '<IP Address> - [<date>] \"GET /projects/260 HTTP/1.1\" <status code> <file size>'
status_codes = {200, 301, 400, 401, 403, 404, 405, 500}

with sys.stdin as f:
    for line in f.readlines():
        if 
