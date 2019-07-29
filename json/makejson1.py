#!/usr/bin/python3
import json

def main():
    ## Create a blob of data to work with
    hitchhikers = [{"name":"Zaphod Beeblebrox","species":"Betelgeusian"},\
            {"name":"Arthur Dent","species":"Human"}]

    ## Display our Python data (a list containing two dictionaries)
    print(hitchhikers)

    ## Open a new file in write mode
#    myfile = open('galaxyguide.json','w')
    ## Use the JSON library
    ## USAGE:  json.dump(input data, file like object) ##
#    json.dump(hitchhikers, myfile)
    ## Close the file when we are done
#    myfile.close()


    with open("galaxyguide.json","w") as myfile:  ## Includes closing the file
        json.dump(hitchhikers,myfile)

main()
