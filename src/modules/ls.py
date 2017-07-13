import sys, stat, os, time

def forge_ls(dictionary="."):
    _dir = {}
    if len(sys.argv) == 1:
        files = os.listdir(dictionary)
    else:
        files = sys.argv[1:]
    now = int(time.time())
    recent = now - (6 * 30 * 24 * 60 * 60)
    for filename in files:
        try:
            stat_info = os.lstat( dictionary + "/" + filename)
        except:
            sys.stderr.write("%s: No such file or directory\n" % filename)
            continue
        nlink = "%4d" % stat_info.st_nlink 
        size = "%8d" % stat_info.st_size
        ts = stat_info.st_mtime
        if (ts < recent) or (ts > now): 
            time_fmt = "%b %e  %Y"
        else:
            time_fmt = "%b %e %R"
        time_str = time.strftime(time_fmt, time.gmtime(ts))
        filenameStr =  filename
        time_str +=  size + " MB"
        _dir[time_str] = filenameStr
    return _dir


def ls(dictionary):
    longest = []
    for key, value in forge_ls(dictionary).items():
        longest.append( len(key) )
    greatest = max(longest)
    for key, value in forge_ls(dictionary).items():
        if len(key) < greatest:
            buff = " " *  int( greatest - len(key)  + 1) + "-->  " + " "* 1
        else:
            buff = " " * 1 + "-->  " + " " 
            
        print(key, buff , value )
