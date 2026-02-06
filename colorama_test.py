from colorama import Fore, Back, Style

print(Fore.BLUE + "some red text")
print(Back.CYAN + "and with a green background")
print(Style.DIM + "and in dim text")
print(Style.RESET_ALL)
print("back to normal now")