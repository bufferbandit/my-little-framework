import src.core.stockpile_manager  as stockpile_manager 

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
    module = craft_module(command.split()[0])
    try:
        argument = command.split()[1]
        module(argument)
    except:
        module()

