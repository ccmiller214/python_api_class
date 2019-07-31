#!/usr/bin/python3

import sqlite3
import argparse

records = [
        "1,'Paul', 32, 'California', 20000.00)",
        "2, 'Allen', 25, 'Texas', 15000.00)",
        "3, 'Teddy', 23, 'Norway', 20000.00)",
        "4, 'Mark', 55, 'Iowa', 65000.00)"
        ]

def main():
    if args.f: dbfile = args.f
    else: dbfile = 'test.db'
    conn = sqlite3.connect(dbfile)

    print("Open database successfully")

    try:
        conn.execute('''CREATE TABLE COMPANY
        (ID INT PRIMARY KEY NOT NULL,
        NAME TEXT           NOT NULL,
        AGE INT             NOT NULL,
        ADDRESS         CHAR(50),
        SALARY          REAL);''')
    
        print("Table created successfully")

    except sqlite3.OperationalError:
        print("Table already created in " + dbfile)
    
    myop = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES ("
    for rec in records:
        try:
#            print("Adding ... -- " + rec + " --")
            conn.execute(myop + rec)
            conn.commit()
            print("Record added successfully")
        except sqlite3.IntegrityError:
            print("Record exists! Not added!")

    conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
    conn.commit()
    print("Total number of rows updated: ", conn.total_changes)

    tablep = conn.execute("SELECT id,name,address,salary from COMPANY")
    for row in tablep:
        print("------------")
#        print(row)
        print("ID = ", row[0])
        print("Name = ",row[1])
        print("Location = ",row[2])
        print("Salary = ",row[3])

    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help="Provide the name of database file")
    args = parser.parse_args()
    main()
