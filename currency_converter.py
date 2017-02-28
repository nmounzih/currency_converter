import Currency

dict_rates = {'USD': 1.0, 'EUR': 0.94, 'GBP': 0.80}


class UnknownCurrencyCodeError(ValueError):
    pass


class CurrencyConverter:
    def __init__(self, dict_rates, code):
        self.code = code
        self.amount = amount
        self.dict_rates = dict_rates

    def convert(self, currency_obj, currency_to_convert):
        if currency_to_convert not in self.dict_rates:
            raise UnknownCurrencyCodeError
        elif currency_obj.code == currency_to_convert:
            return currency_obj
        else:
                if currency_to_convert == 'GBP':
                    return (0.8 * currency_obj.amount)
                elif currency_to_convert == 'EUR':
                    return (0.94 * currency_obj.amount)
                elif currency_to_convert == 'USD':
                    return(1.0 * currency_obj.amount)
