#This program is lesson 17 from "Learn Python 3 The Hard Way"
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying files from {from_file} to {to_file}")

# We could do these two on one line by doing : indata = open(from_file).read()
in_file = open(from_file)
indata = in_file.read()

#Removed to make script more user friendly
#print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}.")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
