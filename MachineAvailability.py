
   '''
This MachineAvailability class represents which machine is in use and which isnt. It displays a status to the user for which machines 
they can and can't use, including cost, time remaining and load size of each machine.
''' 
  class MachineAvailability:
    def __init__(self, number, machine_type, load_size):
        self.number = number
        self.machine_type = machine_type
        self.load_size = load_size
        self.cost = 0.0 
        self.additional_cost = 0.0
        self.in_use = False
        self.time_remaining = 0

    def set_cost(self, base_amount, additional_amount=0.0):
        self.cost = base_amount  # Store the updated base cost
        self.additional_cost = additional_amount

    def set_availability(self, availability):
        self.in_use = availability
        if not availability:
            self.time_remaining = 0  
            # Reset time remaining when 
            #the machine becomes available


    def machine_status(self):
        if self.in_use:
            return f"Machine {self.number} is currently in use. Time remaining: {self.time_remaining} minutes."
        else:
            return f"Machine {self.number} is currently available for use."

    def set_time_remaining(self, time):
        self.time_remaining = time
        return f"Machine {self.number} has {self.time_remaining} minutes remaining until done."

    def decrease_time_remaining(self):
        if self.in_use and self.time_remaining > 0:
            self.time_remaining -= 1

    def get_cost(self):
        return self.cost + self.additional_cost
