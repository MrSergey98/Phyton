import sqlite3


def drop_tables():
    """Удаление таблиц"""

    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    cursor.execute('drop table Responsible_for_lawsuits')
    cursor.execute('drop table Lawsuits')
    cursor.execute('drop table Lawsuits_dates')

    connection.commit()
    connection.close()