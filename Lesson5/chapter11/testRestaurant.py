import unittest
from restaurant import Restaurant

class TestRestaurant(unittest.TestCase):
    
    def setUp(self):
        name='Big Robs Tacos'
        cuisineType = 'Mexican'
        numberServed = 100
        self.restaurant = Restaurant(name, cuisineType, numberServed)

    def testSetNumberServed(self):
        numberServed = 1000
        self.restaurant.setNumberServed(numberServed)
        self.assertEqual(self.restaurant.numberServed,1000)

    def testIncrementNumberServed(self):
        numberServed=200
        self.restaurant.incrementNumberServed(numberServed)
        self.assertEqual(self.restaurant.numberServed,300)  

if __name__ == '__main__':
    unittest.main()
