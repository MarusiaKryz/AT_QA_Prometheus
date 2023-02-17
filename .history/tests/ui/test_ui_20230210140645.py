import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome(service = Service(r""))
