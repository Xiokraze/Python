import pyfiglet
import termcolor
import os

def main():
	os.system('color')

	result = pyfiglet.figlet_format("Joshua") 
	print(termcolor.colored(result, "green")) 

if __name__ == "__main__":
	main()