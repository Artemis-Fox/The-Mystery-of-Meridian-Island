import math, random
import time
import sys

GameLoop = True



class Room:
    def __init__(self, name, actions, description, InRoom):
        self.name = name
        self.actions = []
        self.description = description
        self.InRoom = False
class Tool:
    def __init__(self, name):
        self.name = name


Inventory = []


print(""" 
==================================================
        The Mystery of Meridian Island
==================================================
""")

StartGame = True
while StartGame == True:
    StartScreen = input("Are you ready to brave Meridian Island? Y, N\n")

    if StartScreen == "y" or StartScreen == "Y":
        break
    elif StartScreen == "n" or StartScreen == "N":
        sys.exit("Then Begone with ye! and only return when you got the stones!")
    else:
        continue

while GameLoop == True:


    Name = input("Who are you?: \n")
    print("\n:")

    beach = Room("Beach", ["1", "2", "3"], "A beach that you washed up on", True)
    Hardwin = Tool("Hardwin")

    while beach.InRoom == True:
        print(Name + ", You wake up face down, the feel of sand on your face and the sound of the waves close by. \n Lifting yourself up, you are on a beach. Behind you the ocean stretches past the horizon with the remains of a ship bobbing up and down with the waves\n")
        print("You start to remember what happened, you where on that ship. It was a Carrack, a large vessle of 150 feet (45 meters) in length with a crew of 40 men. Her name was EV Pathfinder, and it seems you are the only surviver of her crash.\n")
        print("Suddenly, a voice calls out to you! looking in the direction you see a skull with a single golden tooth.\n")
        print("Looks like yer in a bit of a pickle lad. My names Hardwin and if you dont want to end up like me yer gonna need my help to escape.... \n")
        print("MERIDIAN ISLAND!\n\n")
