import src.core.stockpile_manager  as stockpile_manager 
def help(*args):
    stockpile_manager.show_available_modules()

def description():
    return "Print or echo your input"