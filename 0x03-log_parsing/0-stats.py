#!/usr/bin/python3
'''
Module: '0-stats'
'''

import sys

# intialize variables
line_count = 0
total_size = 0
stat_dict = {'200': 0, '301': 0, '400': 0, '401': 0,
             '403': 0, '404': 0, '405': 0, '500': 0}

try:
    for line in sys.stdin:
        line_count += 1
        data = line.split()
        try:
            file_size, status_code = int(data[-1]), data[-2]
            total_size += file_size
            if status_code in stat_dict:
                # increase the frequency of the key
                stat_dict[status_code] += 1
        except BaseException:
            pass
        # print after counting 10 lines
        if line_count % 10 == 0:
            # print_metrics(stat_dict, total_size)
            print(f'File size: {total_size:d}')
            for key, value in sorted(stat_dict.items()):
                if value > 0:
                    print(f'{key}: {value}')
    # print after finishing the lines from stdin
    # print_metrics(stat_dict, total_size)
    print(f'File size: {total_size:d}')
    for key, value in sorted(stat_dict.items()):
        if value > 0:
            print(f'{key}: {value}')

except KeyboardInterrupt:
    # print if 'ctrl + c'
    # print_metrics(stat_dict, total_size)
    print(f'File size: {total_size:d}')
    for key, value in sorted(stat_dict.items()):
        if value > 0:
            print(f'{key}: {value}')
    raise

'''
# printing function
def print_metrics(stat_dict, total_size):
    print(f'File size: {total_size:d}')
    for key, value in sorted(stat_dict.items()):
        if value > 0:
            print(f'{key}: {value}')
'''
