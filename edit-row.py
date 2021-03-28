#!C:/Users/rhonc/AppData/Local/Programs/Python/Python38-32/python
print("Content-Type: text/html")
print()
import cgi
import html
from strap import connection
from bs4 import BeautifulSoup


print("Hello World")
soup = BeautifulSoup("127.0.0.1:80/lab1/home.py","html.parser")
for tag in soup.find_all(class_= 'pass-ID'):
    editID = (tag.get('id'))
sdas
print(editID)