
"""Another syntax"""
from mysql.connector import connect
# Connect to mySQL server and create new data base
"""
with connect(host="localhost",user="root",password="root123") as connection:
    #        print(connection)
    #query="CREATE DATABASE mytrial;"
    #with connection.cursor() as cur:
    #    cur.execute(query)
    print("Successfully created a new database")
    query="SHOW DATABASES"
    with connection.cursor() as cur:
        cur.execute(query)
        for db in cur:
            print(db)
"""

# Connecting to existing database and creating a table 
"""
with connect(host="localhost",user="root",
	password="root123", 
	database="mytrial") as connection:
    #print(connection)
    # Create Table
    query = "CREATE TABLE student( roll_no INT PRIMARY KEY, name varchar(10));"
    with connection.cursor() as cur:
        cur.execute(query)
    print("Successfully Created a table name student")
"""

#Connect to Existing Database and insert records in existing table 
"""
with connect(host="localhost",user="root",password="root123", database="mytrial") as connection:
    #print(connection)
    # Insert multiple records in a table
    query = "INSERT INTO student (roll_no,name) VALUES ( %s, %s );"
    student_records=[(1,"xyz"),(2,"pqr"),(3,"abhi")]
    with connection.cursor() as cur:
        cur.executemany(query,student_records)
        connection.commit()
    print("Successfully Inserted multiple student records")
#executemany will take list of tuples
"""

# Connect to Existing Database and select records from existing table 
"""
with connect(host="localhost",user="root",password="root123", database="mytrial") as connection:
    #print(connection)
    # Select records and print them
    query = "select * from student;"
    with connection.cursor() as cur:
        cur.execute(query)
        for row in cur:
            print(row)
""" 