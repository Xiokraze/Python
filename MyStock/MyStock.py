# Joshua Worthington

import csv
import Functions as F
import Input as I
import os


class screen():
    clear = lambda: os.system("cls")

class ticker():
    def __init__(self):
        self.symbols = ["MSFT", "NTDOY", "SNE", "TTWO", "Select All"]
        self.names = ["Microsoft", "Nintendo", "Sony", "Take-Two Interactive"]
        self.columns = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]
        return

    def print_menu_list(self, list):
        print("Enter the menu number(s) you would like to view:")
        count = 1
        for option in list:
            print(f" {count}: {option}")
            count += 1
        return

    def valid_user_input(self, user_input, num_options):
        for num in user_input:
            if num < 1 or num > num_options:
                return False
        return True

    def get_user_input(self, stocks, symbols=True):
        while True:
            if symbols:
                stocks.print_menu_list(self.symbols)
                num_options = len(self.symbols)
            else:
                stocks.print_menu_list(self.columns)
                num_options = len(self.columns)
            try:
                prompt = (f"Enter number(s) between 1 and {num_options}: ")
                user_input = [int(x) for x in input(prompt).split()]
                if (stocks.valid_user_input(user_input, num_options)):
                    break
            except ValueError:
                pass
            screen.clear()   
        screen.clear()
        return user_input


def main():
    stocks = ticker()

    user_input_stocks = stocks.get_user_input(stocks)       
    user_input_options = stocks.get_user_input(stocks, False)
    return

#def main():
#    ticker = ["ACB", "DIS", "MSFT", "NTDOY", "NVDA", "SNE", "TTWO", "TCEHY", "XLNX", "Select All"]
#    name = ["Aurora", "Disney", "Microsoft", "Nintendo", "Nvidia", "Sony", "Take-Two", "Tencent", "Xilinx"]
#    columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

#    getData = True                                                  # Initialize loop flag to true
#    while(getData):                                                 # While the user wants to keep getting data
#        userStock = I.getStocks(ticker)                             # Get user's stock
#        userColumn = I.getData(columns)                             # Get user's data column
#        annualAverages = []                                         # Initialize annual averages list vector
#        stockNames = []                                             # Initialize stock names list vector
#        startingYears = []                                          # Initialize starting years list vector
#        for i in range(len(userStock)):                             # For each stock the user selected
#            stock = str(ticker[userStock[i]]) + ".csv"              # Concatenate the symbol with its .csv file extention
#            valid, calculation, startYear = F.getData(              # Get a validity status, the averages, and the starting year
#                stock,                                              # Pass the function the stock's name
#                userColumn,                                         # Pass the user's data column selection number
#                columns[userColumn]                                 # Pass the word for the data column that is selected
#            )
#            if not (valid):                                         # If the calculation encountered an error and is not valid
#                print("Error calculating " + stock + " data.")      # Print error message
#                os.system("pause")                                  # Pause the systems so user can read the message
#            else:                                                   # Calculations completed
#                stockNames.append(stock)                            # Add the stock name to the names list
#                annualAverages.append(calculation)                  # Add the calculated averages of the stock to the averages list
#                startingYears.append(startYear)                     # Add the stock's starting year to the years list
#        F.Print.printData(                                                # Print the data
#            stockNames,                                             # Send the stock names list
#            annualAverages,                                         # Send the annual averages list
#            startingYears,                                          # Send the starting years list
#            userColumn                                              # Send the data column number
#        )
#        if not (I.moreData()):                                      # If the user does not want to see more data
#            getData = False                                         # Set loop flag to false to exit the loop
        
if __name__=="__main__":                                            # If module is run as a main program
    main()                                                          # Enter the main loop