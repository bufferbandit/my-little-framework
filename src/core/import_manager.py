import re
import src.core.database_manager  as database_manager
import src.core.translate_manager as translate_manager


        
def filter_argument(argument):
    argument = "".join(argument)
    contains_index = re.findall(r"\[([0-9_]+)\]",argument)
    if len(contains_index) > 0:
        table  = argument.split("[")[0]
        index  = int(contains_index[0])
        result =  database_manager.sql_print_one('data/db.db',index,table)
        return result            

    else:
        return argument
    print(argument)
    

def filter_two(argument):
    if len(argument) > 1:
        for index,_argument in enumerate(argument):
             argument[index] = filter_argument(_argument)
        return argument
    else:
        return argument
        


def craft_module(command):
    try:
        module = getattr(
                    getattr(
                        getattr(
                                __import__("src.modules." + command),'modules'
                           ),command
                        ),command)
        return module
    except ImportError:
        return 
  

def call_module(command,*args):
    
    try: 
        module = craft_module(command.split()[0])
        arg = translate_manager.filter_argument(command.split()[1])
        argument =  command.split()[1::]   
        filter_two(argument)
        if len(argument) == 1:
            argument = filter_argument(argument)
            
        module(*argument)
    except IndexError:
        module()
    except TypeError:
        argument = filter_argument(argument)
        module(argument)


        module()


    except:
        module()

