 class MachineAvailability :
   def __init__ (self, number, machine_type, load_size): #initialize machineavailibility with attributes
     #arguments: number represents # representing certain machine, machine_type represents washer or dryer load_size represents load size of machine
     self.number = number
     self.machine_type = machine_type
     self.load_size = load_size
     self.cost = 0.0
     self.in_use = False
     self.time_remaining = 0
   def set_cost(self, base_amount, addiitonal_amount):
     self.cost = base_amount + additional_amount * self.load_size
  
   def set_availability(self, availibility):
     self.in_use = availibility

   def machine_status(self): 
     if self.in_use:
       return
