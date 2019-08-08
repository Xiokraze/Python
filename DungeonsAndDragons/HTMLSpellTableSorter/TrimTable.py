def modifyLine(line, lineLength):                                               # Line length is at least 11
    if (lineLength == 11):                                                      # If the line is an empty "\t<td></td>"
        return "    <td>-</td>\n"                                               # Return the line with the added "-"
    else:                                                                       # If the line has more data
        lineText = ""                                                           # Array to hold specified characters
        start = "\t<td>"
        end = "</td>\n"
        startIndex = 5                                                          # Starting index
        for i in range(lineLength):                                             # Iterate through the line
            if (i < startIndex): continue                                       # Skip "\t<td>
            if (i == 5 and line[i] != '<'):
                while (line[i] != '<'):
                    if (i == lineLength):
                        return ""
                    lineText = lineText + line[i]
                    i += 1
                return "    <td>" + lineText + end
            while (i < lineLength):
                if (line[i] == '>'):
                    i += 1
                    break
                i += 1
            if (line == lineLength):
                return ""
            else:
                while (i < lineLength):
                    lineText = lineText + line[i]
                    i += 1
                    if (line[i] == '<'):
                        break
                return "    <td>" + lineText + end
    return ""

def trimData(textFile):
    with open(textFile, "r") as file:
        data = file.readlines()
    newData = []
    for line in data:
        lineString = ""
        lineLength = len(line)
        if (lineLength == 5 or lineLength == 6):
            start = ""
            start = start.join(line[0] + line[1] + line[2] + line[3])           # Join the first 4 characters of the line
            if (start == "<tr>"):                                               # If the line starts with "<tr>"
                lineString = lineString + "  " + start + "\n"
            elif (start == "</tr"):                                             # If the line starts with "</tr"
                lineString = lineString + "  "  + start + ">\n"
            else:                                                               # If the line doesn't start with either
                continue                                                        # Skip it
        elif (lineLength >= 11):
            start = ""
            start = start.join(line[0] + line[1] + line[2] + line[3]+ line[4])
            if (start == "\t<td>"):                                             # If the line starts with "    <td"
                newLine = modifyLine(line, lineLength)
                lineString = lineString + newLine
            else:                                                               # If the text does not match, skip it
                continue
        else:                                                                   # if Line is not 10 or greater
            continue                                                            # Skip it
        newData.append(lineString)                                              # Add the line to the data array       
    with open("sortedSpells.txt", "w") as file:
        file.writelines(newData)
    return "sortedSpells.txt"
