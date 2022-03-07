# 11-1
import unittest

import city_functions


class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        result = city_functions.format_location('london', 'england')
        self.assertEqual(result, 'London, England')

    def test_city_country_population(self):
        result = city_functions.format_location('london', 'england', 9540000)
        self.assertEqual(result, 'London, England - population 9540000')


if __name__ == '__main__':
    unittest.main()
