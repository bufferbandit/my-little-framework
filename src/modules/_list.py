import src.core.database_manager  as database_manager

def description():
    return "Print or echo your input"
	
def _list( table ):
    if table == "lists" or table == "views":
        tables = database_manager.sql_whats_in_store("data/db.db")
        print("[*] Current {0} list(s) are: ".format( len(tables) ))
        for index,table in enumerate(tables,start=1):
            print("[{0}] {1}".format( index,table ) )
    else:
        database_manager.sql_print_all('data/db.db' ,table )
       
