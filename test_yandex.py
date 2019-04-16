import requests
import unittest


API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


class TestServerFunctionality(unittest.TestCase):
    def setUp(self):
        params = {
            'key': API_KEY,
            'text': 'hi',
            'lang': 'en-ru'
        }
        self.response = requests.get(URL, params=params)

    def test_status(self):
        self.assertEqual(self.response.json()['code'], 200)

    def test_translation(self):
        self.assertEqual(self.response.json()['text'][0], 'привет')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

