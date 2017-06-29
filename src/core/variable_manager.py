def create_vars(var,val):
    variables = {}; variables[var] = val
    for var in variables:
        globals()[var] = variables[var]
        for x in range(10):
            globals()['variable{}'.format(x)] = 0

