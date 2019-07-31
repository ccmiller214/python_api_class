#!/usr/bin/python3

import requests

url = "https://www.anapioficeandfire.com/api/houses?page=1&pageSize=10"
try:
    info = requests.get(url)
    for house in info.json():
        print('-----------------------------')
        print('{} : {}\n{}\n'.format(house['name'],house['region'],house['coatOfArms']))
#        print(house['overlord'])
        try:
            lord = requests.get(house['overlord'])
            print(lord.json()['name'])
        except Exception as err:
            print('House has no overlord')

except:
    print("Something went wrong!")




