
# CURRENCY CONVERTER IN REAL TIME WITH INTERNET

# We need to install our libraries first and other things too
import requests
API_KEY = "e2f6ec04bf4dae03ad8061f4"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

response = requests.get("https://v6.exchangerate-api.com/v6/e2f6ec04bf4dae03ad8061f4/latest/USD")
print(response.json())