def hyphenateSpell(spell):
    tempSpell = ""
    for i in range(len(spell)):
        if (spell[i] == ' '):
            tempSpell += '-'
        elif (spell[i] == '\''):
            tempSpell += ''
        else:
            tempSpell += spell[i]
    return tempSpell

def addHTMLLinks(textFile):
    headerStart = 35                                   # length of <td><a class="magicItem" href="
    headerMid = 18                                     # length of " target="_blank">
    headerEnd = 10                                     # length of </a></td>
    link = "https://www.dndbeyond.com/spells/"
    spellLine = headerStart + headerMid + headerEnd
    with open(textFile, "r") as f:
        data = f.readlines()
    for line in range(len(data)):
        lineLength = len(data[line])
        if (lineLength < spellLine):
            continue
        else:
            start = ""
            for i in range(headerStart):
                start = start + data[line][i]
            mid = ""
            for i in range(headerMid):
                mid = mid + data[line][i + headerStart]
            end = ""
            for i in range(headerEnd):
                end = end + data[line][lineLength-headerEnd + i]
            spell = ""
            for i in range(lineLength - spellLine):
                spell = spell + data[line][headerStart + headerMid + i]
            newSpell = hyphenateSpell(spell)
            spellLink = start + link + newSpell + mid + spell + end
            data[line] = spellLink
    with open(textFile, "w") as f:
        data = f.writelines(data)
    return

def removeColumns(textFile):
    with open(textFile, "r") as f:
        data = f.readlines()  
    lineCount = 1
    for line in range(len(data)):
        if (lineCount == 3 or lineCount == 4 or lineCount == 10 or lineCount == 11):
            data[line] = ""
        #if (lineCount == 11 and data[line] == "    <th>Source</th>\n"):
        #    data[line] = "    <th>Description</th>\n"
        #elif (lineCount == 11 and data[line] != "    <th>Description</th>\n"):
        #    data[line] = "    <td></td>\n"
        lineCount += 1
        if (lineCount == 12):
            lineCount = 0
    with open(textFile, "w") as f:
        f.writelines(data)
    return

