class Restaurant:
    def __init__(self, name, cusineType):
        self.name = name
        self.cuisineType = cusineType 

    def describeResturant(self):
        print(f"{self.name} serves {self.cuisineType} cuisine.")

    def restaurantOpen(self):
        print(f"{self.name} is open.")