import cgi
import sqlite3
con = sqlite3.connect("cgi-bin/my_database.db")
cursor = con.cursor()
form = cgi.FieldStorage()
name = form.getfirst("name")
print("<html>")
print()
print("<head><meta charset=\"UTF-8\"></head>")
try:
    cursor.execute('INSERT INTO Responsible_for_lawsuits (fio) VALUES (?)', (name,))
    con.commit()
    con.close()
except:
    print("<div>Ошибка!</div>")
else:
    print("<div>Данные успешно добавлены!</div>")
finally:
    print("<a href=\"../index.html\">Назад</a>")
    print()
    print("</html>")


