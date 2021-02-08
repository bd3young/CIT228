class Restaurant:
    def __init__(self, name, cusineType):
        self.name = name
        self.cuisineType = cusineType 

    def describeResturant(self):
        print(f"{self.name} serves {self.cuisineType} cuisine.")

    def restaurantOpen(self):
        print(f"{self.name} is open.")

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