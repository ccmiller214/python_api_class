#!/usr/bin/python3
#python -m pip install pyyaml
import yaml

def main():
    ## Create a blob of data to work with
    hitchhikers =[{"name":"Zaphod Beeblebrox","species":"Betelgeusian"}, \
            {"name":"Arthur Dent","species":"Human"}]

    ## Display our Python data (a list containing two dictionaries
    print(hitchhikers)

    ## Open a new file in write mode

    ## Use the YAML library
    ## USAGE: yaml.dump(input data, file like object)
    ## unlike JSON, the YAML lib uses .dump() to create YAML strings and write to files
    ## the JSON lib uses .dump() to create a string and .dumps() to write to files
    yamlstring = yaml.dump(hitchhikers)

    print(yamlstring)

main()
