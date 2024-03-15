'''
This MachineAvailability class represents which machine is in use and which isnt. It displays a status to the user for which machines 
they can and can't use, including cost, time remaining and load size of each machine.
'''

 class MachineAvailability :
  
   def __init__ (self, number, machine_type, load_size): #initialize machineavailibility with attributes
     #arguments:   
     self.number = number #number represents  certain machine
     self.machine_type = machine_type #machine_type represents washer or dryer
     self.load_size = load_size #load_size represents load size of machine
     self.cost = 0.0 #cost of service
     self.in_use = False #machine in use or not
     self.time_remaining = 0 #time remaining to finish machine task
  
  def set_cost(self, base_amount, addiitonal_amount):
   #calculate cost to use machine 
   #base amount cost of using machine additional amount = amount contingent on load size. represented in float
     self.cost = base_amount + additional_amount * self.load_size
  
   def set_availability(self, availibility):
    #availiibility status of machine
     self.in_use = availibility

   def machine_status(self): 
    #return respnse saying whther available for use or not
     if self.in_use:
      return f" Machine(self.number) is currently in use")
     else:
      return f" Machine(self.number) is currently available for use")
   def set_time_remaining(self,time):
    #set time remaining to complete task
    self.time_remaining = time
    #return message indicating time remaining for machine
    return f"Machine {self.number} has {self_time_remaining} minutes remaining until complete
  
