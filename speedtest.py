#!/usr/bin/env python

import os
import subprocess
import argparse
import time


speedtest_result = os.popen('speedtest-cli --server 9928 --simple').read().split()

parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
parser.add_argument(dest='interface', nargs='?', default='wlp4s0',
                    help='wlan interface (default: wlp4s0)')
args = parser.parse_args()

cmd = subprocess.Popen('iwconfig %s' % args.interface, shell=True,
                   stdout=subprocess.PIPE)

for line in cmd.stdout:
    if 'Link Quality' in line:
        print line.lstrip(' '),
    elif 'Not-Associated' in line:
        print 'No signal'

print(speedtest_result)
