import ModifySpellFile
import TrimTable
import GetSpells
import Spells


def writeSpells(table, lines, spellFile, spellLevel):
    GetSpells.writeSpells(lines, table, spellFile)
    ModifySpellFile.modifyData(spellFile, spellLevel)
    ModifySpellFile.removeColumns(spellFile)
    ModifySpellFile.addHTMLLinks(spellFile)
    return

def main():
    spellTable = TrimTable.trimData("spells.txt")

    lines = GetSpells.lineNumbers(spellTable, Spells.Level.cantrips)
    writeSpells(spellTable, lines, "cantrips.txt", "Cantrips")

    lines = GetSpells.lineNumbers(spellTable, Spells.Level.level1Spells)
    writeSpells(spellTable, lines, "firstLevelSpells.txt", " 1 ")

    lines = GetSpells.lineNumbers(spellTable, Spells.Level.level2Spells)
    writeSpells(spellTable, lines, "secondLevelSpells.txt", " 2 ")

    lines = GetSpells.lineNumbers(spellTable, Spells.Level.level3Spells)
    writeSpells(spellTable, lines, "thirdLevelSpells.txt", " 3 ")

    lines = GetSpells.lineNumbers(spellTable, Spells.Level.level4Spells)
    writeSpells(spellTable, lines, "fourthLevelSpells.txt", " 4 ")

    lines = GetSpells.lineNumbers(spellTable, Spells.Level.level5Spells)
    writeSpells(spellTable, lines, "fifthLevelSpells.txt", " 5 ")

    lines = GetSpells.lineNumbers(spellTable, Spells.Level.level6Spells)
    writeSpells(spellTable, lines, "sixthLevelSpells.txt", " 6 ")

    lines = GetSpells.lineNumbers(spellTable, Spells.Level.level7Spells)
    writeSpells(spellTable, lines, "seventhLevelSpells.txt", " 7 ")

    lines = GetSpells.lineNumbers(spellTable, Spells.Level.level8Spells)
    writeSpells(spellTable, lines, "eighthLevelSpells.txt", " 8 ")

    lines = GetSpells.lineNumbers(spellTable, Spells.Level.level9Spells)
    writeSpells(spellTable, lines, "ninthLevelSpells.txt", " 9 ")



    return


if __name__=="__main__":                                                # If module is run as a main program
       main()                                                           # Enter the main loop

