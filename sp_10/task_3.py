"""
Create a Python program to use the sqlite database named "q1.db". 
The query to the database should display information, as shown in the example below, 
including phrases: about the successful connection, the total number of records, 
the actual records, the record of closing the database. From the table of "customers" 
to deduce all records for which in a "grade" field of value more than 200 with sort ordering on id

For example output:

Connected to SQLite
Total rows are:   2
Printing each row
Id:  3022
Name:  Nik Rimando
City:  Madrid
Grade:  1000
Seller:  6001


Id:  3025
Name:  Grem Zusisa
City:  USA
Grade:  2000
Seller:  6002
"""
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('q1.db')
print("Connected to SQLite")

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

try:
    # Execute SQL query to fetch records
    cursor.execute("SELECT * FROM customers WHERE grade > 200 ORDER BY id")
    
    # Fetch all records
    rows = cursor.fetchall()
    
    # Display total number of rows
    print(f"Total rows are:   {len(rows)}")
    
    # Print each row
    print("Printing each row")
    for row in rows:
        print("Id: ", row[0])
        print("Name: ", row[1])
        print("City: ", row[2])
        print("Grade: ", row[3])
        print("Seller: ", row[4])
        print("\n")
        
except sqlite3.Error as e:
    print("Error reading data from SQLite table:", e)

finally:
    # Close cursor and connection
    cursor.close()
    conn.close()
    print("The SQLite connection is closed")
