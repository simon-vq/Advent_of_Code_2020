import os
"""
Based on the game of life problem.

Rules:
    - If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    - If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    - Otherwise, the seat's state does not change.

Functions
- idenifty edge cases; when current cell in on the outside of the board
- capture the current state of all cells that surroun the current cell
- change current seat based results of the adjecnt seats
- ignore floor space.
"""
TAKEN = '#'
FREE = 'L'
FLOOR = '.'



class Chair:
    def __init__(self,value=''):
        self.status = value

    def get_status(self):
        return self.status

    def set_available(self):
        self.status = FREE

    def set_occupied(self):
        self.status = TAKEN

    def set_floor(self):
        self.status = FLOOR

    def is_available(self):
        if self.get_status() == FREE:
            return True
        return False

    def is_occuppied(self):
        if self.get_status() == TAKEN:
            return True
        return False

    def is_floor(self):
        if self.get_status() == FLOOR:
            return True
        return False


class SeatingPlan():
    def __init__(self, data):
        self.rows = len(data)
        self.columns = len(data[0])
        self.grid = self.build_grid_from_input(data)
        self.str_grid = self.get_grid()

    def build_grid_from_input(self, data):
        new_grid = []
        for row in range(len(data)):
            new_row = []
            for col in range(len(data[0])):
                c = data[row][col]
                new_row.append(Chair(c))
            new_grid.append(new_row)
        return new_grid

    def get_grid(self):
        str_grid = [''.join([x.status for x in line]) for line in self.grid]
        return str_grid

    def update_seating(self, sight=False):
        if sight:
            n_occupied = 5
        else:
            n_occupied = 4
        new_grid = self.build_grid_from_input(self.get_grid())
        for y in range(self.rows):
            for x in range(self.columns):
                current = self.grid[y][x]
                current_neigh = self.get_neighbours(check_column=x,
                                                    check_row=y,
                                                    sight=sight)
                # Rules for change
                if current.is_available():
                    if not TAKEN in current_neigh:
                        new_grid[y][x].set_occupied()     
                elif current.is_occuppied():
                    if current_neigh.count(TAKEN) >= n_occupied:
                        new_grid[y][x].set_available()
        self.grid = new_grid
        self.str_grid = self.get_grid()

    def get_neighbours(self, check_column, check_row, sight=False):
        search_min = -1 
        search_max = 2 # max range value 
        neighbour_list = []
        for row in range(search_min, search_max):
            for column in range(search_min, search_max):
                neighbour_row = check_row + row
                neighbour_column = check_column + column
                valid_neighbour = True
                while valid_neighbour:
                    # if this is main square
                    if neighbour_row == check_row \
                        and neighbour_column == check_column:
                        valid_neighbour = False
                        break
                    # top/bottom out of bounds
                    if neighbour_row < 0 \
                        or neighbour_row >= self.rows:
                        valid_neighbour = False
                        break
                    # left/right out of bounds
                    if neighbour_column < 0 \
                        or neighbour_column >= self.columns:
                        valid_neighbour = False
                        break
                    if sight:
                        if not self.grid[neighbour_row][neighbour_column].is_floor():
                            break
                    else:
                        break
                    neighbour_row += row
                    neighbour_column += column
                # valid neighbour
                if valid_neighbour:
                    neighbour_list.append(self.grid[neighbour_row][neighbour_column].get_status())
        return neighbour_list  
    
    def complete(self, sight=False):
        previous = -1
        while True:
            self.update_seating(sight=sight)    
            current = self.count_occupied()        
            if current == previous:
                break
            previous = current

    def count_occupied(self):
        count = sum([1 for line in self.grid for x in line if x.status == TAKEN ])
        return count


if __name__ == '__main__':
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    with open(THIS_DIR+r'\input.txt','r') as f:
        data = f.read()
        data = data.splitlines()
            
    #part 1
    model = SeatingPlan(data)
    model.complete() 
    print(model.count_occupied())

    # part 2
    model = SeatingPlan(data)
    model.complete(sight=True) 
    print(model.count_occupied())