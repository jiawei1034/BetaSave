import sqlite3

connection = sqlite3.connect("mydata.db")

cursor = connection.cursor()

def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Received (
        table_id INTEGER,
        date_received TEXT,
        details TEXT,
        amount_received TEXT
    )
    """)
    connection.commit()
    print("Table created successfully ")

def insert_income():
    table_id = input("ID: ")
    date_received = input("DATE: ")
    details = input("DETAILS: ")
    amount_received = input("AMOUNT: ")
    cursor.execute("INSERT INTO Received VALUES (?, ?, ?, ?)",(table_id, date_received, details, amount_received)
    )
    connection.commit()
    print("Record inserted successfully ")

def view_table():
    cursor.execute("""
    SELECT * FROM Received
    """)
    connection.commit()
    rows = cursor.fetchall()
    print(rows)
    
def delete_row():
    table__id = input("User> ")
    cursor.execute("DELETE FROM Received WHERE table_id=?",(table__id)
    )
    connection.commit()
    print("Record deleted successfully ")



