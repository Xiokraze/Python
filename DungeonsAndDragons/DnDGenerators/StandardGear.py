import Tables
import Input
import Text

class Menu:
    menu = [" 1) Simple Armor",
        " 2) Simple Weapons",
        " 3) Martial Weapons",
        " 4) All The Above",
        " 5) Back"]

def getOption():
    print(" What would you like to view?")
    print()
    numOptions = len(Menu.menu)
    option = Input.getIntegerInput(1, numOptions, Menu.menu)
    return option

def printArmor(armorTable):
    max = len(armorTable)
    tableEntries = 6
    typeWidth = 16
    costWidth = 10
    acWidth = 30
    strWidth = 8
    stealthWidth = 16
    weightWidth = 8
    count = 0
    textColorFlag = 1
    for i in range(max):
        if (textColorFlag == 1):
            print(Text.Color.yellow, end="")
        if (i % tableEntries == 0 and i != 0): 
            print()
        if (count == 0):
            print(armorTable[i].ljust(typeWidth), end="")
        elif(count == 1):
            print(armorTable[i].rjust(costWidth), end="")
        elif(count == 2):
            print(armorTable[i].center(acWidth), end="")
        elif(count == 3):
            print(armorTable[i].center(strWidth), end="")
        elif(count == 4):
            print(armorTable[i].center(stealthWidth), end="")
        else:
            print(armorTable[i].center(weightWidth), end="")
        count += 1
        if (textColorFlag == 1 and i == 5):
            textColorFlag = 0
            print(Text.Color.off, end="")
        if (count == 6):
            count = 0
    print()
    print()
    return

def printWeapons(weaponTable):
    max = len(weaponTable)
    tableEntries = 5
    typeWidth = 16
    costWidth = 10
    damageWidth = 30
    weightWidth = 8
    propertiesWidth = 16
    count = 0
    textColorFlag = 1
    for i in range(max):
        if (textColorFlag == 1):
            print(Text.Color.yellow, end="")
        if (i % tableEntries == 0 and i != 0): print()
        if (count == 0):
            print(weaponTable[i].ljust(typeWidth), end="")
        elif(count == 1):
            print(weaponTable[i].rjust(costWidth), end="")
        elif(count == 2):
            print(weaponTable[i].center(damageWidth), end="")
        elif(count == 3):
            print(weaponTable[i].center(weightWidth) + "    ", end="")
        else:
            print(weaponTable[i].ljust(propertiesWidth), end="")
        if (textColorFlag == 1 and i == 4):
            textColorFlag = 0
            print(Text.Color.off, end="")
        count += 1
        if (count == 5):
            count = 0
    print()
    print()
    return

def run():
    option = getOption()
    if (option == 1):
        printArmor(Tables.StandardArmor.lightArmor)
        printArmor(Tables.StandardArmor.mediumArmor)
        printArmor(Tables.StandardArmor.heavyArmor)
        printArmor(Tables.StandardArmor.shields)
    elif (option == 2):
        printWeapons(Tables.StandardWeapons.simpleMelee)
        printWeapons(Tables.StandardWeapons.simpleRange)
    elif (option == 3):
        printWeapons(Tables.StandardWeapons.martialMelee)      
        printWeapons(Tables.StandardWeapons.martialRange)
    elif (option  == 4):
        printArmor(Tables.StandardArmor.lightArmor)
        printArmor(Tables.StandardArmor.mediumArmor)
        printArmor(Tables.StandardArmor.heavyArmor)
        printArmor(Tables.StandardArmor.shields)
        printWeapons(Tables.StandardWeapons.simpleMelee)
        printWeapons(Tables.StandardWeapons.simpleRange)
        printWeapons(Tables.StandardWeapons.martialMelee)      
        printWeapons(Tables.StandardWeapons.martialRange)
    else:
        return
    return