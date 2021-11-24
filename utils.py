def print_choice():
    conf_list = ["mysql","nginx"]
    print("choose from below options/n")
    for i in range(len(conf_list)):
        print(i," --- ",conf_list[i])
    print("for Exit type exit")

def getIdOptions(index):
    conf_list = ["mysql","nginx"]
    return conf_list[index]


