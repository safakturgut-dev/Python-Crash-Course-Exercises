# 11-1
import unittest

import city_functions


class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        result = city_functions.format_location('london', 'england')
        self.assertEqual(result, 'London, England')


if __name__ == '__main__':
    unittest.main()
