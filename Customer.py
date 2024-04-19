class Customer:
  '''
this Customer class gets the customer login inforamtion and stores their username and password. Customer_info stores things
like the customers Name,Phone number, Email, Payment information. Set_user_info and set_user_login sets their information and
login credentials to allow access to the system.
'''
  def __init__(self, name, laundry_weight):
        self.login = ""
        self.customer_info = ""
        self.name = name
        self.laundry_weight = laundry_weight
        self.notifications = []

  def set_user_info(self, info):
        self.customer_info = info

  def set_user_login(self, login):
        self.login = login
    
  def add_notification(self, notification):
        self.notifications.append(notification)

    def view_notifications(self):
        return self.notifications

class Notification:
    def __init__(self, message, timestamp):
        self.message = message
        self.timestamp = timestamp

