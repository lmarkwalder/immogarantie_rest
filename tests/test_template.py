from .context import app

import unittest 

class MyTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True

    def test_call_roof_type_classifier(self):
        assert 1 == 2

if __name__ == '__main__':
    unittest.main()
