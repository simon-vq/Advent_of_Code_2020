"""
Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.
"""
import os
import math

class Waypoint:
    def __init__(self, ship_E, ship_N):
        self.configure_waypoint()
        self.update_waypoint_location(ship_E, ship_N)  

    def configure_waypoint(self, wp_E=10, wp_N=1):
        self.config_E = wp_E
        self.config_N = wp_N

    def move_waypoint_north(self, steps):
        self.config_N += int(steps)
        self.location_N += int(steps)
    def move_waypoint_south(self, steps):
        self.config_N -= int(steps)
        self.location_N -= int(steps)
    def move_waypoint_east(self, steps):
        self.config_E += int(steps)
        self.location_E += int(steps)
    def move_waypoint_west(self, steps):
        self.config_E -= int(steps)
        self.location_E -= int(steps)

    def update_waypoint_location(self, ship_E, ship_N):
        self.location_E = ship_E + self.config_E
        self.location_N = ship_N + self.config_N
        self.ship_location = [ship_E, ship_N]
   
    def get_waypoint_config(self):
        return self.config_E, self.config_N

    def get_waypoint_locations(self):
        return self.location_E, self.location_N
            
    def rotate(self, origin, point, angle):
        """ 
        Rotate a point counterclockwise by a given angle around a given origin.
        The angle should be given in radians.
        """
        ox,oy = origin
        px,py = point
        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        return int(round(qx)), int(round(qy))

    def rotate_instruction(self, deg=90, counter_c=True):
        if not counter_c:
            deg = int(360 - deg)
        self.location_E, self.location_N = self.rotate(origin=self.ship_location,
                                                        point=self.get_waypoint_locations(),
                                                        angle=math.radians(deg))
        self.config_E, self.config_N = self.rotate(origin=[0,0],
                                                    point=self.get_waypoint_config(),
                                                    angle=math.radians(deg))


class Ship:
    def __init__(self, facing='E', east=0, north=0) -> None:
        self.facing = facing
        self.east = east
        self.north = north
        self.waypoint = Waypoint(ship_E=self.east, ship_N=self.north)

    def get_direction(self):
        return self.facing

    def set_direction(self, new_direction):
        self.facing = new_direction

    def get_position(self):
        return (self.east, self.north)

    def decode_instuctions(self, instruction):
        direction = instruction[0] 
        movement = int(instruction[1:])
        return (direction, movement)

    def move_north(self, steps):
        self.north += int(steps)
    def move_south(self, steps):
        self.north -= int(steps)
    def move_east(self, steps):
        self.east += int(steps)
    def move_west(self, steps):
        self.east -= int(steps)

    

    def turn(self, steps, direction):
        facing_char = ['N','E','S','W']
        current_facing = self.get_direction()
        deg_steps = int(steps/90)
        new_facing = current_facing
        if direction == 'R':
            new_facing = (facing_char.index(current_facing) + deg_steps) % 4
            self.waypoint.rotate_instruction(deg=steps, counter_c=False)
        elif direction == 'L':
            new_facing = (facing_char.index(current_facing) - deg_steps)
            self.waypoint.rotate_instruction(deg=steps, counter_c=True)
        new_facing_char = facing_char[new_facing]
        self.set_direction(new_facing_char)


    def move_forward(self, steps):
        current_dir = self.get_direction()
        if current_dir == 'N':
            self.move_north(steps=steps)
        elif current_dir == 'E':
            self.move_east(steps=steps)
        elif current_dir == 'S':
            self.move_south(steps=steps)
        elif current_dir == 'W':
            self.move_west(steps=steps)


    def move_towards_waypoint(self, steps):
        for _ in range(steps):
            self.east, self.north = self.waypoint.get_waypoint_locations()
            self.waypoint.update_waypoint_location(self.east, self.north)
            


    def process_waypoint_instruction(self, instruction):
        new_instr = self.decode_instuctions(instruction)
        direction = new_instr[0]
        steps = new_instr[1]
        if direction in ['L','R']:
            self.turn(steps, direction)
        elif direction == 'N':
            self.waypoint.move_waypoint_north(steps=steps)
        elif direction == 'E':
            self.waypoint.move_waypoint_east(steps=steps)
        elif direction == 'S':
            self.waypoint.move_waypoint_south(steps=steps)
        elif direction == 'W':
            self.waypoint.move_waypoint_west(steps=steps)
        elif direction == 'F':
            self.move_towards_waypoint(steps=steps)

    def process_waypoint_list_instructions(self, list_instructions):
        for instruction in list_instructions:
            self.process_waypoint_instruction(instruction=instruction)

    def process_instruction(self, instruction):
        new_instr = self.decode_instuctions(instruction)
        direction = new_instr[0]
        steps = new_instr[1]
        if direction in ['L','R']:
            self.turn(steps, direction)
        elif direction == 'N':
            self.move_north(steps=steps)
        elif direction == 'E':
            self.move_east(steps=steps)
        elif direction == 'S':
            self.move_south(steps=steps)
        elif direction == 'W':
            self.move_west(steps=steps)
        elif direction == 'F':
            self.move_forward(steps=steps)

    def process_list_instructions(self, list_instructions):
        for instruction in list_instructions:
            self.process_instruction(instruction=instruction)

    def get_distance(self):
        co_ords = self.get_position()
        x = abs(co_ords[0])
        y = abs(co_ords[1])
        return x+y


if __name__ == '__main__':

    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    with open(THIS_DIR+r'\input.txt','r') as f:
        instructions = f.read()
        instructions = instructions.splitlines()

    # part 1
    ship = Ship()
    ship.set_direction('E')
    ship.process_list_instructions(instructions)
    print(ship.get_distance())

    # part 2
    ship = Ship()
    ship.process_waypoint_list_instructions(instructions)
    print(ship.get_distance())
