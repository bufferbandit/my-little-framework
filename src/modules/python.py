import src.core.stockpile_manager as stockpile_manager

def description():
    return "Run a python IDLE-like shell"


#with open("client","w") as c:


def python():
    quitz = ["quit","exit","exit()","quit()","sys.exit()","raise SystemExit()","os._exit()","os.fork()"]
    blockstarts = ("if","else","def","class","with","for","try","except","while")
    inblock = False                             # We're not in a block yet
    prefix = "Py >>> "                          # Initialize the prefix
    with open("client","w") as c:c.write('')    # Clean out the file on a new run
    while 1:                                    # Start the loop
        i = input(prefix)                       # Set input
        c = open("data/.commands","a")               # Open the (hidden) command file
        if i in quitz:                          # You wanna exit ?
            #print(1)
            print("\t __")
            print("\t{OO}")
            print("\t\__/")
            print("\t|^| Bye  /\ ")
            print("\t| |_____/ / ")
            print("\t\________/  ")
            return                              # Did it
        if i.startswith(blockstarts) :          # Checks if block starts
            #print(2)
            inblock = True                      # We're in a block now
            prefix =  " "*len(prefix) +  "    " # Prefix get's changed to indentation
            c.write(i + "\n")                   # Block start get's written
            c.close()                           # Close file
        elif not inblock:                       # If we're not in a block...
            try:                                # Try to execute a command
                #print(3)
##
                imports = stockpile_manager.stockpile_manager(False)
                #imports = ['download']
                for x in imports:
                    #line = "import src.modules." + x + " as " + x + ";"
                    line = "import src.modules.{0} as {0};".format(x)
                    c.write(line)
##                x = 'banner'
##                c.write("from src.modules." + x + ";\n")   
               
                c.write('import src.modules.banner as banner;')
                c.write('y = "yeeh";')

                
                c.write(i + "\n")               # Write a new line
                c.close()                       # Close file
                exec(open("data/.commands").read())  # Execute the command
                with open("data/.commands","w") as c:# Open the file
                    c.write('')                 # And clean it out 
                continue                        # Continue the loop
            except Exception as e:              # Catch exceptions and print them nicely
                #print(4)
                #print(traceback.print_exc())
                print("[!] Error: {}".format(e))# Print the error in a nice format
                with open("data/.commands","w") as c:# Open the file
                    c.write('')                 # And clean it out
        elif inblock:                           # If we're in a block   
            if i == "":                         # See if we did hit enter
                #print(5)
                prefix = "Py >>> "              # Re-initialize the prefix
                inblock = False                 # We're not in the block anymore
            else:                               # If not hit enter...       
                #print(6)
                c.write("    " + i + "\n")      # Write file with indentation
                c.close()                       # Close file
                exec(open("data/.commands").read())  # So now we can execute whole of the block
                with open("data/.commands","w") as c:# Open the file
                    c.write('')                 # And clean it out

                

