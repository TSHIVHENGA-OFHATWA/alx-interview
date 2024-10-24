#!/usr/bin/env python3
"""
This module reads the standard input line by line and computes a metrics
"""

import sys


def display_stats(total_size, status_counts):
    """Print total size and the count of status codes
     Args:
        status_count: Dictionary to store the count of HTTP status codes.
        total_size: Total size of all files processed.

    Returns:
        None
    """
    print("File size: {}".format(accumulated_size))
    for code, count in sorted(status_code_count.items()):
        if count != 0:
            print("{}: {}".format(code, count))


accumulated_size = 0
current_code = 0
line_counter = 0
status_code_count = {"200": 0, "301": 0, "400": 0, "401": 0,
                     "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for log_entry in sys.stdin:
        reversed_entry = log_entry.split()
        reversed_entry = reversed_entry[::-1]

        if len(reversed_entry) > 2:
            line_counter += 1

            if line_counter <= 10:
                accumulated_size += int(reversed_entry[0])
                current_code = reversed_entry[1]

                if current_code in status_code_count.keys():
                    status_code_count[current_code] += 1

            if line_counter == 10:
                display_stats(status_code_count, accumulated_size)
                line_counter = 0

finally:
    display_stats(status_code_count, accumulated_size)
