#!/usr/bin/env python3
"""
This module reads the standard input line by line and computes a metrics
"""

import sys


def print_stats(total_size, status_counts):
    """Print total size and the count of status codes"""

    print(f"File size: {total_size}")

    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")


total_size = 0
line_count = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0,
                 405: 0, 500: 0}

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 7:
                continue

            file_size = int(parts[-1])
            status_code = int(parts[-2])

            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

        except (ValueError, IndexError):
            continue

except KeyboardInterrupt:
    pass

print_stats(total_size, status_counts)
