import re


class DifferentCurrencyCodeError(ValueError):
    pass


class Currency:

    known_symbols = {"$": "USD", "£": "GBP", "¥": "JPY"}

    def __init__(self, amount, code=""):
        if code == '':
            self.code = self.known_symbols[amount[0]]
            amount = re.sub(r'[$£€]', "", amount)
        else:
            self.code = code
        self.amount = float(amount)

    def __repr__(self):
        return "{}, {}".format(self.amount, self.code)

    def __eq__(self, other):
        return self.code == other.code and self.amount == other.amount

    def __add__(self, other):
        if self.code == other.code:
            return Currency(self.amount + other.amount, self.code)
        else:
            raise DifferentCurrencyCodeError("different currencies")

    def __sub__(self, other):
        if self.code == other.code:
            return Currency(self.amount - other.amount, self.code)
        else:
            raise DifferentCurrencyCodeError("different currencies")

    def __mul__(self, other):
        if type(other) == float or type(other) == int:
            return Currency(self.amount * other, self.code)
        else:
            raise TypeError

    def __rmul__(self, other):
        return self * other
