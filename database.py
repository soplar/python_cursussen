import mysql.connector

conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='')


cur = conn.cursor()

cur.execute('SELECT * FROM personen.persoon')

for rij in cur.fetchall():
    print(rij[1])
