from utils import my_one

print('============Welcome to our app=================')



if __name__ == "__main__":
    while(True):
        my_one()
        print('Enter your name:')
        x = input()
        print('Hello, ' + x)
        if(x == "exit"):
            exit(1)