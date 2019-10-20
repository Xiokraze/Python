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
        self.annual_averages = []
        self.start_year = []
        return

    @staticmethod
    def print_menu_list(list):
        print("Enter the menu number(s) you would like to view:")
        count = 1
        for option in list:
            print(f" {count}: {option}")
            count += 1
        return

    @staticmethod
    def valid_user_input(user_input, num_options):
        for num in user_input:
            if num < 1 or num > num_options:
                return False
        return True

    def get_user_input(self, stocks, symbols=True):
        while True:
            if symbols:
                list = self.symbols
            else:
                list = self.columns
            try:
                num_options = len(list)
                self.print_menu_list(list)
                prompt = (f"Enter number(s) between 1 and {num_options}: ")
                user_input = [int(x) for x in input(prompt).split()]
                if (self.valid_user_input(user_input, num_options)):
                    break
            except ValueError:
                pass
            screen.clear()   
        screen.clear()
        if symbols:
            if num_options in user_input:
                return self.symbols[:num_options - 1]
            user_option_values = []
            for index in user_input:
                user_option_values.append(list[index - 1])
            return user_option_values
        else:
            return user_input

    def get_data(self, user_stocks, options):
        for stock in user_stocks:
            stock_name = f"{stock}.csv"
            print(stock_name)
        return


def main():
    stocks = ticker()
    user_stocks = stocks.get_user_input(stocks)       
    user_options = stocks.get_user_input(stocks, False)
    stocks.get_data(user_stocks, user_options)
    return

  
if __name__=="__main__":                                            # If module is run as a main program
    main()                                                          # Enter the main loop