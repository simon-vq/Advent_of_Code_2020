"""
Bus:
- The time a bus takes to complete a loop is also its ID number
   e.g. ID =  `5`, departs: 0, 5, 10, 15, and so on
        ID = `11`, departs: 0, 11, 22, 33, and so on.


Scinario:

- Each bus travels to the airport, then various other locations, and finally returns 
  to the sea port to repeat its journey forever.
"""
import os

class Bus:
    def __init__(self, id_num=1) -> None:
        self.id_num = int(id_num)

    def get_time_till_next_bus(self, arrival):
        time_till_next = self.id_num - (arrival % self.id_num)
        return time_till_next

    def calculate_closest_bus(self, arrival):
        return arrival + self.get_time_till_next_bus(arrival)

class Schedule:
    def __init__(self) -> None:
        self.buses = []

    def add_multiple_buses(self,buses):
        for bus in buses:
            self.buses.append(Bus(bus))

    def add_bus(self, bus):
        self.buses.append(bus)

    def get_all_bus_ids(self):
        return [bus.id_num for bus in self.buses]

    def get_all_next_bus_times(self, arrival):
        ret_dict = {}
        for bus in self.buses:
            k = bus.calculate_closest_bus(arrival)
            ret_dict[k] = bus.id_num
        return ret_dict

    def get_time_till_all_next_bus_times(self, arrival):
        ret_dict = {}
        for bus in self.buses:
            k = bus.get_time_till_next_bus(arrival)
            ret_dict[k] = bus.id_num
        return ret_dict

    def get_closest_bus_time(self, arrival):
        all_bus_times = self.get_all_next_bus_times(arrival)
        closest_time = min(list(all_bus_times.keys()))
        return [closest_time, all_bus_times[closest_time]]

    def get_time_till_closest_bus(self, arrival):
        all_bus_times = self.get_time_till_all_next_bus_times(arrival)
        closest_time = min(list(all_bus_times.keys()))
        return [closest_time, all_bus_times[closest_time]]




if __name__ == '__main__':
    
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    with open(THIS_DIR+r'\input.txt','r') as f:
        data = f.read().split('\n')
    arrival_time = int(data[0])
    bus_data = [x for x in data[1].split(',') if x is not 'x']
    
    #part 1
    bus_schedule = Schedule()
    bus_schedule.add_multiple_buses(bus_data)
    time, bus_id = bus_schedule.get_time_till_closest_bus(arrival=arrival_time)
    print(f'Closest bus:  {bus_id}')
    print(f'Time in mins: {time}')
    print(f'multiplied: {bus_id*time}')
