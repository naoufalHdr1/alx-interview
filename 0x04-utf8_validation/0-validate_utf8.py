#!/usr/bin/python3
"""
0-validate_utf8.py
Function to check if a list of integers is valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000 in binary
    mask2 = 1 << 6  # 01000000 in binary

    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Count the number of leading 1 bits to determine the byte length
            while byte & mask:
                num_bytes += 1
                mask >>= 1
            # If no leading 1s, it is a 1-byte character (0xxxxxxx)
            if num_bytes == 0:
                continue
            # UTF-8 characters should be between 2 and 4 bytes
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # For subsequent bytes, check that they match 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
