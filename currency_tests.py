from currency import Currency
from currency import DifferentCurrencyCodeError
from currency_converter import CurrencyConverter
from nose.tools import raises

a = Currency("5.00", "USD")
b = Currency("4.50", "USD")
f = a
c = Currency("7", "GBP")
d = Currency("1", "USD")
e = Currency("6.00", "USD")
g = 2
h = 5.0
i = Currency("0.94", "EUR")
j = Currency("1", "EUR")

def test_equal():
    assert (a == f) == True
    assert (a != c) == True


def test_addition():
    assert a + b == Currency(9.50, "USD")
    assert a + d == Currency(6, "USD")


def test_subtraction():
    assert a - b == Currency(0.50, "USD")
    assert e - a == Currency(1, "USD")


def test_multiply():
    assert a * g == Currency(10.00, "USD")
    assert a * h == Currency(25, "USD")


@raises(DifferentCurrencyCodeError)
def test_different_currency_code_error():
    a + c
    a - c


def test_conversion():
    dict_rates = {'USD': 1.0, 'EUR': 0.94, 'GBP': 0.80}
    c = CurrencyConverter(dict_rates)
    assert c.convert(a, "USD") == Currency("5.00", "USD")
    assert c.convert(d, "EUR") == Currency(0.94, "EUR")
    assert c.convert(i, "USD") == Currency(1, "USD")
    assert c.convert(j, "USD") != Currency(1, "USD")



test_equal()
test_addition()
test_subtraction()
test_multiply()
