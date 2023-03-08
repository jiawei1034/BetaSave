from functions import *
#console
def console():
     inp = input("User>")

     if inp == "coin.enter_income":
         insert_income()

     if inp == "coin.create_table":
         create_table()

     if inp == "coin.show_tables":
         show_tables()

     if inp == "coin.view_table":
         view_table()

     if inp == "coin.delete_record":
          delete_row()

     if inp == "coin.exit":
         exit()

     if inp == "coin.help":
         show_options()

     else:
         print("Command not found")
         print("For information on commands type coin.help \n")

#calculation
# graph if possible
