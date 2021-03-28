#!C:/Users/rhonc/AppData/Local/Programs/Python/Python38-32/python
print("Content-Type: text/html")
print()
import cgi
from strap import connection

userRegistered = open("userRegistered.html", 'r').read()

form = cgi.FieldStorage()

name = form.getvalue("name")
email = form.getvalue("email")
password = form.getvalue("password")

cursor = connection.cursor()

insertUser = "insert into user(name, email, password) values(%s, %s, %s)"
cursor.execute(insertUser,(name, email, password))
connection.commit()
connection.close()

print(userRegistered)
# print('<h1 style = "text-align: center">User Registered</h1>')
# print('<h1 style = "text-align: center"><a href = "home.py">See Registered Users</a></h1>')