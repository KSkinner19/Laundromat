class Customer:
  '''
this Customer class gets the customer login inforamtion and stores their username and password. Customer_info stores things
like the customers Name,Phone number, Email, Payment information. Set_user_info and set_user_login sets their information and
login credentials to allow access to the system.
'''
  def __init__(self):
        self.username = ""
        self.password = ""
        self.name = ""
        self.phone_number = ""
        self.email = ""
        self.payment_info = ""
        self.laundry_weight = int("")
        self.notifications = []

  def set_user_info(self, name, phone_number, email, payment_info):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.payment_info = payment_info

  def set_user_login(self, ):
        self.username = username
        self.password = password
    
  def add_notification(self, notification):
        self.notifications.append(notification)

    def view_notifications(self):
        return self.notifications

class Notification:
    def __init__(self, message, timestamp):
        self.message = message
        self.timestamp = timestamp

