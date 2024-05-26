#!/usr/bin/python3
""" Log Parsing Module """

import sys
import signal


def print_stats(stats):
    """ Prints stats """
    for code, count in stats.items():
        if count > 0:
            print(f'{code}: {count}')


read_format = '<IP Address> - [<date>] \"GET /projects/260 HTTP/1.1\" <status code> <file size>'
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}

with sys.stdin as f:
    for line in f.readlines():
        if len(line.split(' ')) == 8:
            try:
                