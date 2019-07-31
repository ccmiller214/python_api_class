#!/usr/bin/python3

import argparse
import time
import hashlib
import requests

XAVIER = 'https://gateway.marvel.com/v1/public/characters'

def hashbuilder(timestone,beast,storm):
    return hashlib.md5((timestone+beast+storm).encode('utf-8')).hexdigest()

def marvelcharcall(timestone,storm,cerebro,lookmeup):
#    deadpool = requests.get(XAVIER + "?name=" + lookmeup + "&ts=" + timestone + "&apikey=" + storm \
#            + "&hash=" + cerebro)
    deadpool = requests.get(XAVIER + '/' + lookmeup + "?series=" + "&ts=" + timestone + "&apikey=" + storm \
            + "&hash=" + cerebro)
    return deadpool.json()

def main():

    ## harvest our private key
    with open(args.dev) as mccoy:
        beast = mccoy.read().rstrip('\n')

    ## harvest our pub key
    with open(args.pub) as monroe:
        storm = monroe.read().rstrip('\n')

    ## Create a RAND by grabbing the current time
    timestone = str(time.time()).rstrip('.')

    ## Grab a 1 time use hash 
    cerebro = hashbuilder(timestone,beast,storm)

#    uncannyxmen = marvelcharcall(timestone,storm,cerebro,"Wolverine")
    uncannyxmen = marvelcharcall(timestone,storm,cerebro,"1009351")
    print(uncannyxmen['data']['results'][0]['stories']['items'][0].values())
#    print(uncannyxmen['data']['results'][0]['id'])
#    print(uncannyxmen['data']['results'][0]['name'])
#    print(uncannyxmen['data']['results'][0]['description'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', help="Provide the /path/to/file.priv containing the Marvel private dev key")
    parser.add_argument('--pub', help="Provide the /path/to/file.pub containing the marvel public key")
    args = parser.parse_args()
    main()

