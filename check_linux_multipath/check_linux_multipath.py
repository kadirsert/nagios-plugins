from __future__ import print_function
import sys
import os
import argparse
import re

__author__ = 'Kadir Sert'
__location__ = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--warn", help="Warning treshold for faulty path count", type=int, default=1)
parser.add_argument("-c", "--crit", help="Alert treshold for faulty path count", type=int, default=2)
parser.add_argument("-ln", "--lun_name", help="LUN/DISK Name")
args = parser.parse_args()

multipath_info = os.popen("multipath -ll " + args.lun_name + " |grep -E '.*[0-9]+:[0-9]+:[0-9]+:[0-9]+\s+sd.*' |grep -Eo 'sd[a-z]{1,4}.*'").read().splitlines()
if not multipath_info:
    print("UNKNOWN - There is no multipath disk for LUN/DISK Name:", args.lun_name)
    sys.exit(3)

i = 0
for line in multipath_info:
    try:
        matchObj = re.match( r'^sd[a-z]{1,4}\s+[0-9]+:[0-9]+\s+([a-z,\s]+).*', line, re.S)
        path_state = matchObj.group(1).strip()
        if path_state != "active ready running":
            i += 1
    except Exception as e:
        print("UNKNOWN -", str(e))
        sys.exit(3)

if (i >= int(args.crit)):
    print("Faulty Path count for", args.lun_name, "is in CRITICAL state: (", str(i), ")")
    sys.exit(2)
elif (i >= int(args.warn)):
    print("Faulty Path count for", args.lun_name, "is in WARNING state: (", str(i), ")")
    sys.exit(1)
else:
    print("Multipath Check for", args.lun_name, "is OK")
    sys.exit(0)
