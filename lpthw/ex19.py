#This program is lesson 19 from "Learn Python 3 The Hard Way"
#Define the function 'cheese_and_crackers' with arguments: 'cheese_count' and 'boxes_of_crackers'
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"\t* You have {cheese_count} cheeses!")
    print(f"\t* You have {boxes_of_crackers} boxes of crackers!")
    print(f"\t* Man thats enough for a party!")
    print("\t* Get a blanket.\n")

#We can pass numbers as arguments
print("We can just give the functions numbers directly:")
cheese_and_crackers(20, 30)

#We can assign values to our variables and then call the function with the arguments we defined
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Like example 2, we can do math to pass the arguments
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#Adds a number to the arguments to increase the variables
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
