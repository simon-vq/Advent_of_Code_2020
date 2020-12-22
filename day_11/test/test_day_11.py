import unittest
from day_11.day_11 import Chair, SeatingPlan
import os


class Test_Chair(unittest.TestCase):
   
    def test_set_occupied(self):
        test_obj = Chair()
        test_obj.set_occupied()
        self.assertEqual(test_obj.status,'#')

    def test_set_available(self):
        test_obj = Chair()
        test_obj.set_available()
        self.assertEqual(test_obj.status,'L')

    def test_set_floor(self):
        test_obj = Chair()
        test_obj.set_floor()
        self.assertEqual(test_obj.status,'.')

    def test_is_available(self):
        test_obj = Chair()
        test_obj.set_available()
        result = test_obj.is_available()
        self.assertTrue(result)

    def test_is_available_false(self):
        test_obj = Chair()
        test_obj.set_occupied()
        result = test_obj.is_available()
        self.assertFalse(result)

    def test_get_status(self):
        test_obj = Chair()
        test_obj.set_occupied()
        result = test_obj.get_status()
        self.assertEqual(result, '#')


class Test_SeatingPlan(unittest.TestCase):
    def load_test_data(self, test_type, n_tests=5):
        THIS_DIR = os.path.dirname(os.path.abspath(__file__))
        with open(THIS_DIR+r'\test_input.txt','r') as f:
            test_input_file = f.read().split('\n')

        test_output = {}
        test_range = range(n_tests)
        for i in test_range:
            with open(THIS_DIR+r'\test_'+str(test_type)+r'_'+str(i)+r'.txt','r') as f:
                list_items = f.read().split('\n')
            test_output[i] = list_items
        return test_input_file, test_output


    def create_blank_grid(self, row, col, value=0):
        grid = [''.join([str(value) for x in range(col)]) for y in range(row)]
        return grid

    def test_grid_row_input(self):
        row=2
        test_input = self.create_blank_grid(row=row, col=3)
        results = SeatingPlan(test_input)
        self.assertEqual(results.rows, row)

    def test_grid_column_input(self):
        col=3
        test_input = self.create_blank_grid(row=2, col=col)
        results = SeatingPlan(test_input)
        self.assertEqual(results.columns, col) 

    def test_build_grid_from_input(self):
        test_input = self.create_blank_grid(row=2, col=3)
        result = SeatingPlan(test_input)
        self.assertEqual(result.get_grid(), test_input)


    def test_build_grid_from_grid(self):
        test_input = self.create_blank_grid(row=2, col=3)
        result = SeatingPlan(test_input)
        self.assertEqual(result.get_grid(), test_input)

    def test_get_grid(self):
        test_input = self.create_blank_grid(row=2, col=3)
        plan_1 = SeatingPlan(test_input)
        plan_2 = SeatingPlan(plan_1.get_grid())
        self.assertListEqual(plan_2.get_grid(), test_input)

    def test_get_grid_with_different_values(self): 
        test_input = [[0,1],[2,3],[4,5]]
        plan = SeatingPlan(test_input) 
        self.assertListEqual(plan.get_grid(), test_input)

    def test_get_grid_with_different_values(self): 
        test_input, test_output_dict = self.load_test_data('output')
        plan = SeatingPlan(test_input) 
        self.assertListEqual(plan.get_grid(), test_input)

    def test_update_seating(self):
        test_input, test_output_dict = self.load_test_data('output')
        result = SeatingPlan(test_input)
        result.update_seating()
        self.assertListEqual(result.get_grid(), test_output_dict[0])
    
    def test_update_seating_adjacent_chain(self):
        test_input, test_output_dict = self.load_test_data('output')
        result = SeatingPlan(test_input)
        for key in test_output_dict:
            result.update_seating() 
            self.assertListEqual(result.get_grid(), test_output_dict[key])

    def test_update_seating_adjacent_has_changed_grid(self):
        test_input, test_output_dict = self.load_test_data('output')
        result = SeatingPlan(test_input)
        result.update_seating()
        self.assertNotEqual(result.get_grid(), test_input)

    def test_count_occupied(self):
        test_input = [['#','.','#'],
                      ['L','L','#'],
                      ['.','.','L']]
        result = SeatingPlan(test_input)
        self.assertEqual(result.count_occupied(), 3)

    def test_get_sightings_full(self):
        THIS_DIR = os.path.dirname(os.path.abspath(__file__))
        with open(THIS_DIR+r'\test_sighting_full.txt','r') as f:
            test_input_file = f.read().split('\n')
        model = SeatingPlan(test_input_file)
        neighbours = model.get_neighbours(check_column=3, check_row=4, sight=True)
        self.assertEqual(len(neighbours), 8)

    def test_get_sightings_empty(self):
        THIS_DIR = os.path.dirname(os.path.abspath(__file__))
        with open(THIS_DIR+r'\test_sighting_empty.txt','r') as f:
            test_input_file = f.read().split('\n')
        model = SeatingPlan(test_input_file)
        neighbours = model.get_neighbours(check_column=3, check_row=3, sight=True)
        self.assertEqual(len(neighbours), 0)
        
    def test_update_seating_sighting_chain(self):
        test_input, test_output_dict = self.load_test_data('sightings', n_tests=6)
        result = SeatingPlan(test_input)
        for key in test_output_dict:
            result.update_seating(sight=True) 
            self.assertListEqual(result.get_grid(), test_output_dict[key])

  
if __name__ == '__main__':
    unittest.main()


