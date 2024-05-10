''' this is the main.py, where it takes the customer info, customer traffic, machine availability, and transcations
and makes it accessible to both the customer and the admin. It takes user and admin information and stores it,
all while providing useful information that will keep this business afloat'''

from datetime import datetime, timedelta
import threading

from customer import Customer
from customerTraffic import CustomerTraffic
from MachineAvailability import MachineAvailability
from transactions import Transactions


def login_or_signup():
    option = input("Select:\n1. Log in\n2. Sign up\n")
    if option == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        # Perform login validation
    elif option == "2":
        name = input("Enter your first and last name: ")
        birthdate = input("Enter your birthdate mm/dd/yyyy: ")
        customer = Customer(name, birthdate)
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        customer.set_user_login(username, password)
        phone_num = input("Enter your phone number: ")
        email = input("Enter your email: ")
        card_number = input("Enter your card number: ")
        card_ccv = input("Enter your card ccv number: ")
        customer.set_user_info(phone_num, email, card_number, card_ccv)
        print("Information saved! You are now able to make purchases.")
    else:
        print("Invalid option.")


def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    # Perform admin login validation
    return username == "admin" and password == "password"


def view_machine_availability(machines):
    machine_number = int(input("There are 40 machines. Enter a machine number: "))
    if 1 <= machine_number <= len(machines):
        machine = machines[machine_number - 1]
        print(machine.machine_status())
        if machine.in_use:
            print(f"Time remaining: {machine.time_remaining} minutes")
    else:
        print("Invalid machine number.")


def view_customer_traffic(traffic):
    print(traffic.current_traffic())


def main_menu(machines, traffic):
    option = input(
    "How can we help you today?\n"
    "1. View Machine Availability\n"
    "2. View Customer Traffic\n"
    "3. Make a purchase\n"
    "4. Admin\n"
    "5. Quit\n")
    
    if option == "1":
        view_machine_availability(machines)
    elif option == "2":
        view_customer_traffic(traffic)
    elif option == "3":
        make_purchase(machines)
    elif option == "4":
        if admin_login():
            admin_menu(machines)
        else:
            print("Invalid admin credentials.")
    elif option == "5":
        print("Exiting...")
        return False
    else:
        print("Invalid option.")
    return True


def make_purchase(machines):
    machine_number = int(input("Which machine number do you wish to purchase? "))
    if 1 <= machine_number <= len(machines):
        machine = machines[machine_number - 1]
        if not machine.in_use:
            cost = machine.get_cost()  # Use get_cost method to calculate cost
            print(f"The cost of using Machine {machine_number} is: ${cost:.2f}")
            payment_type = input("Enter payment type (Card/Prepaid): ")
            transaction = Transactions.confirm_payment(payment_type)
            if transaction == "Payment Successful":
                machine.set_availability(True)
                machine.set_time_remaining(30)
                print(
                f"Machine {machine_number} has started."
                "It will be available in 30 minutes.")
                start_notification_timer(machine)
            else:
                print("Payment failed. Please try again.")
        else:
            print(f"Machine {machine_number} is currently in use.")
    else:
        print("Invalid machine number.")



def admin_menu(machines):
    option = input("Admin Menu:\n1. Change Machine Cost\n2. Back\n")
    if option == "1":
        machine_number = int(input("Enter machine number: "))
        if 1 <= machine_number <= len(machines):
            machine = machines[machine_number - 1]
            base_cost = float(input("Enter new base cost: "))  # Convert input to float
            machine.set_cost(base_cost)
            print(f"Machine {machine_number} cost updated successfully.")
        else:
            print("Invalid machine number.")
    elif option == "2":
        pass
    else:
        print("Invalid option.")


def start_notification_timer(machine):
    notification_thread = threading.Thread(
        target=send_notification_after_delay, 
        args=(machine,))
    notification_thread.start()


def send_notification_after_delay(machine):
    delay = 10  # 10 seconds for testing
    notification_time = datetime.now() + timedelta(seconds=delay)
    while datetime.now() < notification_time:
        pass  # Wait until notification time
    send_notification(machine)


def send_notification(machine):
    print(f"Notification: Machine {machine.number} is now available!")


def main():
    # Initialize machines
    machines = []
    for i in range(1, 41):
        if i <= 20:
            machines.append(MachineAvailability(
                number=i, 
                machine_type="Washer", 
                load_size="Small" if i % 3 == 0 else "Regular" 
                if i % 3 == 1 else "Large"))
        else:
            machines.append(MachineAvailability(
                number=i, 
                machine_type="Dryer", 
                load_size="Regular"))
            machines[-1].set_availability(False)

    # Initialize customer traffic
    traffic = CustomerTraffic()

    login_or_signup()
    while main_menu(machines, traffic):
        pass


if __name__ == "__main__":
    main()

