import sqlite3

# Создаем подключение к базе данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

def create_tables():
    """Создание таблиц"""
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Responsible_for_lawsuits (
                id_responsible int,
                fio TEXT NOT NULL,
                primary key (id_responsible)
    );
    ''')
    cursor.execute('''
    create table if not exists Lawsuits (
                id_lawsuit int not null,
                id_responsible int not null,
                primary key (id_lawsuit),
                foreign key (id_responsible) references Responsible_for_lawsuits(id_responsible)
    );
    ''')
    cursor.execute('''
    create table if not exists Lawsuits_dates (
                id_lawsuit int not null,
                date date not null,
                foreign key (id_lawsuit) references Lawsuits(id_lawsuits)
    );
    ''')

def add_info():
    """Заполнение таблиц"""

    responsible = {1: 'Иванов', 2: 'Петров', 3: 'Сидоров'}
    for key, val in responsible.items():
        cursor.execute('INSERT INTO Responsible_for_lawsuits (id_responsible, fio) VALUES (?, ?)', (key, val))
    lawsuits = {1: 3, 2: 3, 3: 2, 4: 1}
    for key, val in lawsuits.items():
        cursor.execute('INSERT INTO Lawsuits (id_lawsuit, id_responsible) VALUES (?, ?)', (key, val))
    lawsuits_dates = {1: '2024-02-15', 2: '2024-10-07', 3: '2024-09-01', 4: '2024-06-02'}
    for key, val in lawsuits_dates.items():
        cursor.execute('INSERT INTO Lawsuits_dates (id_lawsuit, date) VALUES (?, ?)', (key, val))

def drop_tables():
    """Удаление таблиц"""

    cursor.execute('drop table Responsible_for_lawsuits')
    cursor.execute('drop table Lawsuits')
    cursor.execute('drop table Lawsuits_dates')

def select():
    """Выбор записей"""

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


create_tables()
# add_info()
# drop_tables()
select()

# Сохранение изменений и закрытие соединения
connection.commit()
connection.close()
