from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(r"C:\Users\Toshiba\Downloads\chromedriver_win32\chromedriver.exe")
    return driver

