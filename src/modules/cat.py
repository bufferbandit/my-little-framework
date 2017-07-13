def get_dict(file):
    _dict = {}
    file = file.split('[')[0]
    try:
        file = open(file,"rb").readlines()
    except FileNotFoundError:
        #print('[!] Couldn\'t open file \'{}\''.format(file))
        return False        
    for line_number, line in enumerate(file):
        _dict[line_number] = line
    return _dict


def get_index(file):
    _dict = get_dict(file)
    if len(file.split('[')) == 1:
        index = len(_dict)
        return index
    elif len(file.split('[')) == 2:
        index = file.split('[')[-1][:-1]
        return int(index)



def cat(file):
    try:
        dex = get_index(file)
    except:
        print('[!] Couldn\'t open file \'{}\''.format(file))
        return
    for x in range(13):
        if x < dex:
            try:
               print(get_dict(file)[x].decode('utf-8'))
            except UnicodeDecodeError:
                print("[!] Cat can't print binary data")
                
       

