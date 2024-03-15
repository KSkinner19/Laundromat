# this is the customer class 
'''
this Customer class gets the customer login inforamtion and stores their username and password. Customer_info stores things
like the customers Name,Phone number, Email, Payment information. Set_user_info and set_user_login sets their information and
login credentials to allow access to the system.

'''

class Customer:
  
  def __init__(self):
        self.login = ""
        self.customer_info = ""

  def set_user_info(self, info):
        self.customer_info = info

  def set_user_login(self, login):
        self.login = login

