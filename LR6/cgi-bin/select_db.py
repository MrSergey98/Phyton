

import sqlite3

def select():
    """Выбор записей"""

    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    cursor.execute('select id_responsible from Responsible_for_lawsuits where fio = "Сидоров"')
    result = cursor.fetchall()[0][0]

    cursor.execute('select id_lawsuit from Lawsuits where id_responsible = ?', (result,))
    result = cursor.fetchall()

    for row in result:
        print(row[0])

    cursor.execute('select id_lawsuit from Lawsuits_dates where date < ?', ('2024-10-03',))
    result = cursor.fetchall()

    for row in result:
        print(row[0])

    connection.commit()
    connection.close()

print("Content-type: text/html")
print()
select()
