class Restaurant:
    def __init__(self, name, cusineType, numberServed = 0):
        self.name = name
        self.cuisineType = cusineType
        self.numberServed = numberServed

    def describeResturant(self):
        print(f"{self.name} serves {self.cuisineType} cuisine.")

    def restaurantOpen(self):
        print(f"{self.name} is open.")

    def setNumberServed(self, newNumberServed):
        self.numberServed = newNumberServed
    
    def incrementNumberServed(self, served):
        self.numberServed += served

class IcecreamStand(Restaurant):
    def __init__(self, name, cusineType, numberServed, *flavors):
        super().__init__(name, cusineType, numberServed)
        self.flavors = flavors
    
    def todaysFlavors(self):
        print('Todays Flavors are')
        print('-----------------------')
        for flavor in self.flavors:
            print(f'\t- {flavor}')

stand = IcecreamStand('Beaus Icecream', 'Icecream', 6, 'Strawberry', 'Vanilla', 'Chocolate', 'Superman', 'Moose Tracks')
stand.todaysFlavors()