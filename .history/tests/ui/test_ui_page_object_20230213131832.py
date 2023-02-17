from modules.ui.page_objects.sign_in_page import SignInPage
import pytest

@pytest.mark.ui 
def test_check_incorrect_username_page_object():
    sign_in_page = SignInPage()
    