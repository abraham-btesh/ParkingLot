class Billing:
    """
    Acts as an accountant calculating amount of money to be billed and handling money for the parking lot
    """
    def __init__(self, starting_funds):
        self.funds = starting_funds

    def bill(self, time_spent, rate):
        return time_spent*rate

    def add_payment(self, payment):
        self.funds += payment
