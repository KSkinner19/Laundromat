"""This represents the transactions that take place during the program's usage. Methods are made to get the cost, track the time of
transaction and display the choice of payment the user decides."""

from datetime import datetime

import pytz


class Transactions:

  def __init__(self, cost, time, pay):
    self.cost = cost
    self.time = time
    self.pay = pay

  def get_cost(washer, dryer):
    total = float(washer + dryer)
    return f"Total cost: ${total:.2f}"

  def time_track(self, time_zone='America/Los_Angeles'):
    self.time_zone = time_zone
    tz = pytz.timezone(time_zone)
    now = datetime.now(tz)
    return f"Transaction made at: {now.strftime('%I:%M %p')}."

  def payment(choice):
    if choice == 0:
      return "Payment form: Card"
    elif choice == 1:
      return "Payment form: Prepaid"
