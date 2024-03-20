import sqlite3

def add_info():
    """Заполнение таблиц"""

    connecton = sqlite3.connect("my_databse.db")
    cursor = connecton.cursor()
    
    responsible = {1: 'Иванов', 2: 'Петров', 3: 'Сидоров'}
    for key, val in responsible.items():
        cursor.execute('INSERT INTO Responsible_for_lawsuits (id_responsible, fio) VALUES (?, ?)', (key, val))
    lawsuits = {1: 3, 2: 3, 3: 2, 4: 1}
    for key, val in lawsuits.items():
        cursor.execute('INSERT INTO Lawsuits (id_lawsuit, id_responsible) VALUES (?, ?)', (key, val))
    lawsuits_dates = {1: '2024-02-15', 2: '2024-10-07', 3: '2024-09-01', 4: '2024-06-02'}
    for key, val in lawsuits_dates.items():
        cursor.execute('INSERT INTO Lawsuits_dates (id_lawsuit, date) VALUES (?, ?)', (key, val))
