import unittest
import cityFunctions.CityCountry as CityCountry

class CityCountryTestCase(unittest.TestCase):

    def testCityCounty(self):
        cityCountry = CityCountry('Traverse City', 'USA' )
        self.assertEqual(cityCountry, 'Traverse City, USA')

if __name__ == '__main__':
    unittest.main()