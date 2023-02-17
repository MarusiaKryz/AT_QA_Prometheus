import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome(service = Service(r"/Users/mariiakryzhalko/Marusiia_K/Marysiia/MyIT/Prometheus_AT_QA_2023/AT_QA_Prometheus" + "chromedriver_mac64"))
    driver.get('https://github.com/login')
    driver.close()
