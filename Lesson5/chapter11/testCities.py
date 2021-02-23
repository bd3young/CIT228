import unittest
from cityFunctions import CityCountry

class CityCountryTestCase(unittest.TestCase):

    def testCityCounty(self):
        cityCountry = CityCountry('Traverse City', 'USA' )
        self.assertEqual(cityCountry, 'Traverse City, USA')
    
    def testCityCountryPop(self):
        cityCountry = CityCountry('Traverse City', 'USA', '143372')
        self.assertEqual(cityCountry, 'Traverse City, USA - 143372')

if __name__ == '__main__':
    unittest.main()