from utils import print_choice,getIdOptions
from colorama import Fore, Back, Style
print('============Welcome to our app=================\n')



if __name__ == "__main__":
    while(True):
        print_choice()
        print('Enter your commands: ')
        x = input()
        if isinstance(x, int):
            choice = getIdOptions(x)
            print("int",choice)
        else:
            if(x == "exit"):
                exit(1)
            else:
                print(Fore.RED+"Enter valid commands")
                print(Style.RESET_ALL)
                continue
        