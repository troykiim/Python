#This program is from lesson 5 in "Learning Python the Hard way".
name = 'Troy S. Kim'
age = 29
height = 71 #inches
weight = 193 #lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

height_centimeters = height * 2.54
weight_kilograms = weight * 0.453592

print(f"Let's talk about {name}.")
print(f"He's {height} inches or {round(height_centimeters)} centimeters tall.")
print(f"He's {weight} pounds or {round(weight_kilograms)} kilograms heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are unusually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
