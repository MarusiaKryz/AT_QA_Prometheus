import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome(service = Service(r"/Users/mariiakryzhalko/Marusiia_K/Marysiia/MyIT/Prometheus_AT_QA_2023/AT_QA_Prometheus/chromedriver_mac64" + "chromedriver"))
    driver.get('https://github.com/login')
    login_elem = driver.find_element(By.ID, "login_field")
    login_elem.send_keys("mistake@mistake.com")
    pass_elem = driver.find_element(By.ID, "password")
    pass_elem.send_keys("wrongpassword")
    time.sleep(3)
    driver.close()
