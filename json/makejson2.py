#!/usr/bin/python3
import json

def main():
    ## Create a blob of data to work with
    hitchhikers = [{"name":"Zaphod Beeblebrox","species":"Betelgeusian"},\
            {"name":"Arthur Dent","species":"Human"}]

    ## Display our Python data (a list containing two dictionaries)
    print(hitchhikers)

    ## Create the JSON string
    jsonstring = json.dumps(hitchhikers)

    ## Display a singel string of JSON
    print(jsonstring)

    print(type(hitchhikers))
    print(type(jsonstring))

main()
