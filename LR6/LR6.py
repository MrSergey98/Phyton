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
    lawsuits_dates = {1: '15.02.2024', 2: '07.10.2024', 3: '01.09.2024', 4: '02.06.2024'}
    for key, val in lawsuits_dates.items():
        cursor.execute('INSERT INTO Lawsuits_dates (id_lawsuit, date) VALUES (?, ?)', (key, val))

def drop_tables():
    """Удаление таблиц"""

    cursor.execute('drop table Responsible_for_lawsuits')
    cursor.execute('drop table Lawsuits')
    cursor.execute('drop table Lawsuits_dates')
    
# create_tables()
# add_info()
# drop_tables()

# Сохранение изменений и закрытие соединения
connection.commit()
connection.close()