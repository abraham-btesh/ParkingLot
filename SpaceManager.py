import ParkingSpace


class SpaceManager:
    def __init__(self, num, dimensions, rate):
        self.empty_spaces = [ParkingSpace(i, dimensions, rate) for i in range(1, num + 1)]
        self.occupied_spaces = []

    def add_car(self, car):
        """
        adds a car to a space
        :param car: car  object
        :return: None or exception, if there is no available space
        """
        if len(self.empty_spaces) != 0:
            space = self.empty_spaces.pop()
            if not space.is_occupied():

                try:
                    space.set_occupant()
                except Exception:
                    print("Problem, the space is full")
                    return

                self.occupied_spaces.append(space)
        else:
            return Exception("there are no available spaces")

    def remove_car(self, car):
        """
        removes the car from the space
        :param car: the car to remove
        :return: the amount of time that car has been parked.
        """
        for space in self.occupied_spaces:
            if car == space.get_occupant():
                time_spent = space.empty_space()
                rate = space.rate
            self.empty_spaces.append(space)
            self.occupied_spaces.remove(space)
        return rate, time_spent

    def is_space_available(self):
        """
        Checks if there are empty spaces
        :return: True if there are, otherwise False
        """
        if len(self.empty_spaces) != 0:
            return True

        return False
