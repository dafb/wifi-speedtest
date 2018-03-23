#!/usr/bin/env python
import os

while True:
   speedtest_result = os.popen('speedtest-cli --server 9928 --simple').read().split()

print(speedtest_result)
