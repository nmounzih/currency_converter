from currency import Currency

a = Currency("$", "5.00")
b = Currency("$", "4.50")
f = a
c = Currency("£", "7")
d = Currency("$", "1")
e = Currency("$", "6.00")
g = 2
h = 5.0


def test_equal():
    assert (a == f) == True
    assert (a != c) == True


def test_addition():
    assert a + b == 9.5
    #assert a + c == "DifferentCurrencyCodeError"
    assert a + d == 6


def test_subtraction():
    assert a.sub(b) == 0.50
    #assert a - c == "DifferentCurrencyCodeError"
    assert e.sub(a) == 1

def test_multiply():
    assert a*g == 10
    assert a*h == 25



test_equal()
test_addition()
test_subtraction()
