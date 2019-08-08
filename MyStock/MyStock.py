# Joshua Worthington

import csv
import Functions as F
import Input as I
import os



def main():
    ticker = ["ACB", "DIS", "MSFT", "NTDOY", "NVDA", "SNE", "TTWO", "TCEHY", "XLNX", "Select All"]
    name = ["Aurora", "Disney", "Microsoft", "Nintendo", "Nvidia", "Sony", "Take-Two", "Tencent", "Xilinx"]
    columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

    getData = True                                                  # Initialize loop flag to true
    while(getData):                                                 # While the user wants to keep getting data
        userStock = I.getStocks(ticker)                             # Get user's stock
        userColumn = I.getData(columns)                             # Get user's data column
        annualAverages = []                                         # Initialize annual averages list vector
        stockNames = []                                             # Initialize stock names list vector
        startingYears = []                                          # Initialize starting years list vector
        for i in range(len(userStock)):                             # For each stock the user selected
            stock = str(ticker[userStock[i]]) + ".csv"              # Concatenate the symbol with its .csv file extention
            valid, calculation, startYear = F.getData(              # Get a validity status, the averages, and the starting year
                stock,                                              # Pass the function the stock's name
                userColumn,                                         # Pass the user's data column selection number
                columns[userColumn]                                 # Pass the word for the data column that is selected
            )
            if not (valid):                                         # If the calculation encountered an error and is not valid
                print("Error calculating " + stock + " data.")      # Print error message
                os.system("pause")                                  # Pause the systems so user can read the message
            else:                                                   # Calculations completed
                stockNames.append(stock)                            # Add the stock name to the names list
                annualAverages.append(calculation)                  # Add the calculated averages of the stock to the averages list
                startingYears.append(startYear)                     # Add the stock's starting year to the years list
        F.Print.printData(                                                # Print the data
            stockNames,                                             # Send the stock names list
            annualAverages,                                         # Send the annual averages list
            startingYears,                                          # Send the starting years list
            userColumn                                              # Send the data column number
        )
        if not (I.moreData()):                                      # If the user does not want to see more data
            getData = False                                         # Set loop flag to false to exit the loop
        
if __name__=="__main__":                                            # If module is run as a main program
    main()                                                          # Enter the main loop