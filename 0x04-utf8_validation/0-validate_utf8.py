#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    num_bytes = 0
    for num in data:
        if num_bytes == 0:
            # Check the number of leading set bits
            if (num >> 7) == 0b0:
                continue
            set_bits = 0
            helper = 1 << 7
            while helper & num:
                set_bits += 1
                helper = helper >> 1

            # Validate the number of bytes based on leading set bits
            if set_bits == 1 or set_bits > 4:
                return False

            num_bytes = set_bits - 1  # Set the remaining bytes to check
        else:
            # Check if the current byte has the format 10xxxxxx
            if not (num & (1 << 7) and not (num & (1 << 6))):
                return False
            num_bytes -= 1

    return num_bytes == 0
