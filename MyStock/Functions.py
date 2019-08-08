import csv


class Variables:                                                    # Global variable class
    currentYear = 2019                                              # Initialize current year, makes future updates easier

class Print:
    def printHeader(stockNames):                                        # Prints the stock name header
        print("Year: ", end="")                                         # Print the year column header
        for j in range(len(stockNames)):                                # For each stock
            name = stockNames[j].split(".")                             # Get the stock symbol
            print("%12s " % name[0], end="")                            # Print the stock symbol with a set field width
        print()                                                         # Add a newline
        return                                                          # Return from the function


    def printVolume(data):                                              # Prints stock volumes
        dataString = " {:,.0f}".format(data)                            # Format the string for printing the volume
        print("%12s " % dataString, end="")                             # Print the string
        return                                                          # Return from the function


    def printData(stockNames, averages, startingYears, userColumn):     # Prints the calculated data
        oldestYear = getOldest(startingYears)                           # Get the oldest stock year
        numberOfYears = Variables.currentYear - oldestYear + 1          # Get the number of years to print, add one to include the current year
        filledLists = fillLists(averages, numberOfYears)                # Make all the lists the same size by inserting 0s
        currentYear = 0                                                 # Year tracker variable, added to oldest year to calculate current year
        headerFlag = True                                               # Flag for printing the header

        for i in range(numberOfYears):                                  # For each year
            if (headerFlag):                                            # If the header has not been printed
                Print.printHeader(stockNames)                                 # Print the stock names header
                headerFlag = False                                      # Turn off the print header flag
            print(str(oldestYear + currentYear) + ": ", end="")         # Print the year
            for j in range(len(averages)):                              # For each average
                data = averages[j][currentYear]                         # Get the data for the year
                if (userColumn == 6):                                   # If the column position is for the trading volume
                    Print.printVolume(data)
                else:                                                   # If the data is any of the dollar values
                    if (data == 0):                                     # If the data is 0
                        dataString = "0"                                # Assign a blank space to the data string
                    else:                                               # If there is stock value for that year
                        dataString = " ${:.2f}".format(data)            # Format the price to dollar representation
                    print("%12s " % dataString, end="")                 # Print the data
            currentYear += 1                                            # Increment the year tracking variable
            print()                                                     # Print a newline
        return                                                          # Return from the function


def getLineCount(name):                                             # Counts and returns the number of lines in the csv file
    with open(name, 'r') as file:                                   # Open the file for reading
        reader = csv.reader(file)                                   # Create a csv reader object
        numLines = sum(1 for row in reader)                         # Count the number of lines
    return numLines                                                 # Return the number lines


def getStartYear(name):                                             # Gets and returns the stock's starting year
    with open(name, 'r') as file:                                   # Open the file for reading
        reader = csv.reader(file)                                   # Create a csv reader object
        next(reader)                                                # Skip the first row with column names
        for row in reader:                                          # Assign first row in reader object to a variable                             
            dateSplit = row[0].split('/')                           # Split up the date parameters
            break                                                   # Only need the first row, exit the loop
    return int(dateSplit[2])                                        # Convert the date to an int and return it


def getYear(row):                                                   # Gets and returns the year from the date
    dateSplit = row[0].split('/')                                   # Split up the date parameters
    return int(dateSplit[2])                                        # Convert the date to an int and return it


def getAnnualAverage(column, reader, lineCount, startYear):         # Get's a yearly average for the data
    averages = []                                                   # Initialize vector for averages
    numDays = 0                                                     # Day counter
    total = 0                                                       # Price total
    currentYear = startYear                                         # Initialize variable for tracking the current year
    largestData = 0
    for row in reader:                                              # Iterate through the rows in the reader
        try:                                                        # Try getting the numerical data from the row/col
           data = float(row[column])                                # Cast the data to a float
        except ValueError:                                          # If the data in the row/col was not numerical
            continue                                                # Skip the row
        if (reader.line_num == lineCount):                          # If on the last line of the file
            numDays += 1                                            # Add the last day to the number of days
            total += data                                           # Add the last row's value to the total
            averageValue = total / numDays                          # Calculate the average for the final year
            averages.append(averageValue)                           # Add the final year average to the averages vector
            break                                                   # Calculations complete, exit loop
        else:                                                       # If not on the last line
            if (currentYear == getYear(row)):                       # If the current year is the same as the row's year
                   numDays += 1                                     # Increment the number of days
                   total += data                                    # Add the row's value to the total
            else:                                                   # If the row is now on the next year
                averageValue = total / numDays                      # Calculate the year's average value
                averages.append(averageValue)                       # Add the year's average to the averages vector
                numDays = 1                                         # Reset the days counter
                total = data                                        # Reset the price total, include the first row of the year
                currentYear += 1                                    # Increment the current year
    return averages                                                 # Return the starting year and the averages


def getData(stock, dataPosition, dataName):                         # Computes annual averages
    try:                                                            # Try opening the file
        with open(stock, 'r') as STOCK:                             # Open the file for reading
            lineCount = getLineCount(stock)                         # Get the line count
            startYear = getStartYear(stock)                         # Get the stock's starting year
            reader = csv.reader(STOCK)                              # Create csv reader object
            next(reader)                                            # Skip the first line (column names)
            annualAverages = getAnnualAverage(                      # Get a vector of the yearly averages
                dataPosition,                                       # Colum position for corresponding data type
                reader,                                             # Reader object
                lineCount,                                          # Number of lines
                startYear                                           # Starting year
            )
    except:                                                         # Catch errors opening the file
        return False, None, None                                    # File error occured, return false and no data
    return True, annualAverages, startYear                          # No file error occured, return true, the averages, and the starting year


def getOldest(startingYears):                                       # Gets the oldest of the given stock years
    oldest = startingYears[0]                                       # Initialize oldest to the first stock's year
    for i in range(len(startingYears)):                             # Iterate through the stock years
        if (startingYears[i] < oldest):                             # If the current year is older than the current oldest
            oldest = startingYears[i]                               # Make the current year the oldest
    return oldest                                                   # Return the oldest year


def fillLists(lists, numberOfYears):                                # Fills smaller stock lists with 0s to make them the same length
    for i in range(len(lists)):                                     # Iterate through the lists
        fill = numberOfYears - len(lists[i])                        # Calculate the number of 0s that need to be added
        for j in range(fill):                                       # Loop through the amount of 0s needed
            lists[i].insert(0, 0)                                   # Insert the 0s at the beginning of the list
    return lists                                                    # Return the padded lists