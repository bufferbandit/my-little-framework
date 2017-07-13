import os.path
import src.core.stockpile_manager as stockpile_manager
def poke(file):
    stock = imports = stockpile_manager.stockpile_manager(False)
   
    if len(file.split(".")) == 3:
        file = file.replace(".","/")
        file += ".py"
    if len(file.split("/")) > 1:
        #print(len(file.split("/")))
        exists = os.path.exists(file)
        #path = file.split("/")
        _file = file.split("/")[-1]
        path = file.replace(_file,"")
        if _file in stock:
            file = file +".py"
        if exists:
            print("[*] File '{1}' with path '{0}'({1}) DOES exists ".format(path,_file))
        else:
            print("[!] File '{1}' with path '{0}'({1}) does NOT exists ".format(path,_file))

    else:
        exists = os.path.exists(file)
        if exists:
            print("[*] File '{}' DOES exist ".format(file))
        else:
            print("[!] File '{}' does NOT exists ".format(file))
