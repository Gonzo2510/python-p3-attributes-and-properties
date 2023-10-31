#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
] 

class Dog:
    def __init__(self, name = 'Mutt', breed="Pointer"):

        if type(name) != str:
            print("Name must be string between 1 and 25 characters.")
        elif 1 < len(name) < 25:
            self.name = name
        else:
            print("Name must be string between 1 and 25 characters.")
        
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self.breed = breed

