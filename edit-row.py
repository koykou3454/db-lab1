#!C:/Users/rhonc/AppData/Local/Programs/Python/Python38-32/python
print("Content-Type: text/html")
print()
import cgi
from strap import connection


form = cgi.FieldStorage()
ID = form.getvalue("passID")

cursor = connection.cursor()
cursor.execute("select * from user where id = %s;" % ID)
result = cursor.fetchall()
print('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">')
print('<p>Name: %s</p>' % result[0][1])
print('<p>Email: %s</p>' % result[0][3])
print('<p>Password:  ')

for i in range(len(result[0][2])):
    print('*')
print('</p>')

