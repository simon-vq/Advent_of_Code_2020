import unittest
from day_13.day_13 import Bus

class Test_Bus(unittest.TestCase):
    def test_create_Bus_obj(self):
        test_obj = Bus()
        self.assertIsInstance(test_obj, Bus)

    def test_create_Bus_with_custom_id(self):
        test_id = 5
        test_obj = Bus(test_id)
        self.assertEqual(test_obj.id_num, test_id)
