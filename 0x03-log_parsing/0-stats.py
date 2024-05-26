#!/usr/bin/python3
""" Log Parsing Module """

import sys
import signal


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

page_number = 0
total_size = 0


def print_stats():
    """ Prints stats """
    print(f'File size: {total_size}')
    for code, count in (status_codes.items()):
        if count > 0:
            print(f'{code}: {count}')


def handler(sig, total_size):
    """ Handles a SIGINT """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, handler)

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
                print_stats()
        except (IndexError, ValueError):
            continue
except KeyboardInterrupt:
    pass
finally:
    print_stats()
