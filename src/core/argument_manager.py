import inspect,os

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


    if required_arguments == 0 and given_arguments > 0:
        print("[!] Module: '{}' doesn't require any arguments".format(
                         _command))
        return 0
    if required_arguments <  given_arguments:
        print("[!] You've entered too many arguments")
        print(" |  module: '{0}' only requires {1} argument(s) instead of {2}".format(
                         _command,         required_arguments,         given_arguments  ))
        return 0
    if required_arguments >  given_arguments:
        print("[!] You've entered too few arguments")
        print(" |  module: '{0}' requires {1} argument(s) instead of {2}".format(
                         _command,         required_arguments,         given_arguments  ))
        return 0
    if required_arguments ==  given_arguments:
        return 1

