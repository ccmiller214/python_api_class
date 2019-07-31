#!/usr/bin/python3

## Loop until works
while True:
    try:
        ## Pull info from the local user
        name = input('Enter a file name: ')
        with open(name,'w') as myfile:
            myfile.write('Well done\n')
    except:
        print('Error in creating that file...try again!')
    else:
        print('File created successfully!')
        break
