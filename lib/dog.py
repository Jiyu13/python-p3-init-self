#!/usr/bin/env python3

class Dog:
    # initialise the class
    def __init__(self, name, favorite_toy="Any"):
        self.name = name
        self.favorite_toy = favorite_toy

    
    def bark(self):
        print("Woof!")


    def showing_self(self):
        return self

    def get_adpoted(self, owner_name):
        self.owner = owner_name
    

fido = Dog("Fido")
fido.name    # Fido
print(fido.showing_self())  # <__main__.Dog object at 0x7f49a9a4f7c0>

# set fido owner attritube
fido.get_adpoted("Sophie")
print(fido.owner)   # Sophie

fido.favorite_toy # Any


snoopy = Dog("Snoopy", "Tennis Ball")
snoopy.name
snoopy.favorite_toy # Tennis Ball