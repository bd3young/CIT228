from restaurant import Restaurant
from icecream import IcecreamStand

restaurantOne = Restaurant('Slabtown', 'American')
restaurantTwo = Restaurant('China Wok', 'Chinese')
restaurantThree = Restaurant("Robby's", 'Mexican')

print('Exercise 9-1')
print('=================================================================')
print()
print('-----------------Here are your selections------------------')
print(f'Resturant = {restaurantOne.name}')
print(f'Cuisine = {restaurantOne.cuisineType}')
restaurantOne.describeResturant()
restaurantOne.restaurantOpen()
print()

print('Exercise 9-2')
print('=================================================================')
print()
restaurantOne.describeResturant()
restaurantTwo.describeResturant()
restaurantThree.describeResturant()

stand = IcecreamStand('Beaus Icecream', 'Icecream', 6, 'Strawberry', 'Vanilla', 'Chocolate', 'Superman', 'Moose Tracks')
stand.todaysFlavors()