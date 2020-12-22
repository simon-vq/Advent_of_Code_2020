import math
from unittest import result
from day_12.day_12 import Ship, Waypoint
import unittest
import os

"""
F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
N3 would move the ship 3 units north to east 10, north 3.
F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
F11 would move the ship 11 units south to east 17, south 8.
"""
class Test_Waypoint(unittest.TestCase):
    def test_create_Waypoint(self):
        test_obj = Waypoint(ship_E=0,ship_N=0)
        self.assertIsInstance(test_obj, Waypoint)

    def test_create_waypoint_with_ship_position(self):
        test_obj = Waypoint(ship_E=0, ship_N=0)
        exspected = (10,1)
        self.assertEqual(test_obj.get_waypoint_config(), exspected)

    def test_configure_waypoint(self):
        test_obj = Waypoint(ship_E=0, ship_N=0)
        test_obj.configure_waypoint(wp_E=10, wp_N=5)
        exspected = (10,5)
        self.assertEqual(test_obj.get_waypoint_config(), exspected)
        
    def test_update_waypoint_location(self):
        test_obj = Waypoint(ship_E=0, ship_N=0)
        test_obj.update_waypoint_location(ship_E=10, ship_N=5)
        exspected = (20,6)
        self.assertEqual(test_obj.get_waypoint_locations(), exspected)

    def test_rotate(self):
        '''rotate() 90 degs counterclock wise.
        '''
        test_obj = Waypoint(ship_E=0, ship_N=0)
        result = test_obj.rotate(origin=test_obj.ship_location, 
                                point=[test_obj.location_E, test_obj.location_N],
                                angle=math.radians(90))
        exspected = (-1,10)
        self.assertEqual(result, exspected)

    def test_rotate_clockwise(self):
        '''rotate() 90 degs clockwise.
        deg = 360-90 = 270
        '''
        test_obj = Waypoint(ship_E=0, ship_N=0)
        result = test_obj.rotate(origin=test_obj.ship_location, 
                                point=[test_obj.location_E, test_obj.location_N],
                                angle=math.radians(270))
        exspected = (1,-10)
        self.assertEqual(result, exspected)

    
class Test_Ship(unittest.TestCase):
    
    def test_create_Ship(self):
        test = Ship()
        self.assertIsInstance(test, Ship)

    def test_get_direction(self):
        test = Ship()
        result = test.get_direction()
        self.assertEqual(result, 'E')
    
    def test_get_position(self):
        test = Ship()
        result = test.get_position()
        self.assertEqual(result,(0,0))

    def test_decode_instructions(self):
        test_inputs = ['F10', 'N3', 'F7', 'R90', 'F11']
        exspected = [('F',10), ('N',3), ('F',7), ('R',90), ('F',11)]
        test_obj = Ship()
        for i, test in enumerate(test_inputs):
            result = test_obj.decode_instuctions(test)
            self.assertEqual(result, exspected[i])

    def test_turn_left(self):
        test_obj = Ship()
        test_obj.set_direction('N')
        test_obj.turn(steps=90, direction='L')
        self.assertEqual(test_obj.get_direction(), 'W')

    def test_turn_right(self):
        test_obj = Ship()
        test_obj.set_direction('W')
        test_obj.turn(steps=90, direction='R')
        self.assertEqual(test_obj.get_direction(), 'N')

    def test_move_forward(self):
        test_obj = Ship()
        test_obj.set_direction('N')
        test_obj.move_forward(steps=10)
        self.assertEqual(test_obj.get_position(), (0,10))

    def test_process_instruction(self):
        test_input = 'F10'
        exspected = (10,0)
        test_obj = Ship()
        test_obj.set_direction('E')
        test_obj.process_instruction(test_input)
        self.assertEqual(test_obj.get_position(), exspected)

    def test_process_list_instruction(self):
        test_inputs = ['F10', 'N3', 'F7', 'R90', 'F11']
        exspected = 25
        test_obj = Ship()
        test_obj.set_direction('E')
        test_obj.process_list_instructions(test_inputs)
        manhatten = test_obj.get_distance()
        self.assertEqual(manhatten, exspected)


    def test_turn_clockwise(self):
        '''rotate ship 90deg clockwise using turn()'''
        test_obj = Ship(facing='E', east=10, north=10)
        test_obj.waypoint.configure_waypoint(wp_E=10, wp_N=1)
        test_obj.turn(steps=90, direction='R')
        self.assertEqual(test_obj.facing, 'S')
        self.assertEquals(test_obj.waypoint.get_waypoint_config(), (1,-10))
        self.assertEquals(test_obj.waypoint.get_waypoint_locations(), (11,0))

    
    def test_turn_counterclockwise(self):
        '''rotate ship 90deg counterclockwise using turn()'''
        test_obj = Ship(facing='E', east=10, north=10)
        test_obj.waypoint.configure_waypoint(wp_E=10, wp_N=1)
        test_obj.turn(steps=90, direction='L')
        self.assertEqual(test_obj.facing, 'N')
        self.assertEquals(test_obj.waypoint.get_waypoint_config(), (-1, 10) )
        self.assertEquals(test_obj.waypoint.get_waypoint_locations(), (9, 20))
    
    def test_process_waypoint_instruction(self):
        test_inputs = ['F10', 'N3', 'F7', 'R90', 'F11']
        test_obj = Ship(facing='E', east=0, north=0)
        test_obj.waypoint.configure_waypoint(wp_E=10, wp_N=1)
        for instruction in test_inputs:
            test_obj.process_waypoint_instruction(instruction)
        exspected = (214, -72)
        self.assertEqual(test_obj.get_position(),exspected)



if __name__ == '__main__':
    unittest.main()