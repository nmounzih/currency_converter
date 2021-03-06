from currency import Currency

dict_rates = {'USD': 1.0, 'EUR': 0.94, 'GBP': 0.80}


class UnknownCurrencyCodeError(ValueError):
    pass


class CurrencyConverter:
    def __init__(self, dict_rates):
        self.dict_rates = dict_rates
        

    def convert(self, currency_obj, code_to_convert):
        if currency_obj.code in self.dict_rates and code_to_convert in self.dict_rates:
            return Currency(currency_obj.amount * (self.dict_rates[code_to_convert])/self.dict_rates[currency_obj.code], code_to_convert)
        else:
            raise UnknownCurrencyCodeError
        # if code_to_convert not in self.dict_rates:
        #     raise UnknownCurrencyCodeError
        # elif currency_obj.code == code_to_convert:
        #     return currency_obj
        # else:
        #     return Currency(currency_obj.amount * self.dict_rates[code_to_convert]/self.dict_rates[currency_obj.code], code_to_convert)

a = Currency("5.00", "USD")
b = Currency("4.50", "USD")
print(a - b)
