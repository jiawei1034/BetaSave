from functions import *
#console
def console():
     inp = input("User>")

     if inp == "coin.insert amount":
         insert_income()

     if inp == "coin.create table":
         create_table()

     if inp == "coin.show tables":
         show_tables()

     if inp == "coin.view table":
         view_table()

     if inp == "coin.delete table":
          delete_row()

     if inp == "coin.exit":
         exit()

#help - commands
#calculation
# graph if possible
#error
#pytest
#account, password
