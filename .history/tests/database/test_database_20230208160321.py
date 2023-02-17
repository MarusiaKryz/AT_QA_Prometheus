import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')
    print(user)

    assert user[0][0]  == 'Maydan Nezalezhnosti 1'
    assert user[0][1]  == 'Kyiv'
    assert user[0][2]  == '3127'
    assert user[0][3]  == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    user = db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)
    print(water_qnt)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печево', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30   


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'test', 'data', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


def get_detailed_orders(self):
    query = "SELECT orders.id, customers.name, products.name,\
        products.description, orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
    self.cursor.execute(query)
    record = self.cursor.fetchall()
    return record          

   