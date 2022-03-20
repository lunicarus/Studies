import sqlite3 as sl3
# with sl3.connect('test.db') as conn:
    #& Extracts the current time, unpacks it in 'time' and prints it in line 9
    # query = "SELECT datetime('now', 'localtime');"

    # cursor = conn.cursor()
    # cursor.execute(query)
    # time = cursor.execute(query).fetchone()[0]
# print(time)
#&creates the COMPANY table(ID,NAME,AGE,ADRESS,SALARY)

# conn.execute('''CREATE TABLE COMPANY  
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);''')

# with sl3.connect('test.db') as conn:
    # cursor = conn.cursor()
    # conn.execute('''CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);''')
    # cursor.execute('''INSERT INTO People VALUES
    #              ('david', 'vector', 12),
    #              ('maria','SANCHES',30);
    #              ''')
    # cursor.execute(
    # "SELECT FirstName, LastName FROM People WHERE Age > 30;"
    # )
    # for row in cursor.fetchall():
    #     print(row)
with sl3.connect('exercise.db') as conn:
    cursor = conn.cursor()
    # cursor.execute("DROP TABLE IF EXISTS Roaster")
    # cursor.execute('''CREATE TABLE Roaster(
    #     Name TEXT PRIMARY KEY,
    #                Species TEXT,
    #                IQ INT );''')
    values = (
    ("Jean-Baptiste Zorg", "Human", 122),
    ("Korben Dallas", "Meat Popsicle", 100),
    ("Ak'not", "Mangalore", -5),
    )
    # cursor.executemany("INSERT INTO Roaster VALUES(?, ?, ?);",values)
    
    # cursor.execute(
    #     "UPDATE Roaster SET Species=? WHERE Name=?",
    #     ("Human","Korben Dallas")
        
    # )
    cursor.execute(
    "SELECT Name,IQ FROM Roaster WHERE Species IS 'Human';"
    )
    for row in cursor.fetchall():
        print(row)