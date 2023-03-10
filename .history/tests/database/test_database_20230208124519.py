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

    assert water_qnt[0][0] == 25

   
