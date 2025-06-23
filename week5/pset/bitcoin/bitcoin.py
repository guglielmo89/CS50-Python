import sys
import requests
import json

def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    
    try:
        number = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=483debab9ca5434909b099d5e167153594f7901b5839e29175fd51a9b2ab93ab")
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Request Error")
    
    try:
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except (KeyError, TypeError, ValueError):
        sys.exit("Error parsing price data")

    amount = price * number    
    print(f"${amount:,.4f}")

if __name__ == "__main__":
    main()