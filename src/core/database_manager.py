import zipfile
import time

#zf = zipfile.ZipFile("../../data/database.fgdb", "a")

def write_to_database(database_file, data_file, data):
    database_file.writestr(
                data_file+".fgf",
                data
                     )

def write_list(_list):
    write_to_database(zf, "u", '\n'.join(_list))
    zf.close()

def read_from_database(database_files,data_file):
    lst = database_files.open(data_file+".fgf").readlines()
    zf.close()
    return lst



    

