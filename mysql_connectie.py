# pip install mysql-connector

import mysql.connector

class MySQL:

    def __init__(self, database=''):
        self.__db = mysql.connector.connect( host='localhost', user='root', password='', database=database)
        self.__db.autocommit = True
        self.__cursor = self.__db.cursor()

    @property
    def db(self):
        return self.__db
    
    @property
    def cursor(self):
        return self.__cursor

    def toon_tabellen(self):
        self.cursor.execute('SHOW TABLES')
        for rij in self.cursor:
            print(rij[0])

    def toon_kolommen(self, tabel):
        self.cursor.execute(f'SELECT * FROM {tabel} LIMIT 1')

        kolom_namen = [i[0] for i in self.cursor.description]
        self.cursor.fetchall()
        for rij in kolom_namen:
            print(rij)

    def query_met_data(self, query):
        self.cursor.execute(query)

        kolom_namen = [i[0] for i in self.cursor.description]
        return [{kolom_namen[index] : column for index, column in enumerate(value)} for value in self.cursor.fetchall()]

    def query(self, query):
        self.cursor.execute(query)
        
if __name__ == '__main__':
    db = MySQL('sakila')
    db.toon_kolommen('actor')
    print(db.query('SELECT * FROM actor'))
    
