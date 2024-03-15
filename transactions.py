import time

class Transactions:
  def __init__(self, cost, time, pay):
    self.cost = cost
    self.time = time
    self.pay = pay

def get_cost(washer, dryer):
  total = float(washer + dryer)
  return f"Total cost: ${total:.2f}"

def time_track():
  return time.strftime("%H:%M")
