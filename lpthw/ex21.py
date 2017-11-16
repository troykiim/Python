#This program is lesson 21 from "Learn Python 3 The Hard Way"
def add(a, b):
    print(f"ADDING {a} + {b}")
    return(a + b)

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return(a - b)

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return(a * b)

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return(a / b)

print("Let's do some math with just functions!")

age = add(30, 5) #35
height = subtract(78, 4) #74
weight = multiply(90, 2) #180
iq = divide(100, 2) #50

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#Puzzle
print("Here is a puzzle.")

#what = add(int(age), int(subtract(int(height), int(multiply(int(weight), int(divide(int(iq), 2))))))) #-4391
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print(f"That becomes: {round(what)} Can you do that by hand?")
