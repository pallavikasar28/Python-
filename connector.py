import mysql.connector as mys

mycon = mys.connect(
                     host = "localhost",
                     user = "root",
                     password = "admin",
                     database = "employee"
                     )
mycursor = mycon.cursor()
no = int(input("Enter Employee ID:"))
sql = "select *from emp where empId={}".format(no)
mycursor.execute(sql)
data = mycursor.fetchall()

if mycursor.rowcount>0:
    for x in data:
        print(x)
else:
    print("Data not found")
