import unittest
import json
from helpers.api import *

fixtures_dir = "test/fixtures/"


class TestHelperAPI(unittest.TestCase):

    def test_api_should_be_online(self):
        status_code = ping()
        self.assertEqual(200, status_code)

    def test_extract_price_should_return_number_from_json(self):
        with open(fixtures_dir + "api-response-example.json", 'r') as fixture:
            fixture_json = json.loads("".join(fixture.readlines()))
            price = extract_price(fixture_json)
            self.assertGreater(price, 0)

    def test_get_data_should_return_json(self):
        coin_ticker = "bitcoin"
        response = get_data(coin_ticker)
        self.assertIsNotNone(response)
        self.assertIn("'dict'", str(type(response)))

    def test_get_price_should_return_number(self):
        coin_ticker = "bitcoin"
        price = get_price(coin_ticker)
        self.assertGreater(price, 0)


if __name__ == '__main__':
    unittest.main()
