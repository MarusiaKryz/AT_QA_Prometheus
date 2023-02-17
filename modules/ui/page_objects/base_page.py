from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    PATH = r"/Users/mariiakryzhalko/Marusiia_K/Marysiia/MyIT/Prometheus_AT_QA_2023/AT_QA_Prometheus"
    DRIVER_NAME = "chromedriver"


    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(BasePage.PATH + BasePage.DRIVER_NAME))
    def close(self):
        self.driver.close()