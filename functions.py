import sqlite3

connection = sqlite3.connect("Db/mydata.db")

cursor = connection.cursor()

def create_table():
    table_name = input("TABLE: ")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS {} (
        table_id TEXT,
        date_received TEXT,
        amount_earned TEXT
    )
    """.format(table_name))
    connection.commit()
    print("Table created successfully ")

def insert_income():
    table_name = input("TABLE: ")
    table_id = input("ID: ")
    date_received = input("DATE: ")
    amount_earned = input("AMOUNT: ")
    cursor.execute("INSERT INTO {} VALUES (?, ?, ?)".format(table_name),(table_id, date_received, amount_earned)
    )
    connection.commit() 
    print("Record inserted successfully ")

def view_table():
    table_name = input("TABLE: ")
    cursor.execute("""
    SELECT * FROM {}
    """.format(table_name))
    connection.commit()
    rows = cursor.fetchall()
    heading = ['ID', 'Name', 'City']
    print(f'{heading[0]: <10}{heading[1]: <10}{heading[2]: <10}')
    for i in rows:
        print(f'{rows[0]: <10}{rows[1]: <10}{rows[2]: <10}')

def delete_row():
    table_name = input("TABLE: ")
    table__id = input("ID: ")
    cursor.execute("DELETE FROM {} WHERE table_id=?".format(table_name),(table__id)
    )
    connection.commit()
    print("Record deleted successfully ")

def show_tables():
    # print("1)January")
    # print("2)February")
    # print("3)March")
    # print("4)April")
    # print("5)May")
    # print("6)June")
    # print("7)July")
    # print("8)August")
    # print("9)September")
    # print("10)October")
    # print("11)November")
    # print("12)December \n")
    cursor.execute("""SELECT name FROM sqlite_master
    WHERE type='table';""")
    connection.commit()
    tables = cursor.fetchall()
    print(tables)

def show_options():
    f = open('readme.txt', 'r') 
    file_contents = f.read()
    print(file_contents)


