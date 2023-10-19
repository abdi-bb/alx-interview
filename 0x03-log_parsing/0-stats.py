#!/usr/bin/python3
'''
Module: '0-freq_of_status_code'
'''

import sys

# intialize variables
line_count = 0
total_size = 0
freq_of_status_code = {'200': 0, '301': 0, '400': 0,
                       '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

try:
    for line in sys.stdin:
        line_count += 1
        data = line.split()
        try:
            file_size, status_code = int(data[-1]), data[-2]
            total_size += file_size
            if status_code in freq_of_status_code:
                # increase the frequency of the key
                freq_of_status_code[status_code] += 1
        except BaseException:
            pass

        if line_count % 10 == 0:
            print("File size: {:d}".format(total_size))
            for key, value in sorted(freq_of_status_code.items()):
                if value:
                    print("{}: {}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(total_size))
    for key, value in sorted(freq_of_status_code.items()):
        if value:
            print("{}: {}".format(key, value))
    raise
