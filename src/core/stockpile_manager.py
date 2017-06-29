import sys,os
def stockpile_manager():
    available_modules = []
    excludes = ["clear.py","_exit.py","_clear.py","help.py"]
    for item in os.listdir("./src/modules/"):
        if item.endswith(".py") and item not in excludes:
            available_modules.append(item.replace(".py",""))
    return available_modules

   

def show_available_modules():
    available_modules = stockpile_manager()
    for help_number,help_item in enumerate(available_modules,start=1):
        print("[" + str(help_number) + "] " + help_item)
