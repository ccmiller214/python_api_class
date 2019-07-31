#!/usr/bin/python3

import requests

url = 'http://api.open-notify.org/astros.json'
try:
    info = requests.get(url)

    with open("astros","a") as myfile:
        for people in info.json()['people']:
            myfile.write(people['name'] + '\n')
except:
    print("Something went wrong!")




