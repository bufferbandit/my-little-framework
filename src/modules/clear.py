import os,platform
def clear():
    if "Windows" in platform.platform():
        os.system("cls")
    else:
        os.system("clear")
    
