#!/usr/bin/python3
'''
Module: '0-stats'
'''

import sys


# intialize variables
line_count = 0
total_size = 0
freq_of_status_code = {200: 0, 301: 0, 400: 0,
                       401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        data = line.split()
        if len(data) >= 3:
            status_code, file_size = int(data[-2]), int(data[-1])
        line_count += 1
        total_size += int(file_size)
        if int(status_code) in freq_of_status_code:
            # increase the frequency of the key
            freq_of_status_code[int(status_code)] += 1

        if line_count == 10:
            print(f'File size: {total_size:d}')
            for key in sorted(freq_of_status_code.keys()):
                if freq_of_status_code[key] > 0:
                    print(f'{key}: {int(freq_of_status_code[key])}')
            # reset the variables back to their intial value
            line_count = 0
            total_size = 0
            freq_of_status_code = {200: 0, 301: 0, 400: 0,
                                   401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
except KeyboardInterrupt:
    print(f'File size: {total_size}')
    for key in sorted(freq_of_status_code.keys()):
        if freq_of_status_code[key] > 0:
            print(f'{key}: {int(freq_of_status_code[key])}')
