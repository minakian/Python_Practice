# Run an external program, read the application's output
# convert the output to a string and then an int
import subprocess

def convertToNumber(val):
  try:
    number = int(val)
    return number
  except:
    return -1

cmd = ['./program']

#subprocess.run(cmd)

process = subprocess.Popen(cmd, stdout=subprocess.PIPE)

(output, err) = process.communicate()

output = output.decode("utf-8")

number = convertToNumber(output)

print(output)
print(number)
