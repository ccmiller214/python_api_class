#!/usr/bin/python3

class Dog:  
    def __init__(self,name,age):
        self.n = name
        self.a = age

    def __str__(self):
        return 'Name: ' + self.n + ' Age: ' + str(self.a)

    def aged(self, yearsolder):
        self.a = self.a + yearsolder

## Inheritance
class Jackrussell(Dog):
    def __init__(self,name,age,isWirehair,isHunter):
        Dog.__init__(self,name,age)
        self.wh = isWirehair
        self.h = isHunter

    def __str__(self):
        retStr = Dog.__str__(self)
        retStr += ' Wirehaired: ' + str(self.wh) + ' Trained to Hunt:  ' \
                + str(self.h)
        return retStr
    
    def traintohunt(self,zbool):
        self.h = zbool

def main():
    mutt = Dog("DerpyDoge",3)
    print(mutt)
    print('now let us age DerpyDoge')
    mutt.aged(2)
    print(mutt)

    eddie = Jackrussell('Eddie',4,False,False)
    print(eddie)

    eddie.aged(3)
    print(eddie)

    eddie.traintohunt(True)
    print(eddie)

if __name__ == "__main__":
    main()
