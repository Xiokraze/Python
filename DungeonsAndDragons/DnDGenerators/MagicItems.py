import random
import Dice
import Text
import Tables

class Variables:                                                # Variables for tracking the magic item tables based on integer values
    TableA = 1
    TableB = 2
    TableC = 3
    TableD = 4
    TableE = 5
    TableF = 6
    TableG = 7
    TableH = 8
    TableI = 9

def getLevelSpell(spellLevel):                                  # Randomly selects and returns a spell of the requested level
    if (spellLevel == 0):                                       # If the spell is level 0
        numCantrips = len(Tables.Spells.cantrips)               # Get the total number of cantrips     
        cantrip = random.randint(0, numCantrips - 1)            # Generate a random number between 0 and the cantrip total - 1
        return Tables.Spells.cantrips[cantrip]                  # Return the cantrip at the generated location in the cantrip table

    elif (spellLevel == 1):                                     # If the spell is level 1
        numSpells = len(Tables.Spells.level1Spells)             # Get the total number of level 1 spells
        spell = random.randint(0, numSpells - 1)                # Generate a random number between 0 and the level 1 spell total - 1
        return Tables.Spells.level1Spells[spell]                # Return the spell at the generated location in the level 1 spell table

    elif (spellLevel == 2):                                     # If the spell is level 2
        numSpells = len(Tables.Spells.level2Spells)             # Get the total number of level 2 spells
        spell = random.randint(0, numSpells - 1)                # Generate a random number between 0 and the level 2 spell total - 1
        return Tables.Spells.level2Spells[spell]                # Return the spell at the generated location in the level 2 spell table

    elif (spellLevel == 3):                                     # If the spell is level 3
        numSpells = len(Tables.Spells.level3Spells)             # Get the total number of level 3 spells
        spell = random.randint(0, numSpells - 1)                # Generate a random number between 0 and the level 3 spell total - 1
        return Tables.Spells.level3Spells[spell]                # Return the spell at the generated location in the level 3 spell table

    elif (spellLevel == 4):                                     # If the spell is level 4
        numSpells = len(Tables.Spells.level4Spells)             # Get the total number of level 4 spells
        spell = random.randint(0, numSpells - 1)                # Generate a random number between 0 and the level 4 spell total - 1
        return Tables.Spells.level4Spells[spell]                # Return the spell at the generated location in the level 4 spell table

    elif (spellLevel == 5):
        numSpells = len(Tables.Spells.level5Spells)             # Get the total number of level 5 spells
        spell = random.randint(0, numSpells - 1)                # Generate a random number between 0 and the level 5 spell total - 1
        return Tables.Spells.level5Spells[spell]                # Return the spell at the generated location in the level 5 spell table

    elif (spellLevel == 6):
        numSpells = len(Tables.Spells.level6Spells)             # Get the total number of level 6 spells
        spell = random.randint(0, numSpells - 1)                # Generate a random number between 0 and the level 6 spell total - 1
        return Tables.Spells.level6Spells[spell]                # Return the spell at the generated location in the level 6 spell table

    elif (spellLevel == 7):
        numSpells = len(Tables.Spells.level7Spells)             # Get the total number of level 7 spells
        spell = random.randint(0, numSpells - 1)                # Generate a random number between 0 and the level 7 spell total - 1
        return Tables.Spells.level7Spells[spell]                # Return the spell at the generated location in the level 7 spell table

    elif (spellLevel == 8):
        numSpells = len(Tables.Spells.level8Spells)             # Get the total number of level 8 spells
        spell = random.randint(0, numSpells - 1)                # Generate a random number between 0 and the level 8 spell total - 1
        return Tables.Spells.level8Spells[spell]                # Return the spell at the generated location in the level 8 spell table

    elif (spellLevel == 9):
        numSpells = len(Tables.Spells.level9Spells)             # Get the total number of level 9 spells
        spell = random.randint(0, numSpells - 1)                # Generate a random number between 0 and the level 9 spell total - 1
        return Tables.Spells.level9Spells[spell]                # Return the spell at the generated location in the level 9 spell table

    return " "                                                   # Redundant return catch, return an empty string

