# Description:
This Nagios Plugin calculates faulty Multipath DISK/LUN devices for a Linux machine.

# Usage:

`<python_interpreter_path> check_linux_multipath.py {-w,--warn} <warning_treshold> {-c,--crit} <critical_treshold> {-ln,--lun_name} <disk_alias_name>`

# Example:
Check paths for the "data1" disk then warn if faulty paths are above 1 or alert if above 2 in a python3 interpreter environment:
  
`/usr/bin/python3 check_linux_multipath.py -w 1 -c 2 -ln data1`
