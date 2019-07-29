#!/usr/bin/python3
import json

def main():
    with open("datacenter.json", "r") as datacenter:
        datacenterstring = datacenter.read()
    
    ## Display our decoded string
    print(datacenterstring)
    print(type(datacenterstring))
    print("\nThe code above is string data.  Pythong cannot easily work with this data.")
    input("Press Enter to continue\n")

    ## Create a JSON object(datacenterdecoded) from the JSON string (datacenterstring)
    datacenterdecoded = json.loads(datacenterstring)

    ## This is now a dictionary
    print(type(datacenterdecoded))

    ## Display the servers in row3
    print(datacenterdecoded["row3"])

    ## Display the 2nd server in row2
    print(datacenterdecoded["row2"][0])

    ## Display the last server in row3
    print(datacenterdecoded["row3"][-1])


main()
