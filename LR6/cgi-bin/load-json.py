import sqlite3
import json
print("<html>")
print()
print("<head><meta charset=\"UTF-8\"></head>")
try:
    con = sqlite3.connect("cgi-bin/my_database.db")
    cursor = con.cursor()
    cursor.execute("select * from Lawsuits")
    lawsuits = cursor.fetchall()
    lawsuits = {"data": {item[0]: item[1] for item in lawsuits}}
    cursor.execute("select * from Lawsuits_dates")
    lawsuits_dates = cursor.fetchall()
    lawsuits_dates = {"data": {item[0]: item[1] for item in lawsuits_dates}}
    cursor.execute("select * from Responsible_for_lawsuits")
    resp_for_lawsuits = cursor.fetchall()
    resp_for_lawsuits = {"data": {item[0]: item[1] for item in resp_for_lawsuits}}
    table = {"Lawsuits" : lawsuits, "Lawsuits-dates": lawsuits_dates, "Responsible_for_lawsuits": resp_for_lawsuits}
    with open("data.json", "w") as file:
        json.dump(table, file)
    file.close()
    string = ""
    with open("data.json", "r") as file:
        string = json.load(file)
except:
    print("Ошибка!")
else:
    print(f"<div>Файл сохранён!</div><div>Данные: {string}</div>")
finally:
    print("<a href=\"../index.html\">Назад</a>")