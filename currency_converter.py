from currency import Currency

dict_rates = {'USD': 1.0, 'EUR': 0.94, 'GBP': 0.80}


class UnknownCurrencyCodeError(ValueError):
    pass


class CurrencyConverter:
    def __init__(self, dict_rates, code, amount):
        self.dict_rates = dict_rates
        self.code = code
        self.amount = amount

    def convert(self, currency_obj, code_to_convert):
        if code_to_convert not in self.dict_rates:
            raise UnknownCurrencyCodeError
        elif currency_obj.code == code_to_convert:
            return currency_obj
        else:
            return (currency_obj.amount * self.dict_rates[currency_obj.code]/self.code)
