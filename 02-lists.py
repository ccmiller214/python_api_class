#!/usr/bin/python3

def main():
    mylist = ['cisco','juniper','bigip','tellabs','meraki']

    print(mylist[2])

    mylist.append('nortel')

    print(mylist[-1])

    mylist.extend(['genband','lucent'])

    print(mylist)

    zcloud = ['aws','openstack','google','azure']

    mylist.extend(zcloud)

    print(mylist)
    
main()