def getDescription(table, i):                                   # Returns a spell based on the provided table and array position
    if (table == Variables.TableA):                             # If looking at table A
        if (i == 1):                                            # If the item is tableA[1] (spell scroll cantrip)
            return getLevelSpell(0)                             # Return a level 0 spell
        elif (i == 3):                                          # If the item is tableA[3] (1st level scroll)
            return getLevelSpell(1)                             # Return a 1st level spell
        elif (i == 4):                                          # If the item is tableA[4] (2nd level scroll)
            return getLevelSpell(2)                             # Return a 2nd level spell
    
    elif (table == Variables.TableB):                           # If looking at table B
        if (i == 8):                                            # If the item is tableB[8] (2nd level scroll)
            return getLevelSpell(2)                             # Return a 2nd level spell
        elif (i == 9):                                          # If the item is tableB[9] (3rd level scroll)
            return getLevelSpell(3)                             # Return a 3rd level spell
    
    elif (table == Variables.TableC):                           # If looking at table C
        if (i == 1):                                            # If the item is tableC[1] (4th level scroll)
            return getLevelSpell(4)                             # Return a 4th level spell
        elif (i == 11):                                         # If the item is tableC[11] (5th level scroll)
            return getLevelSpell(5)                             # Return a 5th level spell
    
    elif (table == Variables.TableD):                           # If looking at table D
        if (i == 3):                                            # If the item is tableD[3] (6th level scroll)
            return getLevelSpell(6)                             # Return a 6th level spell
        elif (i == 4):                                          # If the item is tableD[4] (7th level scroll)                              
            return getLevelSpell(7)                             # Return a 7th level spell
        elif (i == 11):                                         # If the item is tableD[4] (8th level scroll)
            return getLevelSpell(8)                             # Return a 8th level spell
    
    elif (table == Variables.TableE):                           # If looking at table E
        if (i == 0):                                            # If the item is tableE[0] (8th level scroll)
            return getLevelSpell(8)                             # Return a 8th level spell
        elif (i == 3):                                          # If the item is tableE[3] (9th level scroll)
            return getLevelSpell(9)                             # Return a 9th level spell
    
    # Table F has no special conditions                         # Table F has no special conditions

    elif (table == Variables.TableG):                           # If looking at table G 
        if (i == 1):                                            # If the item is tableG[1] (figurine of wonderous power)
            numFigurines = len(Tables.MagicItems.figurines)     # Get the number of figurines in the magic items figurine table
            figurine = random.randint(0, numFigurines - 1)      # Get a random figurine                   
            return Tables.MagicItems.figurines[figurine]        # Return the figurine

    # Table H has no special conditions                         # Table H has no special conditions

    elif (table == Variables.TableI):                           # If looking at table I
        if (i == 28):                                           # If the item is tableI[28] (magic armor)
            numMagicArmor = len(Tables.MagicItems.magicArmor)   # Get the number of magic armor types in the magic armor table
            magicArmor = random.randint(0, numMagicArmor - 1)   # Get a random piece of magic armor
            return Tables.MagicItems.magicArmor[magicArmor]     # Return the magic armor

    return " "                                                  # If the item is not a spell scroll or special item, return a " " for printing

