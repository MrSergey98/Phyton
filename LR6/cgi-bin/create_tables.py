import sqlite3

def create_tables():
    """Создание таблиц"""

    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    
    
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
    connection.commit()
    connection.close()
