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