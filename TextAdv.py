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


NAME = ("Who are you?\n: ")
for char in NAME:
    print(char, end="", flush=True)
    time.sleep(0.1)
Name = input()
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

        BeachText = (Name + """, you find yourself face first in the sand. The sounds of waves crashing crashing on the shore fill your ears.\n You pick yourself up, behind you see the wreckage of your ship. The wreckage bobs up and down in the water, it seems you are the only survivor.\n *Ah, seems we've got a live un here.* The voice comes from near by, but looking around there is no obvious source. *I'm over here ya nitwit*\n Following the voice you find the source, a skull wearing an ipatch and a bandana. *So yer eyes do work, I'm Hardwin. Welcome to Merridian Island, a horror ridden pox of an island. If you want to srvive matey, you'll need my help. plus it gets me off the island as well, its a win win!*\n You could almost sense a sly smile from Hardwin as he said that.\n ---Hardwin Added to inventory---\n""")
        for char in BeachText:
            print(char, end="", flush=True)
            time.sleep(0.1)

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
        ForrestText = ("""As you enter the forrest the sounds of the beach slowly fade behind you, replaced by the chitter of insects and the caws of birds.\n *Be careful here lad*\n You continue to sneak your way through the forrest. You hear things like the breaking of branches and maybe even some growls. but you're lucky it seems what ever in the forrest didn't see you, or at least didn't think you would taste good. \n eventually after what feels like hours of trudging through the forrest. You find yourself at the steps of a temple. It's crumbling visage belies how ancient this place truly is.\n It's huge, must be over 8 stories tall at least. and who knows how deep it goes underground?""")

    for char in ForrestText:
        print(char, end="", flush=True)
        time.sleep(0.1)

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
