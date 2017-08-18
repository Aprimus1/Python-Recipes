# json_response.py

import requests

def get_json_data(url):
    r = requests
    response = r.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

if __name__ == '__main__':
    print(get_json_data('http://ip.jsontest.com/'))
    
#----------------------------------------------------------

# mock_example_test.py

import unittest
from unittest.mock import Mock, patch
from json_response import get_json_data


@patch("json_response.requests.get")
class TestJsonResponse(unittest.TestCase):

    def test_get_json_data_with_wrong_status_code(self, mock_get):
        mock_get.return_value.status_code = 400
        self.assertEqual(get_json_data('http://ip.jsontest.com/'), None)

    def test_get_some_data_with_correct_status_code(self, mock_get):
        mock_get.return_value.status_code = 200
        data = {"ip": "91.37.99.172"}
        mock_get.return_value.text = data
        self.assertEqual(get_json_data('http://ip.jsontest.com/'), data)



if __name__ == '__main__':
    unittest.main()


