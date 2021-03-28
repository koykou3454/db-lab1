#!C:/Users/rhonc/AppData/Local/Programs/Python/Python38-32/python
print("Content-Type: text/html")
print()
import cgi
from strap import connection


form = cgi.FieldStorage()
ID = form.getvalue("passID")
print(form.getvalue("passID"))

cursor = connection.cursor()
cursor.execute("select * from user where id = %s;" % ID)
result = cursor.fetchall()

print(result)    
