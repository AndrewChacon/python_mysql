import mysql.connector
from mysql.connector import errorcode
from database import cursor

DB_NAME = 'acme'

TABLES = {}

TABLES['logs'] = (
    "CREATE TABLE `logs` ("
    " `id` INT(11) NOT NULL AUTO_INCREMENT,"
    " `text` VARCHAR(250) NOT NULL,"
    " `user` VARCHAR(250) NOT NULL,"
    " `created` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)


def create_database():
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("DATABASE {} CREATED".format(DB_NAME))


def create_tables():
    cursor.execute("USE {}".format(DB_NAME))
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("CREATING TABLE ({}) ".format(table_name), end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("ALREADY EXISTS")
            else:
                print(err.msg)


create_database()
create_tables()
