def description():
    return "Print or echo your input"

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
