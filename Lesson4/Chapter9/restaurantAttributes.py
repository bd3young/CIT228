class Restaurant:
    def __init__(self, name, cusineType, numberServed):
        self.name = name
        self.cuisineType = cusineType
        self.numberServed = 0

    def describeResturant(self):
        print(f"{self.name} serves {self.cuisineType} cuisine.")

    def restaurantOpen(self):
        print(f"{self.name} is open.")

    def setNumberServed(self, newNumberServed):
        self.numberServed = newNumberServed
    
    def incrementNumberServed(self, served):
        self.numberServed += served



restaurant = Restaurant('Slabtown', 'American', 6)
print('Exercise 9-4')
print('=================================================================')
print()
print('# processing initial number served #')
print(f'The starting number of customers was: {restaurant.numberServed}')
print()
print('# changing the number served #')
restaurant.numberServed = 10
print(f'The starting number of customers was: {restaurant.numberServed}')
print()
print('# changing the number served using the set number served method #')
restaurant.setNumberServed(40)
print(f'how many total cutomers have been served today? {restaurant.numberServed}')
print(f'The number of customers served is currently {restaurant.numberServed}')
print()
print('# addint to the number_served using the increment_number_served method  #')
print(f'How many additional customers have been served? 45')
print()
print('# printing the grand total for the day  #')
restaurant.incrementNumberServed(45)
print(f'The number of customers served this business day = {restaurant.numberServed}')
print()