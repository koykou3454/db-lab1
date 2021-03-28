#!C:/Users/rhonc/AppData/Local/Programs/Python/Python38-32/python
print("Content-Type: text/html")
print()
import cgi
from strap import connection

homeHtml = open("home.html", 'r').read()

cursor = connection.cursor()

cursor.execute("select * from user;")
result = cursor.fetchall()

# count = 1;
# print(len(result[1]))
# for idx, data in enumerate(result):
#     print("<h1>%d) %s</h1>" % (int(count),str(data)))
#     count += 1

print(homeHtml)
for row in range(len(result)):
    print("<tr>")
    for column in range(len(result[0])):
        # if column == 0:
        #     print('<td><a href = "index.php">%s</a></td>' % result[row][column])
        print('<td>%s</td>' % result[row][column])
    # print('<td><a class = "edit-row" href  = "edit-row.py" onclick = passID(%d) >Edit</a><td>' % (int(result[row][0])))
    print('<td><input type = "submit" id = "edit" name = "passID" value = %d class = "edit-row"></td>' % (int(result[row][0])))
    print("</tr>")
print("</table>")
print('</form>')
print('<div id = "filler" class = "pass-ID"></div>')
print('<script src = "edit.js"></script>')

print('<div id = "center-button"><a href = "index.py"><button type = "button" class="btn btn-dark container" style = "max-width:80%">Add User</button></a></div>')
