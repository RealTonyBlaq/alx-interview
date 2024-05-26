#!/usr/bin/python3
""" Log Parsing Module """

import sys
import signal


def print_stats(stats, total_size):
    """ Prints stats """
    print(f'File size: {total_size}')
    for code, count in (stats.items()):
        if count > 0:
            print(f'{code}: {count}')


def handler(stats, total_size):
    """ Handles a SIGINT """
    print_stats(stats, total_size)
    sys.exit(0)


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

signal.signal(signal.SIGINT, handler)

page_number = 0
total_size = 0
try:
    for line in sys.stdin:
        page_number += 1
        new_line = line.split()

        try:
            code = new_line[-2]
            size = new_line[-1]
            total_size += int(size)
            if code in status_codes:
                status_codes[code] += 1
            if page_number % 10 == 0:
                print_stats(status_codes, total_size)
        except (IndexError, ValueError):
            continue
except KeyboardInterrupt:
    pass
finally:
    print_stats(status_codes, total_size)
