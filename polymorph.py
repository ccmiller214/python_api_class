#!/usr/bin/python3

class Bear(object):
    def sound(self):
        print("Goarrr")

class Dog(object):
    def sound(self):
        print("Woof woof!")

def makeSound(animalType):
    animalType.sound()

bearObj = Bear()

dogObj = Dog()

makeSound(bearObj)

makeSound(dogObj)

