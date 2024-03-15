from datetime import datetime
import pytz

class Transactions:
  '''
Transcations class will display the total amount of money spent on machines and stores the time in which the machines usage starts 
'''
  def __init__(self, cost, time, pay):
    self.cost = cost
    self.time = time
    self.pay = pay

def get_cost(washer, dryer):
  total = float(washer + dryer)
  return f"Total cost: ${total:.2f}"



def time_track(time_zone='America/Los_Angeles'):
    tz = pytz.timezone(time_zone)
    now = datetime.now(tz)
    return f"Transaction made at: {now.strftime('%I:%M %p')}"
