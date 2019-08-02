#!/usr/bin/python3

import time
mystring = ("GMO-Free Grass Fed Human Time - " + time.ctime())
print(mystring)

with open("mycrontime.log",'a') as myfile:
    myfile.write(mystring + "\n")
