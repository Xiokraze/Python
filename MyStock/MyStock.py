
import csv
import os
from datetime import datetime


class screen():
    clear = lambda: os.system("cls")


class stock_input():
    def __init__(self):
        self.symbols = ["MSFT", "NTDOY", "SNE", "TTWO", "Select All"]
        self.names = ["Microsoft", "Nintendo", "Sony", "Take-Two Interactive"]
        self.columns = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
        self.user_stocks = None
        self.user_option = None
        self.user_stocks_text = None
        self.user_option_text = None
        return

    def get_option_text(self):
        index = self.user_option
        return self.columns[index - 1]

    def get_stock_text(self):
        symbols = []
        for index in self.user_stocks:
            symbols.append(self.symbols[index])
        return symbols

    def get_num_options(self, is_stocks):
        if is_stocks:
            return len(self.symbols)
        return len(self.columns)

    def print_menu(self, is_stocks):
        # Prints numbered list of options
        if is_stocks:
            print("Enter the stock number(s) you would like to view:")
            list = self.symbols
        else:
            print("Which annual averages would you like to view? ")
            list = self.columns
        count = 1
        for option in list:
            print(f" {count}: {option}")
            count += 1
        return

    def get_input_prompt(self, is_stocks, num_options):
        option = "options" if is_stocks else "an option"
        prompt = (f"Enter {option} between 1 and {num_options}: ")
        return prompt

    def valid_input(self, user_input, is_stocks, num_options):
        # Checks if a user didn't enter anything, then for duplicates,
        # then for correct menu numbers, and if looking at options, for
        # more than one entry.
        if len(user_input) != 0:
            if len(user_input) == len(set(user_input)):
                for num in user_input:
                    if num < 1 or num > num_options:
                        return False
                if not is_stocks:
                    if len(user_input) > 1:
                        return False
                return True
        return False

    def get_user_input(self, is_stocks=False):
        num_options = self.get_num_options(is_stocks)
        while True:
            try:
                self.print_menu(is_stocks)
                prompt = self.get_input_prompt(is_stocks, num_options)
                user_input = [int(x) for x in input(prompt).split()]
                if (self.valid_input(user_input, is_stocks, num_options)):
                    if is_stocks:
                        if num_options in user_input:
                            user_input = [i for i in range(num_options - 1)]
                    break
                screen.clear()
            except ValueError:
                pass
        screen.clear()
        if is_stocks:
            return user_input
        else:
            return user_input[0]

    def reset_user_input(self):
        self.user_stocks = self.get_user_input(True)
        self.user_option = self.get_user_input()
        self.user_stocks_text = self.get_stock_text()
        self.user_option_text = self.get_option_text()
        return


class csv_data():
    def __init__(self):
        self.annual_averages = []
        self.current_year = datetime.now().year
        self.oldest_year = None
        self.column_width = 13
        self.file_names = None
        return

    @staticmethod
    def get_file_names(user_stocks):
        # Returns concatenated list of stock symbols and .csv extension
        file_names = []
        for stock in user_stocks:
            file_names.append(f"{stock}.csv")
        return file_names

    @staticmethod
    def get_year(row):
        year = row[0].split('/')
        year = int(year[2])
        return year

    def set_oldest_year(self, year):
        if self.oldest_year == None:
            self.oldest_year = year
        elif year < self.oldest_year:
            self.oldest_year = year

    def get_annual_averages(self, file, user_option):
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
        self.set_oldest_year(start_year)
        return annual_averages

    def reset_data(self, user_stocks, user_option, user_option_text):
        self.file_names = self.get_file_names(user_stocks)
        for file in self.file_names:
            try:
                annual_averages = self.get_annual_averages(file, user_option)
                self.annual_averages.append(annual_averages)
            except:
                print(f"Failed to open/read {file}.")
        self.print_header(user_stocks, user_option_text)
        self.print_data(user_stocks)
        return

    def print_header(self, user_stocks, user_option_text):
        text = user_option_text + " Avg"
        print(f"{text:<{self.column_width}}", end="")
        for stock in user_stocks:
            print(f"{stock:>{self.column_width}}", end="")
        print()
        return

    def print_data(self, user_stocks):
        year = self.oldest_year
        while year < self.current_year:
            print(f"{year:<{self.column_width}}", end="")
            for stock in self.annual_averages:
                if year in stock:
                    print(f"{stock[year]:{self.column_width}}", end="")
                else:
                    no_data = "-"
                    print(f"{no_data:>{self.column_width}}", end="")
            year += 1
            print()

        return


def main():
    stocks = stock_input()
    data = csv_data()

    stocks.reset_user_input()
    data.reset_data(
        stocks.user_stocks_text, 
        stocks.user_option, 
        stocks.user_option_text
    )

    return


if __name__=="__main__":
    main()