"""
Write a Python program to determine if a Python shell is executing on 32bit or 64bit mode on OS.
"""

import struct

print(struct.calcsize('P') * 8)
# 'P' represents a generic pointer.
# On 32-bit systems a pointer is 4 bytes and on 64-bit systems a pointer is 8 bytes.
# So, after multiplying it with 8 you can get know whether the system is 32-bit or 64bit.
