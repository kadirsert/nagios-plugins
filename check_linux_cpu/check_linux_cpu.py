from __future__ import print_function
import sys
import os
import argparse

__author__ = 'Kadir Sert'
__location__ = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--warn", help="Warning treshold for cpu usage percent", type=int, default=80)
parser.add_argument("-c", "--crit", help="Alert treshold for cpu usage percent", type=int, default=90)
args = parser.parse_args()

vmstat_line = os.popen("/usr/bin/vmstat 1 2 |tail -1 |xargs |egrep -v '[a-z,A-Z]|-' |egrep '[0-9]'").read()

cpu_idle =int(vmstat_line.split()[14])
cpu_usage = 100 - cpu_idle

if (cpu_usage >= int(args.crit)):
    print ("CPU Usage is in CRITICAL state: (", str(cpu_usage),  ")")
    sys.exit(2)
elif (cpu_usage >= int(args.warn)):
    print ("CPU Usage is in WARNING state: (", str(cpu_usage),  ")")
    sys.exit(1)
else:
    print("CPU Usage is OK: (", str(cpu_usage), ")")
    sys.exit(0)
