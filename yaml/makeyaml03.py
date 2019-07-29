#!/usr/bin/python3
#python -m pip install pyyaml
import yaml
import json

def main():
    ## Create a blob of data to work with
    with open("galaxyguide.yaml") as galaxy:
        pyyammy = yaml.load(galaxy)
    
    print(pyyammy)
    
    pyyammy.append({"name":"Christian Miller","species":"Human"})

    print(pyyammy)

    with open("galaxyguide.json","w") as galaxyjson:
        json.dump(pyyammy,galaxyjson)

main()
