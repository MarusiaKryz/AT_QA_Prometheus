def test_remove_name(user):
    user.name = ''
    assert user.name == ''

def test_name(user):
    assert user.name == 'Mariia'

def test_second_name(user):
    assert user.second_name == 'Kryzhalko'        