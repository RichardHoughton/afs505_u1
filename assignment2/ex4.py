cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
#cars not driven = number of cars - number of drivers
cars_not_driven = cars - drivers
#cars driven = number of drivers
cars_driven = drivers
#carpool capacity = number of cars driven times space in the car for people
carpool_capacity = cars_driven * space_in_a_car
#average passengers per car = passengers / number of cars driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

i = 10
j = 12
k = i + j
print("10 plus 12 is", k)
