from day_11 import test
import unittest
from day_13.day_13 import Bus, Schedule

class Test_Bus(unittest.TestCase):
    def test_create_Bus_obj(self):
        test_obj = Bus()
        self.assertIsInstance(test_obj, Bus)

    def test_create_Bus_with_custom_id(self):
        test_id = 5
        test_obj = Bus(test_id)
        self.assertEqual(test_obj.id_num, test_id)

    def test_calculate_closest_bus(self):
        test_bus_input = [7,13,59]
        exspected = [945,949,944]
        test_time = 939
        for bus, ex in zip(test_bus_input, exspected):
            test_obj = Bus(bus)
            result = test_obj.calculate_closest_bus(test_time)
            self.assertEqual(result, ex)

    def test_1_min_till_next_bus(self):
        test_val = 17
        arrival_time = 16
        expected = test_val - arrival_time
        test_obj=Bus(test_val)
        result = test_obj.get_time_till_next_bus(arrival_time)
        self.assertEqual(result, expected)


    def test_zero_time_till_next_bus(self):
        test_val = 17
        arrival_time = 17
        expected = test_val - arrival_time
        test_obj=Bus(test_val)
        result = test_obj.get_time_till_next_bus(arrival_time)
        self.assertEqual(result, expected)


class Test_Schedule(unittest.TestCase):
    def test_create_bus_schedule(self):
        test_bus_input = [7,13,59]
        test_obj = Schedule()
        for bus in test_bus_input:
            test_obj.add_bus(Bus(bus))
        self.assertEqual(test_obj.get_all_bus_ids(), test_bus_input)
    
    def test_get_next_bus_times(self):
        test_obj = Schedule()
        test_obj.add_bus(Bus(7))
        test_obj.add_bus(Bus(13))
        test_obj.add_bus(Bus(59))
        test_time = 939
        results = test_obj.get_all_next_bus_times(test_time)
        exspected = {945: 7, 949: 13, 944: 59}
        self.assertEqual(results,exspected)

    def test_get_closest_bus_time(self):
        test_obj = Schedule()
        test_obj.add_bus(Bus(7))
        test_obj.add_bus(Bus(13))
        test_obj.add_bus(Bus(59))
        test_time = 939
        results = test_obj.get_closest_bus_time(test_time)
        exspected = [944, 59]
        self.assertEqual(results,exspected)

    def test_get_time_till_closest_bus(self):
        test_obj = Schedule()
        test_obj.add_bus(Bus(7))
        test_obj.add_bus(Bus(13))
        test_obj.add_bus(Bus(59))
        test_time = 939
        results = test_obj.get_time_till_closest_bus(test_time)
        exspected = [5, 59]
        self.assertEqual(results,exspected)


    def test_find_longer_bus_sequence(self):
        test_seq = [7,13,'x','x',59,'x',31,19]
        test_obj = Schedule()
        for bus in test_seq:
            test_obj.add_bus(Bus(bus))
        self.assertEqual(test_obj.find_bus_sequence(), 1068781)


    def test_find_bus_sequence(self):
        test_seq = [17,'x',13,19]
        test_obj = Schedule()
        for bus in test_seq:
            test_obj.add_bus(Bus(bus))
        self.assertEqual(test_obj.find_bus_sequence(), 3417)


    