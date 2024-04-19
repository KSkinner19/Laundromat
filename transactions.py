"""This represents the transactions that take place during the program's usage. Methods are made to get the cost, track the time of
transaction and display the choice of payment the user decides."""

from datetime import datetime

import pytz


class Transactions:

  def __init__(self, cost, time, payment_type, card_number=None, prepaid_card_info=None):
    self.cost = cost
    self.time = time
    self.payment_type = payment_type
    self.card_number = card_number
    self.prepaid_card_info = prepaid_card_info

  def get_cost(washer, dryer):
    total = float(washer + dryer)
    return f"Total cost: ${total:.2f}"

  def time_track(self, time_zone='America/Los_Angeles'):
    self.time_zone = time_zone
    tz = pytz.timezone(time_zone)
    now = datetime.now(tz)
    return f"Transaction made at: {now.strftime('%I:%M %p')}."

   def make_payment(self):
        if self.payment_type == 'Card':
            if self.card_number:
                # Process card payment
                # Return True if payment is successful, False otherwise
                return True
            else:
                return False
        elif self.payment_type == 'Prepaid':
            if self.prepaid_card_info:
                # Process prepaid card payment
                # Return True if payment is successful, False otherwise
                return True
            else:
                return False
        else:
            return False

    def confirm_payment(self):
        if self.make_payment():
            return "Payment Successful"
        else:
            return "Payment Failed"

    def send_notification(self, recipient):
        if recipient == 'customer': 
            return "Notification sent to customer: Your payment has been processed."
        elif recipient == 'owner':         
            return "Notification sent to owner: A transaction has been made in your laundromat."
        else:
            return "Invalid recipient"
