#initializing variables
run = True
thing = []
slist = []
number = 0
item = ""

#adding and removing items
print("""To add an item, type the name of your item and press enter.
To remove an item, type \"remove\", a space, and the name of the item to be removed then press enter.
To finish, type \"done\" and press enter.
To see your list, type \"list\" and press enter.""")
while run == True:
    thing = input().strip()
    try:
        if thing =="done":
            break
        elif thing.startswith("remove"):
            thing = thing.replace("remove","").strip()
            slist.remove(thing)
            print("Removed",thing)
        elif thing in slist:
            print("You already listed that item!")
        elif thing == "list":
            print("Your shopping list items are:")
            for item in slist:
                number = number + 1
                print(number, ". ", item, sep = "")
        elif thing == "":
            print("You can't add nothing!")
        else:
            slist.append(thing)
            print("Added",thing)
    except:
        print("Make sure the item is in the list or is spelled correctly!")

#lists out all your items and numbers them
print("Your shopping list items are:")
for item in slist:
    number = number + 1
    print(number, ". ", item, sep = "")

#asks if you want to make a new file of the list
print("Would you like to make a text file of your list? (y/n)")
while run == True:
    prq = input()
    if prq == "y":
        number = 1
        print("What would you like to name the file?")
        filename = input()
        newfile = open("%s.txt" % (filename),"w+")
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


    
