import sqlite3

connection = sqlite3.connect("mydata.db")

cursor = connection.cursor()

def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Salary (
        table_id INTEGER,
        date_received TEXT,
        amount_earned TEXT
    )
    """)
    connection.commit()
    print("Table created successfully ")

def insert_income():
    table_id = input("ID: ")
    date_received = input("DATE: ")
    amount_earned = input("AMOUNT: ")
    cursor.execute("INSERT INTO Salary VALUES (?, ?, ?)",(table_id, date_received, amount_earned)
    )
    connection.commit()
    print("Record inserted successfully ")

def view_table():
    cursor.execute("""
    SELECT * FROM Salary
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



