# Importing necessary library
from forex_python.converter import CurrencyRates

# Create a CurrencyRates object
cr = CurrencyRates()

# List of top 10 most traded currencies
currencies = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD']

# Get rate from USD to each currency
for currency in currencies:
    rate = cr.get_rate('USD', currency)
    print(f"The exchange rate from USD to {currency} is: {rate}")
