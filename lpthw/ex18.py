#This program is lesson 18 from "Learn Python 3 The Hard Way"
#this function is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1},arg2:{arg2}")

#*arg is pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1:{arg1},arg2:{arg2}")

#this just takes one argument
def print_one(arg1):
    print(f"arg1:{arg1}")

#this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Troy", "Kim")
print_two_again("Troy", "Kim")
print_one("Pepper")
print_none()
