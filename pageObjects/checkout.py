
from selenium.webdriver.common.by import By


class checkout:


    payTheBill_xpath = "//body/div[@id='__next']/div[1]/div[1]/div[1]/div[3]/div[1]"
    def __init__(self,driver):
        self.driver = driver

    def payTheBill(self):
        self.driver.find_element(By.XPATH, self.payTheBill_xpath).click()





