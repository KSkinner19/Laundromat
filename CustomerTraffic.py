
class CustomerTraffic:
  '''
this Customer class gets the customer login inforamtion and stores their username and password. Customer_info stores things
like the customers Name,Phone number, Email, Payment information. Set_user_info and set_user_login sets their information and
login credentials to allow access to the system.
'''
  def __init__(self, users=0, machines_in_use=0):
    self.users = users
    self.machines_in_use = machines_in_use
    self.user_info = {}
  def set_userInfo(self, username, info):
    self.user_info[username] = info
  def set_userLogin(self, username, password):
    if username in self.user_info:
      sefl.user_info[username]['password'] = password
    else:
      print("User not found")
  def current_traffic(self,):
    print("Current Traffic:")
    print("Users:", self.users)
    print("Machines in Use:", self.machines_in_use)
  def traffic_sumamry(self, users):
     print("Traffic Summary:")
     print("Total Users:", self.users)
        
