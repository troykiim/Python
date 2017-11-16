#This program is lesson 14 from "Learn Python 3 The Hard Way".
from sys import argv

script, user_name = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"\nDo you like me {user_name}?")
likes = input(prompt)

print(f"\nWhere do you live {user_name}?")
lives = input(prompt)

print("\nWhat kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice
""")
