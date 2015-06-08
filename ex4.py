#This is a variable, = gives a name to an object
cars = 100
drivers = 30
cars_available = 100
empty_cars = cars - drivers
persons_per_car = 4.0
passengers = 90
carpool_capacity = drivers * persons_per_car
average_person_per_car = passengers / drivers

print "There are", cars, "cars avalaible."
print "Thre are only", drivers, "drivers available."
print "There will be", empty_cars, "empty cars today."
print "we can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_person_per_car, "persons in each car."
print cars * drivers
print "I %s am"
