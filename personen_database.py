
from mysql_connectie import MySQL

db = MySQL()

db.query('''CREATE DATABASE IF NOT EXISTS personen''')
            
db.query('''CREATE TABLE IF NOT EXISTS personen.persoon(
            naam VARCHAR(50),
            geboortedatum DATE,
            geslacht ENUM('M','V'),
            bsn VARCHAR(20))''')

db.query('''INSERT INTO personen.persoon VALUES
            ('Jeroen','1991-03-24', 'M', '28992'),
            ('Joan','1960-02-01', 'M', '12345'),
            ('Cor','1975-05-05', 'M', '25122'),
            ('Arthur','1970-12-10', 'M', '23443')
         ''')
