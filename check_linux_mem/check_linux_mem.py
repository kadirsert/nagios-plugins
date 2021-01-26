from __future__ import print_function
import sys
import os
import argparse

__author__ = 'Kadir Sert'
__location__ = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--warn", help="Warning treshold for memory usage percent", type=int, default=80)
parser.add_argument("-c", "--crit", help="Alert treshold for memory usage percent", type=int, default=90)
args = parser.parse_args()

mem_info = os.popen("free -m |head -2 |tail -1").read().strip()
mem_list = mem_info.split()

mem_usage = int((float(mem_list[2]) / float(mem_list[1])) * 100)


if (mem_usage >= int(args.crit)):
    print("Memory Usage is in CRITICAL state: (", str(mem_usage), ")")
    sys.exit(2)
elif (mem_usage >= int(args.warn)):
    print("Memory Usage is in WARNING state: (", str(mem_usage), ")")
    sys.exit(1)
else:
    print("Memory Usage is OK: (", str(mem_usage), ")")
    sys.exit(0)
