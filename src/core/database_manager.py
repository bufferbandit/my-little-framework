#import ruamel.std.zipfile as zipfile
import zipfile, sqlite3
def zip_write_to_database(data_file, data, database_file):
    
    zf_name = str(database_file).split("'")[1].split("/")[-1]
    zf.close()
    try:
        zipfile.delete_from_zip_file(zf_name,file_names=['sites.fgf'])#'.*.exe')
    except:
        pass
    database_file.writestr( data_file + ".fgf", data)
    zf.close()

def zip_write_list(name,_list,zf):
    write_to_database(name, '\n'.join(_list),zf)
    zf.close()

def zip_read_from_database(database_files,data_file):
    lst = database_files.open(data_file+".fgf").readlines()
    zf.close()
    return lst

def sql_create_table(db,name):
    conn = sqlite3.connect(db)
    c    = conn.cursor()
    c.execute(
        """

         CREATE TABLE IF NOT EXISTS {0}
                (ID INTEGER PRIMARY KEY,
                VALUE TEXT)
                 
        """.format(name)
              )
    #c.close()
    
def sql_add_data(db,name,_list,mode="w"):
    conn = sqlite3.connect(db)
    c    = conn.cursor()
    if mode == "w":
        c.execute(
                """
                 DROP TABLE IF EXISTS {0}
                """.format(name)

                )
    elif mode == "a":
        pass
    sql_create_table(db,name)
    for num, data in enumerate(_list,start=1):
        
        c.execute(
            """
        
             INSERT INTO {0}
             (VALUE) VALUES ('{1}')
             
            """.format(name,  data )
                  )
        conn.commit() 
    #c.close()

def sql_read_data(db,table):
    c = db
    try:
        c.execute(
            """
            SELECT * FROM {0}; 
            """.format(table)
                 )
        result = c.fetchall()
        #c.close()
        return result
    except sqlite3.OperationalError:
        return False

def sql_print_all(db,table):
    conn = sqlite3.connect(db)
    c    = conn.cursor()
    
    gett = sql_read_data(c,table)
    try:
        for pack in gett:
            print("[" + str(pack[0]) + "] " + pack[1])
    except TypeError:
        return False

def sql_print_one(db,index,table):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    try:
        return sql_read_data(c,table)[index-1][-1]
    except IndexError:
        print("Variable doesn't have index {0}".format(index)) 
        return 0
    except TypeError:
        print("Variable {0} doesn't exist".format(table))
        return 0
    
def sql_whats_in_store(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(
        """
        SELECT name FROM sqlite_master
        WHERE type='table';
        """
        )
    ret = []        ; fetched = c.fetchall()
    for i in fetched: ret.append(i[0])
    return            ret
    
