#!/usr/bin/python3
'''
Module: '0-validate_utf8'
Checks if a list of integers are a valid utf8 format
'''


def validUTF8(data):
    '''
    Returns True/False indicating a valid utf format or not
    '''
    bytes_tobe_checked = 0

    for num in data:
        if type(num) != int or num < 0 or num > 1114111:
            return False
        bin_num = bin(num)[2:].zfill(8)
        if bytes_tobe_checked == 0:
            if bin_num[0] == '0':
                bytes_tobe_checked = 0
            elif bin_num[:3] == '110':
                bytes_tobe_checked = 1
            elif bin_num[:4] == '1110':
                bytes_tobe_checked = 2
            elif bin_num[:5] == '11110':
                bytes_tobe_checked = 3
            else:
                return False
        else:
            if bin_num[:2] != '10':
                return False
            bytes_tobe_checked -= 1

    return bytes_tobe_checked == 0
