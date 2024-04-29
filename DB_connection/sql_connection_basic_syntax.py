#BASIC CONNECTION
'''
#pip install mysql-connector-python         mini conda isnt available
import mysql.connector
cnx=mysql.connector.connect(user='root',
                            password='avi.bansal3',
                            host='127.0.0.1',
                            database='mytrial')
cnx.close()
#In database give the name of existing database
#password is the mysql password

'''
#CREATE TABLE
'''
import mysql.connector
cnx=mysql.connector.connect(user='root',
                            password='avi.bansal3',
                            host='127.0.0.1',
                            database='mytrial')
cur=cnx.cursor()
cur.execute("""CREATE TABLE student(
            roll_no int,
            subid varchar(10),
            marks int);
""")
cnx.commit()
cnx.close()
'''
#INSERT RECORDS
'''
records=[
        [1,'sub1',34],
        [2,'sub1',30],
        [3,'sub1',23],
        [1,'sub2',23],
        [2,'sub2',26],
        [3,'sub2',30],
        [1,'sub3',30],
        [2,'sub3',30],
        [3,'sub3',27]
]
import mysql.connector
cnx=mysql.connector.connect(user="root",
                               password='avi.bansal3',
                               host='127.0.0.1',
                               database='mytrial')
cur=cnx.cursor()
for rno,sub,marks in records:
    query="insert into student values("+\
        str(rno)+","+\
        repr(sub)+","+\
        str(marks)+");"
    print(query)
    cur.execute(query)
cnx.commit()
cnx.close()
#use rept to pas "" into sql querry
'''

#Select records and display
'''
import mysql.connector
cnx=mysql.connector.connect(user="root",
                            password="avi.bansal3",
                            host="127.0.0.1",
                            database="mytrial")
cur=cnx.cursor()
cur.execute("select*from student")
for i in cur:
    print(i)
cnx.close()
'''

