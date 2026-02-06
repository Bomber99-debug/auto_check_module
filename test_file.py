import sys, os
import auto_check_module_2 as au
from colorama_test import Fore, Back, Style


def main():
    if len(sys.argv) >= 1:
        print(sys.argv)

if __name__ == "__main__":
    # print(au.string_to_date('2022.3.5'))
    # print(sys.modules["os"])
    # print(sys.modules.keys())
    print(Fore.RED + 'Це червоний текст')
    print(Back.GREEN + 'Це текст на зеленому фоні')
    print(Style.RESET_ALL)
    print('Це звичайний текст після скидання стилю')




    print(len(sys.argv))
    main()