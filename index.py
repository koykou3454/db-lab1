#!C:/Users/rhonc/AppData/Local/Programs/Python/Python38-32/python
print("Content-Type: text/html")
print()
import cgi
from strap import connection
indexHtml = open("index.html", 'r').read()
print(indexHtml)