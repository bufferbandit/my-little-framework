import src.core.database_manager as database_manager
import time
def description():
    return "This module is more advanced and uses the database"

def demo_two():
    print("You start with this list: ")
    ls = ["item_one","item_two","item_three","item_four","item_five"]
    for item in ls:
        print(item )
        
    time.sleep(2)
        
    print("\nNow we're going to write this to the database: db.db in data")
    print("Lateron you can acces them as 'example_list'.")
    
    time.sleep(2)

    database_manager.sql_add_data("data/db.db","example_list",ls)

    time.sleep(2)
          
    print("example_list is written to the database!")

    time.sleep(2)

    print("You can view whole of the 'list' table with 'view example_list' or 'list example_list' ")

    time.sleep(2)
    
    print("You can view all of the available lists by typing 'list lists'")

    time.sleep(2)
    
    print("You can index a single item from the db as you would do it in python")
    
    time.sleep(2)
    
    print("""In this case you would use 'example_list[1]' or 'example_list[2]' until
                the last number listed with 'view' or 'list'""")
    
