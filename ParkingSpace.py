import time


class ParkingSpace:

    def __init__(self, num, size, occupied=False, occupant=None, rate=5):
        """
        creates a parking space object
        :param num: the parking space number
        :param size: the dimensions of the parking space, as a tuple of length 2, (width, length)
        """
        self.num = num
        self.size = size
        self.occupied = occupied
        self.occupant = occupant
        self.entry_time = 0
        self.rate = rate

    def is_occupied(self):
        return self.occupied

    def get_occupant(self):
        return self.occupant

    def set_occupant(self, car):
        """
        adds a car to the space
        :param car:
        :return:
        """
        if car.fits_in_space(self.size):
            self.occupant = car
            self.entry_time = time.time()

        return Exception("Help, we need to lose weight.")

    def empty_space(self):
        """
        empties the space and returns how much time the car was parked
        :return: time spent in the parking space
        """
        self.occupant = None
        return time.time() - self.entry_time

