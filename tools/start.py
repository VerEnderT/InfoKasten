
import subprocess
import os


cmd = "pkill -9 -f cheese"
os.system(cmd)
cmd = "pkill -9 -f soundtest"
os.system(cmd)
cmd = "pkill -9 -f ffplay"
os.system(cmd)
cmd = "pkill -9 -f rectest.py"
os.system(cmd)
cmd = "pkill -9 -f mictest.py"
os.system(cmd)
cmd = "pkill -9 -f main.py"
os.system(cmd)
cmd = "pkill -9 -f menu.py"
os.system(cmd)
cmd = "pkill -9 -f tastaturtest.py"
os.system(cmd)

cmd = ['python3', '/home/user/tools/main.py']
subprocess.Popen(cmd, shell=False)

cmd = "python3 /home/user/tools/menu.py".split(" ")
subprocess.Popen(cmd, shell=False)


cmd ='amixer -c 1 set Capture 40db'
os.system(cmd)

cmd ='pactl -- set-sink-volume 0 85%'
os.system(cmd)




