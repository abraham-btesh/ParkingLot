class Auto:

    def __init__(self, _type, year, size, handicap=False):
        self._type = _type
        self.year = year
        self.width, self.length = size
        self.handicap = handicap
        self.funds = 100

    def fits_in_space(self, space_size):
        """
        checks that the cars dimensions are compatible with the spaces
        :param space_size:
        :return:
        """
        space_width, space_length = space_size
        if space_width >= self.width and space_length >= self.length:
            return True
        return False

    def is_handicap(self):
        """
        check if the car has a handicap permit
        :return:
        """
        return self.handicap

    def pay(self, amount):
        """
        pay parking bill
        :param amount: amount to pay
        :return: amount of money, or an exception
        """
        if self.funds >= amount:
            self.funds -= amount
            return amount

        return Exception("we have no money, oh no!")