def getMagicalItem(table):
    # This function rolls a d100, then, depending on the 
    # parameters of the corresponding table, returns an 
    # integer value that represents the table's array 
    # location for the roll.

    d100Value = Dice.Roll.d100()
    if (table == Variables.TableA):
        if (d100Value >= 1 and d100Value <= 50): return 0
        elif (d100Value >= 51 and d100Value <= 60): return 1
        elif (d100Value >= 61 and d100Value <= 70): return 2
        elif (d100Value >= 71 and d100Value <= 90): return 3
        elif (d100Value >= 91 and d100Value <= 94): return 4
        elif (d100Value >= 95 and d100Value <= 98): return 5
        elif (d100Value == 99): return 6
        else: return 7

    elif(table == Variables.TableB):
        if (d100Value <= 1 and d100Value <= 15): return 0
        elif (d100Value <= 16 and d100Value <= 22): return 1
        elif (d100Value <= 23 and d100Value <= 29): return 2
        elif (d100Value <= 30 and d100Value <= 34): return 3
        elif (d100Value <= 35 and d100Value <= 39): return 4
        elif (d100Value <= 40 and d100Value <= 44): return 5
        elif (d100Value <= 45 and d100Value <= 49): return 6
        elif (d100Value <= 50 and d100Value <= 54): return 7
        elif (d100Value <= 55 and d100Value <= 59): return 8
        elif (d100Value <= 60 and d100Value <= 64): return 9
        elif (d100Value <= 65 and d100Value <= 67): return 10
        elif (d100Value <= 68 and d100Value <= 70): return 11
        elif (d100Value <= 71 and d100Value <= 73): return 12
        elif (d100Value == 74 or d100Value == 75): return 13
        elif (d100Value == 76 or d100Value == 77): return 14
        elif (d100Value == 78 or d100Value == 79): return 15
        elif (d100Value == 80 or d100Value == 81): return 16
        elif (d100Value == 82 or d100Value == 83): return 17
        elif (d100Value == 84): return 18
        elif (d100Value == 85): return 19
        elif (d100Value == 86): return 20
        elif (d100Value == 87): return 21
        elif (d100Value == 88): return 22
        elif (d100Value == 89): return 23
        elif (d100Value == 90): return 24
        elif (d100Value == 91): return 25
        elif (d100Value == 92): return 26
        elif (d100Value == 93): return 27
        elif (d100Value == 94): return 28
        elif (d100Value == 95): return 29
        elif (d100Value == 96): return 30
        elif (d100Value == 97): return 31
        elif (d100Value == 98): return 32
        elif (d100Value == 99): return 33
        else: return 34

    elif(table == Variables.TableC):
        if (d100Value >= 1 and d100Value <= 15): return 0
        elif (d100Value >= 16 and d100Value <= 22): return 1
        elif (d100Value >= 23 and d100Value <= 27): return 2
        elif (d100Value >= 28 and d100Value <= 32): return 3
        elif (d100Value >= 33 and d100Value <= 37): return 4
        elif (d100Value >= 38 and d100Value <= 42): return 5
        elif (d100Value >= 43 and d100Value <= 47): return 6
        elif (d100Value >= 48 and d100Value <= 52): return 7
        elif (d100Value >= 53 and d100Value <= 57): return 8
        elif (d100Value >= 58 and d100Value <= 62): return 9
        elif (d100Value >= 63 and d100Value <= 67): return 10 
        elif (d100Value >= 68 and d100Value <= 72): return 11
        elif (d100Value >= 73 and d100Value <= 75): return 12
        elif (d100Value >= 76 and d100Value <= 78): return 13
        elif (d100Value >= 79 and d100Value <= 81): return 14
        elif (d100Value >= 82 and d100Value <= 84): return 15
        elif (d100Value >= 85 and d100Value <= 87): return 16
        elif (d100Value == 88 or d100Value == 89): return 17
        elif (d100Value == 90 or d100Value == 91): return 18
        elif (d100Value == 92): return 19
        elif (d100Value == 93): return 20
        elif (d100Value == 94): return 21
        elif (d100Value == 95): return 22
        elif (d100Value == 96): return 23
        elif (d100Value == 97): return 24
        elif (d100Value == 98): return 25
        elif (d100Value == 99): return 26
        else: return 27

    elif(table == Variables.TableD):
        if (d100Value >= 1 and d100Value <= 20): return 0
        elif (d100Value >= 21 and d100Value <= 30): return 1
        elif (d100Value >= 31 and d100Value <= 40): return 2
        elif (d100Value >= 41 and d100Value <= 50): return 3
        elif (d100Value >= 51 and d100Value <= 57): return 4
        elif (d100Value >= 58 and d100Value <= 62): return 5
        elif (d100Value >= 63 and d100Value <= 67): return 6
        elif (d100Value >= 68 and d100Value <= 72): return 7
        elif (d100Value >= 73 and d100Value <= 77): return 8
        elif (d100Value >= 78 and d100Value <= 82): return 9
        elif (d100Value >= 83 and d100Value <= 87): return 10
        elif (d100Value >= 88 and d100Value <= 92): return 11
        elif (d100Value >= 93 and d100Value <= 95): return 12
        elif (d100Value >= 96 and d100Value <= 98): return 13
        elif (d100Value == 99): return 14
        else: return 15        

    elif(table == Variables.TableE):
        if (d100Value >= 1 and d100Value <= 30): return 0
        elif (d100Value >= 31 and d100Value <= 55): return 1
        elif (d100Value >= 56 and d100Value <= 70): return 2
        elif (d100Value >= 71 and d100Value <= 85): return 3
        elif (d100Value >= 86 and d100Value <= 93): return 4
        elif (d100Value >= 94 and d100Value <= 98): return 5
        else: return 6

    elif(table == Variables.TableF):
        if (d100Value >= 1 and d100Value <= 15): return 0
        elif (d100Value >= 16 and d100Value <= 18): return 1
        elif (d100Value >= 19 and d100Value <= 21): return 2
        elif (d100Value == 22 or d100Value == 23): return 3
        elif (d100Value == 24 or d100Value == 25): return 4
        elif (d100Value == 26 or d100Value == 27): return 5
        elif (d100Value == 28 or d100Value == 29): return 6
        elif (d100Value == 30 or d100Value == 31): return 7
        elif (d100Value == 32 or d100Value == 33): return 8
        elif (d100Value == 34 or d100Value == 35): return 9
        elif (d100Value == 36 or d100Value == 37): return 10
        elif (d100Value == 38 or d100Value == 39): return 11
        elif (d100Value == 40 or d100Value == 41): return 12
        elif (d100Value == 42 or d100Value == 43): return 13
        elif (d100Value == 44 or d100Value == 45): return 14
        elif (d100Value == 46 or d100Value == 47): return 15
        elif (d100Value == 48 or d100Value == 49): return 16
        elif (d100Value == 50 or d100Value == 51): return 17
        elif (d100Value == 52 or d100Value == 53): return 18
        elif (d100Value == 54 or d100Value == 55): return 19
        elif (d100Value == 56 or d100Value == 57): return 20
        elif (d100Value == 58 or d100Value == 59): return 21
        elif (d100Value == 60 or d100Value == 61): return 22
        elif (d100Value == 62 or d100Value == 63): return 23
        elif (d100Value == 64 or d100Value == 65): return 24
        elif (d100Value == 66): return 25
        elif (d100Value == 67): return 26
        elif (d100Value == 68): return 27
        elif (d100Value == 69): return 28
        elif (d100Value == 70): return 29
        elif (d100Value == 71): return 30
        elif (d100Value == 72): return 31
        elif (d100Value == 73): return 32
        elif (d100Value == 74): return 33
        elif (d100Value == 75): return 34
        elif (d100Value == 76): return 35
        elif (d100Value == 77): return 36
        elif (d100Value == 78): return 37
        elif (d100Value == 79): return 38
        elif (d100Value == 80): return 39
        elif (d100Value == 81): return 40
        elif (d100Value == 82): return 41
        elif (d100Value == 83): return 42
        elif (d100Value == 84): return 43
        elif (d100Value == 85): return 44
        elif (d100Value == 86): return 45
        elif (d100Value == 87): return 46
        elif (d100Value == 88): return 47
        elif (d100Value == 89): return 48
        elif (d100Value == 90): return 49
        elif (d100Value == 91): return 50
        elif (d100Value == 92): return 51
        elif (d100Value == 93): return 52
        elif (d100Value == 94): return 53
        elif (d100Value == 95): return 54
        elif (d100Value == 96): return 55
        elif (d100Value == 97): return 56
        elif (d100Value == 98): return 57
        elif (d100Value == 99): return 58
        else: return 59

    elif (table == Variables.TableG):
        if (d100Value >= 1 and d100Value <= 11): return 0
        elif (d100Value >= 12 and d100Value <= 14): return 1
        elif (d100Value == 15): return 2
        elif (d100Value == 16): return 3
        elif (d100Value == 17): return 4
        elif (d100Value == 18): return 5
        elif (d100Value == 19): return 6
        elif (d100Value == 20): return 7
        elif (d100Value == 21): return 8
        elif (d100Value == 22): return 9
        elif (d100Value == 23): return 10
        elif (d100Value == 24): return 11
        elif (d100Value == 25): return 12
        elif (d100Value == 26): return 13
        elif (d100Value == 27): return 14
        elif (d100Value == 28): return 15
        elif (d100Value == 29): return 16
        elif (d100Value == 30): return 17
        elif (d100Value == 31): return 18
        elif (d100Value == 32): return 19
        elif (d100Value == 33): return 20
        elif (d100Value == 34): return 21
        elif (d100Value == 35): return 22
        elif (d100Value == 36): return 23
        elif (d100Value == 37): return 24
        elif (d100Value == 38): return 25
        elif (d100Value == 39): return 26
        elif (d100Value == 40): return 27
        elif (d100Value == 41): return 28
        elif (d100Value == 42): return 29
        elif (d100Value == 43): return 30
        elif (d100Value == 44): return 31
        elif (d100Value == 45): return 32
        elif (d100Value == 46): return 33
        elif (d100Value == 47): return 34
        elif (d100Value == 48): return 35
        elif (d100Value == 49): return 36
        elif (d100Value == 50): return 37
        elif (d100Value == 51): return 38
        elif (d100Value == 52): return 39
        elif (d100Value == 53): return 40
        elif (d100Value == 54): return 41
        elif (d100Value == 55): return 42
        elif (d100Value == 56): return 43
        elif (d100Value == 57): return 44
        elif (d100Value == 58): return 45
        elif (d100Value == 59): return 46
        elif (d100Value == 60): return 47
        elif (d100Value == 61): return 48
        elif (d100Value == 62): return 49
        elif (d100Value == 63): return 50
        elif (d100Value == 64): return 51
        elif (d100Value == 65): return 52
        elif (d100Value == 66): return 53
        elif (d100Value == 67): return 54
        elif (d100Value == 68): return 55
        elif (d100Value == 69): return 56
        elif (d100Value == 70): return 57
        elif (d100Value == 71): return 58
        elif (d100Value == 72): return 59
        elif (d100Value == 73): return 60
        elif (d100Value == 74): return 61
        elif (d100Value == 75): return 62
        elif (d100Value == 76): return 63
        elif (d100Value == 77): return 64
        elif (d100Value == 78): return 65
        elif (d100Value == 79): return 66
        elif (d100Value == 80): return 67
        elif (d100Value == 81): return 68
        elif (d100Value == 82): return 69
        elif (d100Value == 83): return 70
        elif (d100Value == 84): return 71
        elif (d100Value == 85): return 72
        elif (d100Value == 86): return 73
        elif (d100Value == 87): return 74
        elif (d100Value == 88): return 75
        elif (d100Value == 89): return 76
        elif (d100Value == 90): return 77
        elif (d100Value == 91): return 78
        elif (d100Value == 92): return 79
        elif (d100Value == 93): return 80
        elif (d100Value == 94): return 81
        elif (d100Value == 95): return 82
        elif (d100Value == 96): return 83
        elif (d100Value == 97): return 84
        elif (d100Value == 98): return 85
        elif (d100Value == 99): return 86
        else: return 87

    elif (table == Variables.TableH):
        if (d100Value >= 1 and d100Value <= 10): return 0
        elif (d100Value == 11 or d100Value <= 12): return 1
        elif (d100Value == 13 or d100Value == 14): return 2
        elif (d100Value == 15 or d100Value == 16): return 3
        elif (d100Value == 17 or d100Value == 18): return 4
        elif (d100Value == 19 or d100Value == 20): return 5
        elif (d100Value == 21 or d100Value == 22): return 6
        elif (d100Value == 23 or d100Value == 24): return 7
        elif (d100Value == 25 or d100Value == 26): return 8
        elif (d100Value == 27 or d100Value == 28): return 9
        elif (d100Value == 29 or d100Value == 30): return 10
        elif (d100Value == 31 or d100Value == 32): return 11
        elif (d100Value == 33 or d100Value == 34): return 12
        elif (d100Value == 35 or d100Value == 36): return 13
        elif (d100Value == 37 or d100Value == 38): return 14
        elif (d100Value == 39 or d100Value == 40): return 15
        elif (d100Value == 41 or d100Value == 42): return 16
        elif (d100Value == 43 or d100Value == 44): return 17
        elif (d100Value == 45 or d100Value == 46): return 18
        elif (d100Value == 47 or d100Value == 48): return 19
        elif (d100Value == 49 or d100Value == 50): return 20
        elif (d100Value == 51 or d100Value == 52): return 21
        elif (d100Value == 53 or d100Value == 54): return 22
        elif (d100Value == 55): return 23
        elif (d100Value == 56): return 24
        elif (d100Value == 57): return 25
        elif (d100Value == 58): return 26
        elif (d100Value == 59): return 27
        elif (d100Value == 60): return 28
        elif (d100Value == 61): return 29
        elif (d100Value == 62): return 30
        elif (d100Value == 63): return 31
        elif (d100Value == 64): return 32
        elif (d100Value == 65): return 33
        elif (d100Value == 66): return 34
        elif (d100Value == 67): return 35
        elif (d100Value == 68): return 36
        elif (d100Value == 69): return 37
        elif (d100Value == 70): return 38
        elif (d100Value == 71): return 39
        elif (d100Value == 72): return 40
        elif (d100Value == 73): return 41
        elif (d100Value == 74): return 42
        elif (d100Value == 75): return 43
        elif (d100Value == 76): return 44
        elif (d100Value == 77): return 45
        elif (d100Value == 78): return 46
        elif (d100Value == 79): return 47
        elif (d100Value == 80): return 48
        elif (d100Value == 81): return 49
        elif (d100Value == 82): return 50
        elif (d100Value == 83): return 51
        elif (d100Value == 84): return 52
        elif (d100Value == 85): return 53
        elif (d100Value == 86): return 54
        elif (d100Value == 87): return 55
        elif (d100Value == 88): return 56
        elif (d100Value == 89): return 57
        elif (d100Value == 90): return 58
        elif (d100Value == 91): return 59
        elif (d100Value == 92): return 60
        elif (d100Value == 93): return 61
        elif (d100Value == 94): return 62
        elif (d100Value == 95): return 63
        elif (d100Value == 96): return 64
        elif (d100Value == 97): return 65
        elif (d100Value == 98): return 66
        elif (d100Value == 99): return 67
        else: return 68

    elif (table == Variables.TableI):
        if (d100Value >= 1 and d100Value <= 5): return 0
        elif (d100Value >= 6 and d100Value <= 10): return 1
        elif (d100Value >= 11 and d100Value <= 15): return 2
        elif (d100Value >= 16 and d100Value <= 20): return 3
        elif (d100Value >= 21 and d100Value <= 23): return 4
        elif (d100Value >= 24 and d100Value <= 26): return 5
        elif (d100Value >= 27 and d100Value <= 29): return 6
        elif (d100Value >= 30 and d100Value <= 32): return 7
        elif (d100Value >= 33 and d100Value <= 35): return 8
        elif (d100Value >= 36 and d100Value <= 38): return 9
        elif (d100Value >= 39 and d100Value <= 41): return 10
        elif (d100Value == 42 or d100Value == 43): return 11
        elif (d100Value == 44 or d100Value == 45): return 12
        elif (d100Value == 46 or d100Value == 47): return 13
        elif (d100Value == 48 or d100Value == 49): return 14
        elif (d100Value == 50 or d100Value == 51): return 15
        elif (d100Value == 52 or d100Value == 53): return 16
        elif (d100Value == 54 or d100Value == 55): return 17
        elif (d100Value == 56 or d100Value == 57): return 18
        elif (d100Value == 58 or d100Value == 59): return 19
        elif (d100Value == 60 or d100Value == 61): return 20
        elif (d100Value == 62 or d100Value == 63): return 21
        elif (d100Value == 64 or d100Value == 65): return 22
        elif (d100Value == 66 or d100Value == 67): return 23
        elif (d100Value == 68 or d100Value == 69): return 24
        elif (d100Value == 70 or d100Value == 71): return 25
        elif (d100Value == 72 or d100Value == 73): return 26
        elif (d100Value == 74 or d100Value == 75): return 27
        elif (d100Value == 76): return 28
        elif (d100Value == 77): return 29
        elif (d100Value == 78): return 30
        elif (d100Value == 79): return 31
        elif (d100Value == 80): return 32
        elif (d100Value == 81): return 33
        elif (d100Value == 82): return 34
        elif (d100Value == 83): return 35
        elif (d100Value == 84): return 36
        elif (d100Value == 85): return 37
        elif (d100Value == 86): return 38
        elif (d100Value == 87): return 39
        elif (d100Value == 88): return 40
        elif (d100Value == 89): return 41
        elif (d100Value == 90): return 42
        elif (d100Value == 91): return 43
        elif (d100Value == 92): return 44
        elif (d100Value == 93): return 45
        elif (d100Value == 94): return 46
        elif (d100Value == 95): return 47
        elif (d100Value == 96): return 48
        elif (d100Value == 97): return 49
        elif (d100Value == 98): return 50
        elif (d100Value == 99): return 51
        else: return 52
    else: return 0

