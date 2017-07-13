import inspect,os

def import_from_sub_dir(_module):
    mod = getattr(
                getattr(
                        __import__(_module),"modules")
                ,_module.split(".")[-1]
                )
    return getattr(mod,_module.split(".")[-1])
 

def get_arg_len(module):
    return int(
                (
                len(
                    inspect.getargspec(module)[0]
                    )
                )
            )



def check_arguments(command, care_package):
    global _command

    required_arguments = get_arg_len(care_package)
    
    given_arguments = len(command.split()) - 1
    
    _command = command.split()[0]
    if _command.startswith("_"):_command = _command[1::]


    if required_arguments == 0 and given_arguments > 0:
        print("[!] Module: '{}' doesn't require any arguments".format(
                         _command))
        return False
    if required_arguments <  given_arguments:
        print("[!] You've entered too many arguments")
        print(" |  module: '{0}' only requires {1} argument(s) instead of {2}".format(
                         _command,         required_arguments,         given_arguments  ))
        return False
    if required_arguments >  given_arguments:
        print("[!] You've entered too few arguments")
        print(" |  module: '{0}' requires {1} argument(s) instead of {2}".format(
                         _command,         required_arguments,         given_arguments  ))
        return False
    if required_arguments ==  given_arguments:
        return True

