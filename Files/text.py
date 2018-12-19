# Program to convert .cycacd file into a 
# useable format for Particle bootloading

import os
import sys

length = len(sys.argv)

if(length == 1):
  print("Need file name.")
  quit()
if(length == 3):
  num = 3
if os.path.exists("new_file.txt"):
  os.remove("new_file.txt")

if not os.path.exists(sys.argv[1]):
  print("Not a valid file path")
  quit()
f = open(sys.argv[1], 'r')

new_file = open("new_file.txt", 'w')
#message = f.readline()   # Read the file one line at a time
message = f.readlines()  # Read the entire file, result broken up by line
for line in message:
  i = 0
  if line[0] == ':':
    i = 1
  length = len(line)
  new_line = "{"
  while(i < length):
    if(line[i] == '\n'):
      break
    else:
      if(i <= 1):
        new_line += "0x" + line[i:i+2]
      else:
        new_line += ",0x" + line[i:i+2]
    i += 2
  new_line += "},\n"
  print(new_line)
  new_file.write(new_line)
new_file.close()

#print(message[1][-2])

f.close()