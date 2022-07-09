import HandicappedParking
import SpaceManager


class HandicapManager(SpaceManager):

    def __init__(self, num, dimensions):
        self.empty_spaces = [HandicappedParking(i, dimensions) for i in range(1, num + 1)]
        self.occupied_spaces = []
