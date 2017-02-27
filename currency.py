class DifferentCurrencyCodeError(ValueError):
        pass


class Currency:
    def __init__(self, code, amount):
        self.code = code
        self.amount = float(amount)

    def __eq__(self, other):
        return self.code == other.code

    def __add__(self, other):
        if self.code == other.code:
            return self.amount + other.amount
        else:
            raise DifferentCurrencyCodeError("different currencies")

    def sub(self, other):
        if self.code == other.code:
            return (self.amount - other.amount) or (other.amount - self.amount)
        else:
            raise DifferentCurrencyCodeError("different currencies")

    def multiply(self, other):
        if type(other) == float or type(other) == int:
            return self.amount * other
        else:
            raise ValueError
