# My little framework. By Bufferbandit.
import src.core.argument_manager   as argument_manager
import src.core.banner_manager     as banner_manager
import src.core.import_manager     as import_manager 
import src.core.stockpile_manager  as stockpile_manager

def input_handler(prefix):
    _input = input(prefix)
    return _input

def split_input(_input):
    global command, argument
    try:
        command  = _input.split()[0]
        argument = _input.split()[1]
    except:
        command = _input

def main():
    global care_package, base,j,c
    while 1:
        c = input_handler("Mlf> ")
        try:
            base = c.split()[0]
        except IndexError:
            print("[!] Please enter a command")
            continue
        try:
            care_package = argument_manager.import_from_sub_dir("src.modules." + base )
            checkpoint = argument_manager.check_arguments(c,care_package)
            if checkpoint:
                import_manager.call_module(c)
            else:
                continue
           
        except:
            print("[!] Module '{}' doesn't exist, please enter a valid one".format(base))
            print(" | To view all the available modules type 'help'")
            continue
        
if __name__ == "__main__":
    print(banner_manager.banner())
    main()
    import src.core.stockpile_manager     as import_manager;stockpile_manager.stockpile_manager()
