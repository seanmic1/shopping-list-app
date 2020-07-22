thing = []
slist = []
number = 0
print("Type in your shopping list item, press enter to add to the list. \nType \"done\" when you are finished\nIf you want to remove an item, type \"rem\" and the item name to remove it.")
while thing != "done":
    thing = input()
    try:
        if thing.startswith("rem"):
            thing = thing.replace("rem","").strip()
            slist.remove(thing)
            print("Removed",thing)
        else:
            slist.append(thing.strip())
            print("Added",thing)
    except:
        print("Make sure you spell the item correctly!")
slist.remove("done")
print("Your shopping list items are:")
for item in slist:
    number = number + 1
    print(number, ". ", item, sep = "")

    
