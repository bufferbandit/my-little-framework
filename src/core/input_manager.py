

def yes():
     while 1:
          i = input("[?] Yes/no: ")
          yes = ["Yes","yes","y","Y","true","True",1]
          no = ["No","no","N","n","false","False",0]
          if i in yes:
               return True
               break
          elif i in no:
               return False
               break
          else:
               print('[!] Error, please enter one of these options: ')
               print(" |  Y/y/Yes/yes/1 for yes and N/n/No/no/0 for no")
               continue

def no():
     while 1:
          i = input("[?] Yes/no: ")
          yes = ["Yes","yes","y","Y","true","True",1]
          no = ["No","no","N","n","false","False",0]
          if not i in yes:
               return True
               break
          elif not i in no:
               return False
               break
          else:
               print('[!] Error, please enter one of these options: ')
               print(" |  Y/y/Yes/yes/1 for yes and N/n/No/no/0 for no")
               continue
