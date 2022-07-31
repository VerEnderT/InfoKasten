#!/usr/bin/env python
import subprocess

command = ['sudo', 'python3', '/home/user/tools/main.py']
cmd1 = subprocess.Popen(['echo','user'], stdout=subprocess.PIPE)
cmd2 = subprocess.Popen(['sudo','-S'] + command, stdin=cmd1.stdout, stdout=subprocess.PIPE)
output = cmd2.stdout.read

cmd = "python3 /home/user/tools/menu.py".split(" ")
subprocess.Popen(cmd, shell=False)






