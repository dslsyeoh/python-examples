import sqlite3
import os
import logging.config

DB_PATH = "../../resources/stocks.db"
LOG_CONFIG = "../../resources/config/db_logger.conf"
LOG_PATH = "../log/db_query.log"

logging.config.fileConfig(fname=LOG_CONFIG, disable_existing_loggers=True, defaults={"path": LOG_PATH, "mode": "w"})


class Stock:
    id = 0
    name = ""
    quantity = 0
    price = 0.0

    def __init__(self, c):
        self.cursor = c

    def insert(self):
        query = f'''INSERT INTO STOCKS ('ID', 'NAME', 'QUANTITY', 'PRICE') VALUES ({self.id}, '{self.name}', {self.quantity}, {self.price})'''
        logging.log(level=logging.INFO, msg=query)
        self.cursor.execute(query)

    def update(self):
        query = f'''UPDATE STOCKS SET NAME = '{self.name}', QUANTITY = {self.quantity}, PRICE = {self.price} WHERE ID = {self.id}'''
        logging.log(level=logging.INFO, msg=query)
        self.cursor.execute(query)

    def delete(self):
        query = f"DELETE FROM STOCKS WHERE ID = {self.id}"
        self.cursor.execute(f"DELETE FROM STOCKS WHERE ID = {self.id}")
        logging.log(level=logging.INFO, msg=query)

    def display(self):
        query = f"SELECT * FROM STOCKS WHERE ID = {self.id}"
        self.cursor.execute(query)
        logging.log(level=logging.INFO, msg=query)
        row = self.cursor.fetchone()
        print(f"ID: {row[0]} Name: {row[1]} Quantity: {row[2]} Price: {row[3]}")


def create_table(c):
    c.execute('''
        CREATE TABLE IF NOT EXISTS STOCKS
        (ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        QUANTITY INT NOT NULL,
        PRICE DOUBLE NOT NULL);
    ''')


def init_stocks(c):
    my_list = []

    stock_1 = Stock(c)
    stock_2 = Stock(c)
    stock_3 = Stock(c)

    stock_1.id = 1
    stock_1.name = "Apple"
    stock_1.price = 2.50
    stock_1.quantity = 10

    stock_2.id = 2
    stock_2.name = "Grape"
    stock_2.price = 5
    stock_2.quantity = 20

    stock_3.id = 3
    stock_3.name = "Orange"
    stock_3.price = 2
    stock_3.quantity = 30

    my_list.append(stock_1)
    my_list.append(stock_2)
    my_list.append(stock_3)

    return my_list


def connect_db():
    try:
        return sqlite3.connect(DB_PATH)
    except sqlite3.OperationalError as error:
        logging.log(level=logging.ERROR, msg=error)


def init_table(c):
    try:
        create_table(c)
    finally:
        logging.log(level=logging.INFO, msg="Completed initialize table.")


def list_stocks(c):
    c.execute("SELECT * FROM STOCKS")
    rows = c.fetchall()
    for row in rows:
        print(f"ID: {row[0]} Name: {row[1]} Quantity: {row[2]} Price: {row[3]}")


def is_exists():
    return os.path.exists(DB_PATH)


connection = connect_db()
cursor = connection.cursor()

init_table(cursor)
stocks = init_stocks(cursor)

for stock in stocks:
    stock.insert()

list_stocks(cursor)

to_be_update = stocks[0]
to_be_update.name = "Green Apple"
to_be_update.price = 3
to_be_update.update()

print("\nAFTER UPDATED")
list_stocks(cursor)

print("\nAFTER DELETED")
to_be_deleted = stocks[2]
to_be_deleted.delete()
list_stocks(cursor)

print("\nShow Stock 1")
to_be_update.display()

# DROP TABLE
cursor.execute("DROP TABLE STOCKS")

connection.commit()
connection.close()








