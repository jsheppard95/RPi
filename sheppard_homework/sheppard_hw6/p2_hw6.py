#!/usr/bin/env python3
# P2) fork() and execv()
# p2_hw6.py
# Author: Jackson Sheppard
# 03Aug17 - Created

import os
import sys
os.execv(sys.argv[0], sys.argv)
