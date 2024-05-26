#!/usr/bin/python3
""" Log Parsing Module """

import sys


def print_stats(stats, total_size):
    """ Prints stats """
    print(f'File size: {total_size}')
    for code, count in (stats.items()):
        if count > 0:
            print(f'{code}: {count}')


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

try:
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        page_number += 1
        new_line = line.split()
        
        try:
            code = new_line[-2]
            size = new_line[-1]
            total_size += int(size)
            if code in status_codes:
                status_codes[code] += 1
        except (IndexError, ValueError):
            # Handle lines that don't have enough elements or invalid integers
            continue
        
        if page_number % 10 == 0:
            print_stats(status_codes, total_size)
except KeyboardInterrupt:
    print_stats(status_codes, total_size)
