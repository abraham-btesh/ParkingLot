import ParkingSpace


class HandicappedParking(ParkingSpace):

    def __init__(self, num, size, occupied=False, occupant=None, rate=9):
        super().__init__(num, size, occupied, occupant, rate)


