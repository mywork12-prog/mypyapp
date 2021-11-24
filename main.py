print('============Welcome to our app=================')



if __name__ == "__main__":
    while(True):
        print('Enter your name:')
        x = input()
        print('Hello, ' + x)
        if(x == "exit"):
            exit(1)