import Quotes

def getAuthorBio(bioLink):
    dateText = Quotes.findData(bioLink, "author-born-date")
    locationText = Quotes.findData(bioLink, "author-born-location")
    if (dateText and locationText):
        authorBirthday = dateText[0].text
        authorLocation = locationText[0].text
        return authorBirthday, authorLocation
    else:
        return False, False

def getAuthorInitials(author):
    tempInitials = author.split()
    fname = tempInitials[0][0]
    lname = tempInitials[1][0]
    return f"{fname}{lname}"

def printNameClue(author):
    tempName = author.split()
    fname = tempName[0]
    lname = tempName[1]
    nameClue = ""
    flag = True
    for char in fname:
        if (char == fname[0] and flag):
            nameClue = nameClue + char
            flag = False
        else:
            nameClue = nameClue + "_"
    nameClue = nameClue + " "
    flag = True
    for char in lname:
        if (char == lname[0] and flag):
            nameClue = nameClue + char
            flag = False
        else:
            nameClue = nameClue + "_"
    return nameClue
