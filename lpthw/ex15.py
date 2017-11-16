#This program is lesson 15 from "Learn Python 3 The Hard Way"
from sys import argv
script, filename = argv

#Prints the name of the script based on input from argv
print(f"\nRunning the script: {script}")

#Assigns function 'open' with argument of 'filename' to variable 'txt'
txt = open(filename)
#Prints name of the file based on input from argv
print(f"\nHere's your file {filename}:")
#Prints the contents of 'filename'. txt.read() is the same as
#open(filename).read()
print(txt.read())

#Asks for the name of the file, 'filename'
print("Type the filename again:")
#Assigns the input 'filename' to variable 'file_again'
file_again = input(">")
#Assigns function 'open' with argument of 'file_again' to variable
# 'txt_again'
txt_again = open(file_again)
#Prints the contents of 'file_again'. txt_again.read() is the same as
#open(file_again).read()
print(txt_again.read())

#It's the same thing as above, but without assigning txt_again
print("Type the filename again:")
file_last = input(">")

print(open(file_last).read())
