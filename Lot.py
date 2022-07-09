import Billing
import SpaceManager
import HandicapManager


class ParkingLot:

    def __init__(self, num_spaces, size, num_handicap_spaces, handicap_space_size, rate=3, handicap_rate=5):
        self.spaces = SpaceManager.SpaceManager(num_spaces, size)
        self.handicap_spaces = HandicapManager.HandicapManager(num_handicap_spaces, handicap_space_size)
        self.billing = Billing.Billing()
        self.rate = rate
        self.handicap_rate = handicap_rate

    def add_car(self, car):
        if not car.is_handicap():
            self.spaces.add_car(car)
        else:
            self.handicap_spaces.add_car(car)

    def remove_car(self, car):
        """
        removes the car and bills it
        :param car:
        :return:
        """
        if not car.is_handicap():
            rate, time_spent = self.spaces.remove_car(car)
        else:
            rate, time_spent = self.handicap_spaces.remove_car(car)

        self.bill(car, time_spent, rate)

    def bill(self, car, time_spent, rate):
        """
        handles billing the car
        :param car:
        :param time_spent: time spent in the parking space
        :param rate: rate to charge per
        :return:
        """
        to_pay = self.billing.bill(car, time_spent, rate)

        try:
            self.billing.add_payment(car.pay(to_pay))

        except Exception:
            print("broke, call the cops.")

    def available_space(self):
        return self.spaces.empty_spaces()

    def available_hand_space(self):
        return self.handicap_spaces.empty_spaces()
