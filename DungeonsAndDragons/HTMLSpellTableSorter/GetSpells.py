import Spells


def checkSpell(string, lineNum, spellLevelTable):
    end = len("</td>\n")
    tempSpell = ""
    for i in range(len(string) - end):
        tempSpell = tempSpell + string[i]
    for i in range(len(spellLevelTable)):
        if (tempSpell == spellLevelTable[i]):
            return(lineNum)
    return 0

def writeSpells(lines, trimmedSpellTable, writeFile):
    data = open(trimmedSpellTable, "r")
    fwrite = open(writeFile, "w")
    lineNum = 1
    numElements = 12
    printElements = 0
    printFlag = 0
    for i in range(len(Spells.Level.header)):
        fwrite.write(Spells.Level.header[i])
    for line in data:
        for i in range(len(lines)):
            if (lineNum == lines[i] - 1):
                printFlag = 1
                break
        if (printFlag == 1):
            fwrite.write(line)
            printElements += 1
            if (printElements == numElements):
                printElements = 0
                printFlag = 0
        lineNum += 1
    data.close()
    fwrite.close()
    return

def lineNumbers(trimmedSpellTable, spellLevelTable):
    with open(trimmedSpellTable, "r") as f:
        data = f.readlines()
    data = open(trimmedSpellTable, "r")
    lineNum = 1
    lines = []
    for line in data:
        tempString = ""
        if (lineNum == 2 or ((lineNum - 2) % 12) == 0):
            for i in range(len(line)):
                if (i < 8 and i < len(line)):
                    continue
                else:
                    tempString = tempString + line[i]
            spellLineNum = checkSpell(tempString, lineNum, spellLevelTable)
            if (spellLineNum > 0):
                lines.append(spellLineNum)
        lineNum += 1
    return lines

