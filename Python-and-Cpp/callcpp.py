# Run an external program, read the application's output
# convert the output to a string and then an int

import subprocess

cmd = ['./program', '3']

#subprocess.run(cmd)

process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
(output, err) = process.communicate()

number = int(output.decode("utf-8"))
print(output)
print(number + 2)