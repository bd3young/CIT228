from restaurant import Restaurant

class IcecreamStand(Restaurant):
    def __init__(self, name, cusineType, numberServed, *flavors):
        super().__init__(name, cusineType, numberServed)
        self.flavors = flavors
    
    def todaysFlavors(self):
        print('Todays Flavors are')
        print('-----------------------')
        for flavor in self.flavors:
            print(f'\t- {flavor}')