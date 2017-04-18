import re


class DifferentCurrencyCodeError(ValueError):
    pass


class Currency:

    known_codes = {"USD": "$", "GBP": "£", "JPY": "¥"}
    known_symbols = {"$": "USD", "£": "GBP", "¥": "JPY"}

    def __init__(self, amount, code=""):
        self.code = code
        self.amount = re.sub(r'[^$£€B]', "", float(amount))

    def __repr__(self):
        return "{}{}".format(self.amount, self.code)

    def __eq__(self, other):
        return self.code == other.code and self.amount == other.amount

    def __add__(self, other):
        if self.code == other.code:
            return self.amount + other.amount
        else:
            raise DifferentCurrencyCodeError("different currencies")

    def __sub__(self, other):
        if self.code == other.code:
            return (self.amount - other.amount) or (other.amount - self.amount)
        else:
            raise DifferentCurrencyCodeError("different currencies")

    def __mul__(self, other):
        if type(other) == float or type(other) == int:
            return self.amount * other, self.code
        else:
            raise TypeError

    def __rmul__(self, other):
        return self * other
