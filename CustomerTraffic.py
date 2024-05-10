  '''
this Customer class gets the customer login inforamtion and stores their username and password. Customer_info stores things
like the customers Name,Phone number, Email, Payment information. Set_user_info and set_user_login sets their information and
login credentials to allow access to the system.
'''

class CustomerTraffic:
    def __init__(self, users=0, machines_in_use=0, machines_not_in_use=40):
        self.users = users
        self.machines_in_use = machines_in_use
        self.machines_not_in_use = machines_not_in_use
        self.level = ""

    def current_traffic(self):
        if self.machines_in_use >= 30:
            self.level = "Highly"
        elif self.machines_in_use > 20:
            self.level = "Moderately busy"
        elif self.machines_in_use > 10:
            self.level = "Not very"

        return f"Current traffic: {self.users} users in store " \
               f"{self.machines_in_use} machines in use."

    def traffic_summary(self, total_users):
        if total_users < 0:
            return "Error: Number of users cannot be negative."

        return f"Traffic summary: {total_users} users visited the laundromat today."
