#!/usr/bin/python3
'''
Module: '0-stats'
'''

import sys
import re

# intialize variables
count_line = 0
total_size = 0
freq_of_status_code = {200: 0, 301: 0, 400: 0,
                       401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'

try:
    for line in sys.stdin:
        match = re.match(line_pattern, line)
        if match:
            ip_address, date, status_code, file_size = match.groups()
            count_line += 1
            total_size += int(file_size)
            if int(status_code) in freq_of_status_code:
                # increase the frequency of the key
                freq_of_status_code[int(status_code)] += 1

        if count_line == 10:
            print(f'File size: {total_size}')
            for key in sorted(freq_of_status_code.keys()):
                if freq_of_status_code[key] > 0:
                    print(f'{key}: {int(freq_of_status_code[key])}')
            # reset the variables back to their intial value
            count_line = 0
            total_size = 0
            freq_of_status_code = {200: 0, 301: 0, 400: 0,
                                   401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
except KeyboardInterrupt:
    print(f'File size: {total_size}')
    for key in sorted(freq_of_status_code.keys()):
        if freq_of_status_code[key] > 0:
            print(f'{key}: {int(freq_of_status_code[key])}')
