import cgi
import sqlite3
con = sqlite3.connect("cgi-bin/my_database.db")
cursor = con.cursor()
form = cgi.FieldStorage()
lawsuit = form.getfirst("lawsuit")
name = form.getfirst("name_resp")
print("<html>")
print()
print("<head><meta charset=\"UTF-8\"></head>")
try:
    cursor.execute(f'select id_responsible from Responsible_for_lawsuits where fio="{name}"')
    id_resp = cursor.fetchall()[0][0]
    cursor = con.cursor()
    cursor.execute('INSERT INTO Lawsuits (id_lawsuit, id_responsible) VALUES (?, ?)', (int(lawsuit), id_resp))

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


