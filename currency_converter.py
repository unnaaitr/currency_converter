
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
print(f"- {rates['EUR']:.3f} €") # Euros
print(f"- {rates['GBP']:.3f} £") # Pounds
print(f"- {rates['JPY']:.3f} ¥\n") # Yens


# We ask the user what he wants, solving minor issues like money < 0
while True:
    try:
        amount = float(input("Choose the quantity to convert: "))
        print(" ") # Added another line to make it look cooler

        if amount <= 0:
            print("Try again!\n")  

        else:  
            from_currency = str(input("- Which currency is it? ")).strip().upper()
            to_currency = str(input("- Which currency do you want to convert it to? ")).strip().upper()

            if from_currency not in rates or to_currency not in rates:
                print(" ")
                print("Enter a valid currency!\n")

            else:
                break

    except ValueError:
        print("Enter a valid number!\n")   


# We just need a simple function for it all
def convert(amount, from_currency, to_currency, rates):    
        result = (amount / rates[from_currency]) * rates[to_currency] # AI's formula
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}\n")

        return result
        

# Then we call the function to let it work
convert(amount, from_currency, to_currency, rates)

