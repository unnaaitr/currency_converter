
# CURRENCY CONVERTER IN REAL TIME WITH INTERNET

# We need to install our libraries first and other things too
import requests

API_KEY = "e2f6ec04bf4dae03ad8061f4"


# Thing for the APP, rates and data
response = requests.get(f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD")
data = response.json()
rates = data["conversion_rates"]


# We print the convertions
print("\nRates to $1 USD:")
print(f"- {rates['EUR']} €") # Euros
print(f"- {rates['GBP']} £") # Pounds
print(f"- {rates['JPY']} ¥\n") # Yens


# We ask the user what he wants
amount = float(input("Choose the quantity to convert: "))
from_currency = str(input("- Which currency is it? ")).strip().upper()
to_currency = str(input("- Which currency do you want to convert it to? ")).strip().upper()


# We just need a simple function for it all
def convert(amount, from_currency, to_currency, rates):
    result = (amount / rates[from_currency]) * rates[to_currency]
    print(f"{amount} {from_currency} = {result:.2f} {to_currency}\n")
    return result

convert(amount, from_currency, to_currency, rates)