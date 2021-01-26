# Description:
This Nagios Plugin calculates memory usage percent for a Linux machine.

# Usage:

`<python_interpreter_path> check_linux_mem.py {-w,--warn} <warning_treshold> {-c,--crit} <critical_treshold>`

# Example:
Check memory usage then warn if above 80% or alert if above 90% in a python3 interpreter environment:
  
`/usr/bin/python3 check_linux_mem.py -w 80 -c 90`
