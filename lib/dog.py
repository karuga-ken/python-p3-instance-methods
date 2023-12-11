#!/usr/bin/env python3

class Dog:
    def __init__(self, bark, sit):
        self.bark = bark
        self.sit = sit
        
dog = Dog("Woof!", "The dog is sitting")
print(dog.bark)
print(dog.sit)

