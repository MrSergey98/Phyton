import sqlite3
con = sqlite3.connect("cgi-bin/my_database.db")
cursor = con.cursor()
def c_1():
    cursor.execute("""
        create table Lawsuits (
                id_lawsuit int not null,
                id_responsible INTEGER,
                primary key (id_lawsuit)
                foreign key (id_responsible) references Responsible_for_lawsuits (id_responsible)
        )
    """)
    
def c_2():
    cursor.execute("""
            CREATE TABLE Responsible_for_lawsuits (
                id_responsible INTEGER PRIMARY KEY AUTOINCREMENT,
                fio TEXT NOT NULL
            )
    """)
def d_2():
    cursor.execute("drop table Responsible_for_lawsuits")
def d_1():
    cursor.execute("drop table Lawsuits")

def a_2():
    cursor.execute('INSERT INTO Responsible_for_lawsuits (fio) VALUES (?)', ('Петров',))

a_2()
con.commit()
con.close()