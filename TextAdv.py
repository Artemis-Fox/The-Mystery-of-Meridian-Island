import math, random
import time
import sys

GameLoop = True



class Room:
    def __init__(self, descrption, InRoom):
        self.descrption = descrption
        self.InRoom = False

class Tool:
    def __init__(self, name):
        self.name = name

class Text:
    def __init__(self, name, body):
        self.name = name
        self.body = body

Inventory = []


title = ("""
==================================================
        The Mystery of Meridian Island
==================================================
""")

for char in title:
    print(char, end="", flush=True)
    time.sleep(0.1)

StartGame = True
while StartGame == True:
    READY = ("Are you ready to brave Meridian Island? Y, N\n: ")
    for char in READY:
        print(char, end="", flush=True)
        time.sleep(0.1)

    StartScreen = input()

    if StartScreen == "y" or StartScreen == "Y":
        break
    elif StartScreen == "n" or StartScreen == "N":
        sys.exit("Then Begone with ye! and only return when you got the stones!")
    else:
        print("That was an incorrect input. try again!\n")
        continue


Name = input("Who are you?\n: ")
for char in Name:
    print(char, end="", flush=True)
    time.sleep(0.1)
print("\n")

while GameLoop == True:


    beach = Room("The Beach that you washed up on. debris can still be seen bobbing in the ocean",False)
    coast = Room("Further down the coast of the island. Maybe you can find a way off?", False)
    forest = Room("A forrest that encompassess the Majority of Meridian Island. What will you find in its heart?", False)
    temple = Room("The heart of Merridian Island", False)
    Hardwin = Tool("Hardwin")
    CoolStick = Tool("Cool Stick")

    beach.InRoom = True

    while beach.InRoom == True:

        print(Name + ", You wake up face down, the feel of sand on your face and the sound of the waves close by. \n Lifting yourself up, you are on a beach. Behind you the ocean stretches past the horizon with the remains of a ship bobbing up and down with the waves\n")
        print("You start to remember what happened, you where on that ship. It was a Carrack, a large vessle of 150 feet (45 meters) in length with a crew of 40 men. Her name was EV Pathfinder, and it seems you are the only surviver of her crash.\n")
        print("Suddenly, a voice calls out to you! looking in the direction you see a skull with a single golden tooth.\n")
        print("Looks like yer in a bit of a pickle matey. My names Hardwin and if you dont want to end up like me yer gonna need my help to escape.... \n")
        print("MERIDIAN ISLAND!\n")
        print("--Hardwin added to inventory--\n")
        Inventory.append(Hardwin)

        BeachChoice = input("What do you do now?\n 1. go into the woods\n 2. go down the coast\n 3. look around\n: ")

        if BeachChoice == "1":
            beach.InRoom = False
            forest.InRoom = True
            break
        elif BeachChoice == "2":
            beach.InRoom = False
            coast.InRoom = True
            break
        elif BeachChoice == "3":
            print(beach.descrption)
        else:
            print("gay")

    while beach.InRoom == False and forest.InRoom == True:
        print("You enter deeper into the forrest, the sounds of the waves slowly fade as the caws of birds and the chittering of bugs fill your ears. \n")
        print("you decide to pick up a cool stick you found along your way was you explore\n")
        print("---Cool Stick added to inventory!---\n")
        Inventory.append(CoolStick)
        print("After what feels like hours, you find yourself at the foot of an imposing structure. It must be some sort of temple, seems to be 9.. no 10 stories tall!\n")
        print("The Temple looks worn, weathered, like a hand me down leather coat.\n")
        print("Hardwin pipes up\n")
        print("I hope yer ready matey. once you go in there, no turning back.\n")

        ForrestChoice = input("what will you do now?\n 1. Go into the temple\n 2. Turn around\n 3.Description\n: ")

        if ForrestChoice == "1":
            forest.InRoom = False
            temple.InRoom = True
            break
        elif ForrestChoice == "2":
            forest.InRoom = False
            beach.InRoom = True
            break
        elif ForrestChoice == "3":
            print(forest.descrption)
        else:
            print("gay")
    
    while temple.InRoom == True:
        print("You climb the steps of the temple and reach a large locked door, a hole in the shape of a skull carved in it.\n")
        print("Told ya would need me! You feel like Hardwin would be giving you a smirk if he could\n")
        print("You place Hardwin in the spot\n")
        Inventory.remove(Hardwin)
        print("---Hardwin removed from inventory!---")
        print("Good luck matey, Hardwin give you one last look before his skull gets split in half as the door unlocks\n")
        print("A bright light erupts from the temple doors searing your eyes.")
