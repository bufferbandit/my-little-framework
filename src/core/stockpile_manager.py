import sys, os
from collections import Counter
def stockpile_manager():
    available_modules = []
    excludes = ["clear.py","_exit.py","_clear.py","help.py","import_helper.py","banner.py","_print.py","_list.py"]
    for item in os.listdir("./src/modules/"):
        if item.endswith(".py") and item not in excludes:
            
            if item.startswith("_"):
                available_modules.append(item[1:].replace(".py",""))  
            else:
                available_modules.append(item.replace(".py",""))
    if len(available_modules) > 0:
        print("[*] Current {0} module(s) in stock are:".format(len(available_modules)))   
    else:
        pass
    return available_modules

   
#__import__("src.modules._print").modules._print.description.short_description
def show_available_modules():
    available_modules = stockpile_manager()
    longest = []
    for help_item in available_modules:
        longest.append( len(help_item) )
    greatest = max(longest)
    for help_number, help_item in enumerate(available_modules,start=1):
        #print(1)
        try:
            description = getattr(getattr(getattr(__import__("src.modules." + help_item),"modules"),help_item),"description")()
        except:
            #print(help_item)
            help_item = "_" + help_item
            description = description = getattr(getattr(getattr(__import__("src.modules." + help_item),"modules"),help_item),"description")()
            help_item = help_item[1:]
        #print(2)
        if len(help_item) < greatest:
            buff = " " *  int( greatest - len(help_item)  + 3) + "-" + " "* 3
        else:
            buff = " " * 3 + "-" + " " + " "* 2
        #print(3)
        print("[" + str(help_number) + "] " + help_item + buff + description)
