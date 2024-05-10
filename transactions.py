"""This represents the transactions that take place during the program's usage. Methods are made to get the cost, track the time of
transaction and display the choice of payment the user decides."""

from datetime import datetime

class Transactions:
    @staticmethod
    def get_cost(load_size):
        # Calculate cost based on load size
        return 0  # Placeholder for actual implementation

    @staticmethod
    def confirm_payment(payment_type):
        return "Payment Successful"  # Placeholder for actual implementation

    @staticmethod
    def time_track():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current timestamp in format

    @staticmethod
    def send_notification(recipient):
        # Placeholder for sending notification based on recipient preference
        return "Notification sent"  # Placeholder for actual implementation
