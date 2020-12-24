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
        if id_num == 'x':
            self.id_num = 1
        else:
            self.id_num = int(id_num)
    
    def get_time_till_next_bus(self, arrival):
        time_till_next = self.id_num - (arrival % self.id_num)
        if time_till_next == self.id_num:
            return 0
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

    def search_sequence(self, time):
        for i, bus in enumerate(self.buses):
            mins_to_wait = bus.get_time_till_next_bus(time+i)
            if mins_to_wait:
                return False         
        return True


    def find_bus_sequence(self):
        bus_ids = self.get_all_bus_ids()
        max_bus = max(bus_ids)
        max_bus_idx = bus_ids.index(max_bus)
        count = max_bus - max_bus_idx

        while True:
            if self.search_sequence(count):
                break
            count += max_bus

        return count

if __name__ == '__main__':
    
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    with open(THIS_DIR+r'\input.txt','r') as f:
        data = f.read().split('\n')
    arrival_time = int(data[0])
    origina_bus_data = data[1].split(',')
    bus_data = [x for x in origina_bus_data if x is not 'x']
    
    #part 1
    bus_schedule = Schedule()
    bus_schedule.add_multiple_buses(bus_data)
    time, bus_id = bus_schedule.get_time_till_closest_bus(arrival=arrival_time)
    print(f'Closest bus:  {bus_id}')
    print(f'Time in mins: {time}')
    print(f'multiplied: {bus_id*time}')

    #part 2
    bus_schedule = Schedule()
    bus_schedule.add_multiple_buses(bus_data)
    time = bus_schedule.find_bus_sequence()
    print(f'Time in mins: {time}')
   

    test_seq = [7,13,'x','x',59,'x',31,19]
    test_obj = Schedule()
    for bus in test_seq:
        test_obj.add_bus(Bus(bus))
    if test_obj.find_bus_sequence() == 1068781:
        print(test_obj.find_bus_sequence())