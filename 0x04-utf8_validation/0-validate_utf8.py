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
        if bytes_tobe_checked == 0:
            if num & 128 == 0: # '0'
                bytes_tobe_checked = 0
            elif num & 224 == 192: # '110'
                bytes_tobe_checked = 1
            elif num & 240 == 224: # '1110'
                bytes_tobe_checked = 2
            elif num & 248 == 240: # '11110'
                bytes_tobe_checked = 3
            else:
                return False
        else:
            if num & 192 != 128: # '10'
                return False
            bytes_tobe_checked -= 1
    if bytes_tobe_checked == 0:
        return True

    return False
