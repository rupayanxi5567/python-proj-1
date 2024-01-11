import requests

API_KEY = "fca_live_cdvIOwD3wpJKS5Jgv1nqxr66k4uDToVOeLbIxHoa"

BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD","CAD","AUD","INR"]
currencies = ",".join(CURRENCIES)

def convert_currency(base):
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"


    try:
        response = requests.get(url) 
        data = response.json()
        return data
    except:
        print("Invalid Currency")
        return None

while True:
    base = input("Enter the currency to conver, (q to quit) ").upper()    

    if base == "Q":
        break;
    else:
        data = convert_currency(base)
        if not data:
            continue;


        # del data[base]
        for ticker, value in data.items():
            print(f"{ticker}: {value}")