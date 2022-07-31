import subprocess


command = ("lshw -C system").split(" ")
print(command)
complete = subprocess.run(command, capture_output=True)
ergebnis = str(complete.stdout)  # .split("\\n")
print(ergebnis)

