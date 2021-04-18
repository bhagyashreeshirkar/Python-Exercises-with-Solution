"""
Write a Python program to get OS name, platform and release information.
"""

import os
import platform

print(os.name)  # nt == New Technology, 'nt' means that you are running windows system.
print(platform.uname())  # uname == unix name, it is used to get information about current operating system.
