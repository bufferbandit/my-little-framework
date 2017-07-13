import re
import src.core.database_manager  as database_manager
def filter_command(command):
    global base
    alliassed = {
                "quit"      :   "_quit",
                "?"         :   "help",
                "exit"      :   "_exit",
                "with"      :   "_with",
                "list"      :   "_list",
                "view"      :   "_list",
                "cls"       :   "clear",
                "print"     :   "_print",
                "echo"      :   "_print",
                "py"        :   "python",
                "dir"       :   "ls"
                }
    if command == "":
        return 0
    if command.split()[0] in list(alliassed.keys()):
        base = alliassed[command.split()[0]]
        return base + " " + " ".join(command.split()[1:])
    else:
        return command
    

def filter_argument(argument):
    contains_index = re.findall(r"\[([0-9_]+)\]",argument)
    if len(contains_index) > 0:
        table = argument.split("[")[0]
        index = int(contains_index[0])
      
            
    else:
        return argument
