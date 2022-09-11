from forex_python.converter import CurrencyRates
def print_hi():
    c = CurrencyRates()
    result=c.get_rates('USD')
    print(result)
print(print_hi())
