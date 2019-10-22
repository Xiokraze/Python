# Joshua Worthington

import csv
import Functions as F
import os


class screen():
    clear = lambda: os.system("cls")

class ticker():
    # Handles presenting user with menu options and converts chosen
    # stocks to their appropriate .csv file name. Gets stock file names
    # and data options.
    def __init__(self):
        self.symbols = ["MSFT", "NTDOY", "SNE", "TTWO", "Select All"]
        self.names = ["Microsoft", "Nintendo", "Sony", "Take-Two Interactive"]
        self.columns = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
        return

    def get_values(self, symbols, user_input, num_options, list):
        # Returns appropriate stock symbol(s)
        if symbols:
            if num_options in user_input:
                values = self.symbols[:num_options - 1]
            else:
                values = []
                for index in user_input:
                    values.append(self.symbols[index - 1])
        else:
            values = user_input[0] - 1
        return values

    def get_list(self, symbols):
        # Returns appropriate list options
        if symbols:
            return self.symbols
        else:
            return self.columns

    def get_menu_options(self, stocks, symbols=True):
        # Returns user input from a list of options
        while True:
            list = self.get_list(symbols)
            num_options = len(list)
            user_input = get_user_input(list, num_options, symbols) 
            if user_input != None:
                break
        screen.clear()
        values = self.get_values(symbols, user_input, num_options, list)
        return values

class csv_stock_data():
    stock_annual_averages = []
    def __init__(self):
        return

    @staticmethod
    def get_year(row):
        year = row[0].split('/')
        year = int(year[2])
        return year

    def get_file_data(self, file, user_option):
        start_year = None
        current_year = None
        days = 0
        data_total = 0
        annual_averages = {}
        with open(file, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if start_year == None:
                    start_year = self.get_year(row)
                    current_year = start_year
                if current_year == self.get_year(row):
                    days += 1
                    try:
                        data = float(row[user_option])
                        data_total += data
                    except ValueError:
                        continue
                else:
                    annual_average = round(data_total / days, 2)
                    annual_averages[current_year] = annual_average
                    days = 1
                    data_total = data
                    current_year += 1
        return annual_averages

    def print_data(self):
        count = 0
        for stock in self.stock_annual_averages:
           count += 1
        print(count)
        return

    def get_data(self, user_stocks, user_option, files):
        for file in files:
            try:
                annual_averages = self.get_file_data(file, user_option)
                self.stock_annual_averages.append(annual_averages)
            except:
                print(f"Failed to open/read {file}")
        return

def valid_user_input(user_input, num_options):
    # Verifies the numbers entered by the user are within the option parameters
    for num in user_input:
        if num >= 1 and num <= num_options:
            return True
    return False

def print_menu_list(list, symbols):
    # Prints numbered list of options
    if symbols:
        print("Enter the stock number(s) you would like to view:")
    else:
        print("Which option would you like to view? ")
    count = 1
    for option in list:
        print(f" {count}: {option}")
        count += 1
    return

def get_user_input(list, num_options, symbols):
    # Returns validated user input from a list of options
    try:
        print_menu_list(list, symbols)
        if symbols:
            option = "options"
        else:
            option = "an option"
        prompt = (f"Enter {option} between 1 and {num_options}: ")
        user_input = [int(x) for x in input(prompt).split()]
        if (valid_user_input(user_input, num_options)):
            return user_input
    except ValueError:
        pass
    screen.clear()
    return None

def get_file_names(user_stocks, options):
    # Returns concatenated list of stock symbols and .csv extension
    file_names = []
    for stock in user_stocks:
        file_names.append(f"{stock}.csv")
    return file_names


def main():
    stocks = ticker()
    data = csv_stock_data()
    user_stocks = stocks.get_menu_options(stocks)       
    user_option = stocks.get_menu_options(stocks, False)
    files = get_file_names(user_stocks, user_option)
    data.get_data(user_stocks, user_option, files)
    data.print_data()
    return

  
if __name__=="__main__":                                            # If module is run as a main program
    main()                                                          # Enter the main loop