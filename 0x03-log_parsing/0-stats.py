#!/usr/bin/python3
'''
Module: '0-status'
'''

import sys

# intialize variables
line_count = 0
total_size = 0
codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
status = {k: 0 for k in codes}

try:
    for line in sys.stdin:
        line_count += 1
        data = line.split()
        try:
            file_size, status_code = int(data[-1]), data[-2]
            total_size += file_size
            if status_code in status:
                # increase the frequency of the key
                status[status_code] += 1
        except BaseException:
            pass

        if line_count % 10 == 0:
            print("File size: {:d}".format(total_size))
            for key, value in sorted(status.items()):
                if value:
                    print("{}: {}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(total_size))
    for key, value in sorted(status.items()):
        if value:
            print("{}: {}".format(key, value))
    raise
