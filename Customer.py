  '''
this Customer class gets the customer login inforamtion and stores their username and password. Customer_info stores things
like the customers Name,Phone number, Email, Payment information. Set_user_info and set_user_login sets their information and
login credentials to allow access to the system.
'''

class Customer:

    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
        self.username = ""
        self.password = ""
        self.phone_num = ""
        self.email = ""
        self.card_number = ""
        self.card_ccv = ""
        self.notification_preference = ""

    def set_user_login(self, username, password):
        self.username = username
        self.password = password

    def set_user_info(self, phone_num, email, card_number, card_ccv):
        self.phone_num = phone_num
        self.email = email
        self.card_number = card_number
        self.card_ccv = card_ccv

    def set_notification_preference(self, notification_preference):
        self.notification_preference = notification_preference


