# -*- coding: utf-8 -*-
# Flashgun SWF toolkit. By Bufferbandit.
import src.core.argument_manager   as argument_manager
import src.core.banner_manager     as banner_manager
import src.core.import_manager     as import_manager 
import src.core.stockpile_manager  as stockpile_manager
import src.core.database_manager   as database_manager
import src.core.translate_manager  as translate_manager

import os
debug = 0

def __main__():
    previous = []
    print(
        banner_manager.banner()
         )
    global care_package, base,j,c
    while True:
        try:
            c = translate_manager.filter_command(input("MLF> "))
            
        except KeyboardInterrupt:
            print("\n[*] Goodbye ( ･‿･)ﾉ゛")
            return
        try:
            if (c.startswith("#")  or c.startswith("//") or
               (c.startswith("/*") and c.endswith("*/")) or
               (c.startswith("'") and c.endswith("'"))   or
               (c.startswith("\"") and c.endswith("\""))):
                continue
            if c.split()[0] == "!!":
                try:
                    c = previous[-1]
                except IndexError:
                    print("[!] You haven't typed any commands yet")
                    continue
        except AttributeError:
            #print("[!] Please enter a command")
            continue

        if c: 
            try:
                base = c.split()[0]
            except IndexError:
                continue
            try:
                care_package = argument_manager.import_from_sub_dir("src.modules." + base )
                checkpoint = argument_manager.check_arguments(c, care_package)
                if checkpoint:
                    import_manager.call_module( c )
                    previous.append(base)
                else:
                    continue
               
            except ImportError:
                print(''.join([traceback.print_exc() if debug else ""] ),end="")
                print("[!] Module '{}' doesn't exist, please enter a valid one".format(base))
                print(" | To view all the available modules type 'help'")
                previous.append(base)
                continue
            #print(base)
            
        elif not c:
            #print("[!] Please enter a command")
            continue
       
        
if __name__ == "__main__":
    __main__()
    

if __name__ == "__main__":
    #pass
    print(banner_manager.banner())
    __main__()
    

if __name__ == "__main__":
    print(banner_manager.banner())
    main()
    