def modifyData(textFile, level):
    lvl0 = "    <td>level0lvl0</td>\n"
    lvl1 = "    <td>level1lvl1</td>\n"
    lvl2 = "    <td>level2lvl2</td>\n"
    lvl3 = "    <td>level3lvl3</td>\n"
    lvl4 = "    <td>level4lvl4</td>\n"
    lvl5 = "    <td>level5lvl5</td>\n"
    lvl6 = "    <td>level6lvl6</td>\n"
    lvl7 = "    <td>level7lvl7</td>\n"
    lvl8 = "    <td>level8lvl8</td>\n"
    lvl9 = "    <td>level9lvl9</td>\n"

    spellLevel = "    <td>" + level + "</td>\n"
    replaceCon = "    <td>Concentration,upto1minute</td>\n"
    con = "    <td>Con, up to 1 min</td>\n"
    replaceCon2 = "    <td>Concentration,upto1hour</td>\n"
    con2 = "    <td>Con, up to 1 hour</td>\n"
    replaceCon3 = "    <td>Concentration,upto10minutes</td>\n"
    con3 = "    <td>Con, up to 10 min</td>\n"
    replaceCon4 = "    <td>Concentration,upto1round</td>\n"
    con4 = "    <td>Con, up to 1 round</td>\n"
    replaceCon5 = "    <td>Concentration,upto10minute</td>\n"
    con5 = "    <td>Con, up to 10 min</td>\n"
    replaceCon6 = "    <td>Concentration,upto8hours</td>\n"
    con6 = "    <td>Con, up to 8 hours</td>\n"
    replaceCon7 = "    <td>Concentration,upto2hours</td>\n"
    con7 = "    <td>Con, up to 2 hours</td>\n"
    replaceCon8 = "    <td>Concentration,upto1day</td>\n"
    con8 = "    <td>Con, up to 1 day</td>\n"
    replaceCon9 = "    <td>Concentration,upto6rounds</td>\n"
    con9 = "    <td>Con, up to 6 rounds</td>\n"
    replaceCon10 = "    <td>Concentration,upto24hours</td>\n"
    con10 = "    <td>Con, up to 24 hours</td>\n"
    replaceHour = "    <td>1hour</td>\n"
    hour = "    <td>1 hour</td>\n"
    replaceHour2 = "    <td>Upto1hour</td>\n"
    hour2 = "    <td>Up to 1 hour</td>\n"
    replaceHour3 = "    <td>8hours</td>\n"
    hour3 = "    <td>8 Hours</td>\n"
    replaceHour4 = "    <td>24hours</td>\n"
    hour4 = "    <td>24 Hours</td>\n"
    replaceMin = "    <td>1minute</td>\n"
    min = "    <td>1 min</td>\n"
    replaceMin2 = "    <td>10minutes</td>\n"
    min2 = "    <td>10 Minutes</td>\n"
    replaceMin3 = "    <td>Upto1minute</td>\n"
    min3 = "    <td>Up to 1 min</td>\n"
    replaceDays = "    <td>10days</td>\n"
    days = "    <td>10 Days</td>\n"
    replaceInstant = "    <td>Instantaneous</td>\n"
    instant = "    <td>Instant</td>\n"
    replaceInstantaneous = "    <td>Instantaneousor1hour(seebelow)</td>\n"
    instantaneous = "    <td>Instant/1 hour</td>\n"
    replaceConStatus = "    <td>Concentration</td>\n"
    conStatus = "    <td>Yes</td>\n"
    replaceDispelled = "    <td>Untildispelled</td>\n"
    dispelled = "    <td>Until Dispelled</td>\n"
    replaceDispelled2 = "    <td>Untildispelledortriggered</td>\n"
    dispelled2 = "    <td>Until Dispelled/Triggered</td>\n"
    replaceRound = "    <td>1round</td>\n"
    round = "    <td>1 round</td>\n"
    start = "    <td><a class=\"magicItem\" href=\"\" target=\"_blank\">"
    end = "</a></td>\n"

    with open(textFile, "r") as file:
        data = file.readlines()

    for line in range(len(data)):
        if (line == 1 or line == 2): continue
        if (data[line] == lvl0 or data[line] == lvl1 or data[line] == lvl2 or data[line] == lvl3 or data[line] == lvl4 or data[line] == lvl5 or data[line] == lvl6 or data[line] == lvl7 or data[line] == lvl8 or data[line] == lvl9):
            data[line] = spellLevel
        elif (data[line] == replaceCon):
            data[line] = con
        elif (data[line] == replaceDays):
            data[line] = days
        elif (data[line] == replaceHour):
            data[line] = hour
        elif (data[line] == replaceHour2):
            data[line] = hour2
        elif (data[line] == replaceHour3):
            data[line] = hour3
        elif (data[line] == replaceHour4):
            data[line] = hour4
        elif (data[line] == replaceMin):
            data[line] = min
        elif (data[line] == replaceMin2):
            data[line] = min2
        elif (data[line] == replaceMin3):
            data[line] = min3
        elif (data[line] == replaceInstant):
            data[line] = instant
        elif (data[line] == replaceConStatus):
            data[line] = conStatus
        elif (data[line] == replaceInstantaneous):
            data[line] = instantaneous
        elif (data[line] == replaceCon2):
            data[line] = con2
        elif (data[line] == replaceCon3):
            data[line] = con3
        elif (data[line] == replaceCon4):
            data[line] = con4
        elif (data[line] == replaceCon5):
            data[line] = con5
        elif (data[line] == replaceCon6):
            data[line] = con6
        elif (data[line] == replaceCon7):
            data[line] = con7
        elif (data[line] == replaceCon8):
            data[line] = con8
        elif (data[line] == replaceCon9):
            data[line] = con9
        elif (data[line] == replaceCon10):
            data[line] = con10
        elif (data[line] == replaceRound):
            data[line] = round
        elif (data[line] == replaceDispelled):
            data[line] = dispelled
        elif (data[line] == replaceDispelled2):
            data[line] = dispelled2

        elif (line == 2 or ((line - 1) % 12 == 0)):
            if (line == 3): continue
            spell = ""
            startIndex = 8
            for char in range(len(data[line])):
                if (char < startIndex):
                    continue
                if (data[line][char] == '<'):
                    break
                else:
                    spell = spell + data[line][char]
            data[line] = start + spell + end

    with open(textFile, "w") as file:
        file.writelines(data)
    return