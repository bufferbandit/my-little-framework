import os,platform
def description():
    return "Print or echo your input"

def clear():
    if "Windows" in platform.platform():
        os.system("cls")
    else:
        os.system("clear")
    
