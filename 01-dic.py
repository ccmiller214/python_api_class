#!/usr/bin/python3

def main():
    hostipdict = {'host01':'10.0.0.2','host02':'192.168.70.1','host03':'8.8.8.8'}

    print(hostipdict['host02'])

    hostipdict['host04'] = '172.0.0.1'

    print(hostipdict)

    hostipdict.update({'host05':'9.9.9.9'})

    print(hostipdict)

    print(hostipdict.get('host66'))

    hostipdict.keys()

    print(hostipdict.values())

main()
