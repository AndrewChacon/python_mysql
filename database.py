import mysql.connector

config = {
    'user': 'root',
    'password': 'isolation',
    'host': 'localhost',
    'database': 'acme'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()