def getMagicItemTable(magicItemValueTable):                     # Returns the table corresponding to the magicItemValueTable value
    if (magicItemValueTable == Variables.TableA):
        return Tables.MagicItems.tableA
    elif (magicItemValueTable == Variables.TableB):
        return Tables.MagicItems.tableB
    elif (magicItemValueTable == Variables.TableC):
        return Tables.MagicItems.tableC
    elif (magicItemValueTable == Variables.TableD):
        return Tables.MagicItems.tableD
    elif (magicItemValueTable == Variables.TableE):
        return Tables.MagicItems.tableE
    elif (magicItemValueTable == Variables.TableF):
        return Tables.MagicItems.tableF
    elif (magicItemValueTable == Variables.TableG):
        return Tables.MagicItems.tableG
    elif (magicItemValueTable == Variables.TableH):
        return Tables.MagicItems.tableH
    else:
        return Tables.MagicItems.tableI

def getMagicItems(numMagicItems, magicItemValueTable):          # Prints a list of randomly generated magical items
    print(Text.Color.green, end="")                             # Turn on green text output formatting
    magicItemTable = getMagicItemTable(magicItemValueTable)     # Get the magic item table based on the value given
    print(" Magic Items: ")                                     # Print informative header
    numMagicItemTypes = len(magicItemTable)                     # Get the number of the types of magic items in the table
    magicItemTracker = [0] * numMagicItemTypes                  # Initialize an array of the size above to track how many of each one is rolled
    for i in range(numMagicItems):                              # For the number of magic items to retrieve 
        item = getMagicalItem(magicItemValueTable)              # Get a magic item
        magicItemTracker[item] += 1                             # Increment that items corresponding array location in the item tracker
    for i in range(numMagicItemTypes):                          # For the number of magic items in the table
        description = " "                                       # Initialize a spell string variable
        if (magicItemTracker[i] > 0):                           # If the tracker array has at least 1 for the item
            itemCount = str(magicItemTracker[i])                # Get the actual number of items
            description = getDescription(magicItemValueTable, i)# Get the spell string if necessary
            print(" " + itemCount, end="")                      # Print the amount for the magic item, suppressing the newline
            print(" " + magicItemTable[i], end="")              # Print the magic item/description from the table, suppressing the newline
            print(" " + description)                            # Print the spell string variable, either empty string or a spell
    print(Text.Color.off)                                       # Turn the green text output formatting off
    return                                                      # Return from the function