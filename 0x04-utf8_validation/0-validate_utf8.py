#!/usr/bin/python3
""" Interview Prep """


def validUTF8(data):
    """
    method that determines if a given data set
    represents a valid UTF-8 encoding
    """
    # Number of bytes in the current UTF-8 character.
    n_bytes = 0

    # Masks check the most significant bits of each byte
    mask1 = 1 << 7
    mask2 = 1 << 6

    # Loop through each byte in the data
    for byte in data:
        # Get only the least significant 8 bits of the integer
        byte = byte & 0xFF

        if n_bytes == 0:
            # Determine the number of bytes in the current UTF-8 character
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask = mask >> 1

            # 1-byte characters (ASCII) or no leading 1s (invalid scenarios)
            if n_bytes == 0:
                continue

            # UTF-8 character must be between 2 and 4 bytes
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check that the byte starts with 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes remaining in the current UTF-8
        # char
        n_bytes -= 1

    # If n_bytes is not zero, then we have incomplete UTF-8 characters
    return n_bytes == 0
