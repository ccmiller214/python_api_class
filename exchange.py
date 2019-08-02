#!/usr/bin/python3

import requests
import json
import argparse

key = "LDLCS9364HNRRJEU"
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}'

def main():
    try:
        if args.curto: toCurr = args.curto
        else: toCurr = input("Enter currency to change to > ")
        if args.curfr: fromCurr = args.curfr
        else: fromCurr = input("Enter currency to change from > ")
        rate = requests.get(url.format(fromCurr,toCurr,key))
        rate_json = rate.json()["Realtime Currency Exchange Rate"]
        fromName = rate_json["2. From_Currency Name"]
        toName = rate_json["4. To_Currency Name"]
        exRate = rate_json["5. Exchange Rate"]
        print(f"\n{fromName} equals {float(exRate):.4f} {toName}\n")
    except:
        print("\nSomething went wrong! Please recheck currency abrreviations.\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--curfr', help="Currency to exchange from")
    parser.add_argument('--curto',help="Currency to exchange to")
    args = parser.parse_args()
    main()
    

