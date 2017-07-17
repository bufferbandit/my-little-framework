import re
import src.core.database_manager  as database_manager
import src.core.translate_manager as translate_manager
import src.core.database_manager  as database_manager
        
def filter_argument(argument,permission):
    if argument in database_manager.sql_whats_in_store('data/db.db') and permission:
        l = []
        for i in database_manager.sql_read_data('data/db.db',argument):
            l.append(i[-1])
        return l
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
    

def filter_two(argument,permission=True):
    if len(argument) > 1:
        for index,_argument in enumerate(argument):
             argument[index] = filter_argument(_argument,permission)
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
        #print(command.split()[0])
        no_permission = ['_list']
        if command.split()[0] in no_permission:
            permission = False
        else:
            permission = True
        arg = translate_manager.filter_argument(command.split()[1])
        argument =  command.split()[1::]   
        filter_two(argument)
        if len(argument) == 1:
            argument = filter_argument(argument,permission)
        #print(permission)
        module(*argument)
    except IndexError:
        module()
    except TypeError:
        no_permission = ['_list']
        if command.split()[0] in no_permission:
            permission = False
        else:
            permission = True
        argument = filter_argument(argument,permission)
        module(argument)

