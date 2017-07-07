import re
import src.core.database_manager  as database_manager
import src.core.translate_manager as translate_manager

def filter_argument(argument):
    contains_index = re.findall(r"\[([0-9_]+)\]",argument)
    if len(contains_index) > 0:
        table  = argument.split("[")[0]
        index  = int(contains_index[0])
        result =  database_manager.sql_print_one('data/db.db',index,table)
        return result            

    else:
        return argument
    
def import_from_parent_dir(module,folder):
    global imported_module
    py_module = module + ".py"
    import os,sys
    sys.path.append(
        os.path.dirname(
            os.path.expanduser( folder+module )
            )
        )
    imported_module = __import__(module)

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
    # = translate_manager.filter_argument(arg)
    
    try:
        module = craft_module(command.split()[0])
        
        arg = translate_manager.filter_argument(command.split()[1])
        #print(arg)
        argument = filter_argument( command.split()[1] )
        module(argument)
    except:
        module()

