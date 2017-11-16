#This program is from lesson 4 in "Learning Python the Hard way".
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_not_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

'''
When I wrote this program the first time I had a mistake, and Python told me about it like this:
Traceback (most recent call last):
    File "ex4.py", line 9, in <module>
        average_passengers_per_car = car_pool_capacity / passenger
NameError: name 'car_pool_capacity' is not defined

Both 'car_pool_capacity' and 'passenger' are not consistent with their initialized variable names.
'car_pool_capacity' and 'passengers'.
'''
