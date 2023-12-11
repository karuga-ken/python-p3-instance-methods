#!/usr/bin/env python3

class Person:
    # Class body goes here
    def __init__(self, talk, walk, dance):
       self.talk = talk
       self.walk = walk
       self.dance = dance

    #Instance method definition
user = Person("Hello World!", "The person is walking", "The person is dancing")
print(user.talk)
print(user.walk)
print(user.dance)