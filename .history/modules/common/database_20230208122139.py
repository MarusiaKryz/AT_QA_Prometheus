import sqlite3


class Database():
    
    def __init__(self) -> None:
        self.connection = sqlite3.connect(r'/Users/mariiakryzhalko/Marusiia_K/Marysiia/MyIT/Prometheus_AT_QA_2023/AT_QA_Prometheus' + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f'Connected successfully. SQLite Database Version is: {record}')

    def get_all_users(self):
        query = 'SELECT name, address, city FROM customers'
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record   

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country  FROM customers WHERE '{name}'"; 
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record  