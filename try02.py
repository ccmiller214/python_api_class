#!/usr/bin/python3

import sys

## Start with our infinite loop
while True:
    try:
        z = 'successful job.'
        print("Let's divide x by y!")
        x = int(input("What is the integer value of x? "))
        y = int(input("What is the integer value of y? "))
        print("The value of x/y: ", x/y)
    except ZeroDivisionError as err:
        print("Handling of a run time error: ", err)
        z = "Error div by zero"
    except ValueError as err:
        z = "Value Error detected via user input."
    except KeyboardInterrupt: break
    except:
        print("Oh wow. We did not produce code to handle this type of error yet.")
        print(sys.exc_info()[0])
        z = sys.exc_info()[0]
        #raise
    finally:
        with open("try02.log", "a") as log:
            log.write(z + '\n')
    
