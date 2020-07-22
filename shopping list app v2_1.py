#importing modules
import tkinter as tk

#initializing variables
run = True
thing = []
slist = []
number = 0

#adding and removing items, checks if loop is done as well
print("Type an item and press enter to add it to the list. \nType \"done\" when you are finished.\nIf you want to remove an item, type \"remove\", a space, and the name of the item to be removed.")
while run == True:
    thing = input()
    try:
        if thing =="done":
            break
        elif thing.startswith("remove"):
            thing = thing.replace("remove","").strip()
            slist.remove(thing)
            print("Removed",thing)
        else:
            slist.append(thing.strip())
            print("Added",thing)
    except:
        print("Make sure the item is in the list or is spelled correctly!")

#lists out all your items and numbers them
print("Your shopping list items are:")
for item in slist:
    number = number + 1
    print(number, ". ", item, sep = "")

#asks if you want to make a new file of the lis
print("Would you like to make a text file of your list? (y/n)")
while run == True:
    prq = input()
    if prq == "y":
        number = 1
        newfile = open("yourlist.txt","w+")
        for listitem in slist:
            newfile.write("%d. %s\n" % (number,listitem))
            number = number + 1
        newfile.close()
        print("Made new file")
        quit()
    elif prq == "n":
        print("Bye bye")
        quit()
    else:
        print("Please type y or n only")


    
