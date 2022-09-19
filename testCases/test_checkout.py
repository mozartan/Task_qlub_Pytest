
from selenium.webdriver import Keys
from pageObjects.checkout import checkout
from selenium.webdriver.common.by import By
from time import sleep

class Test_Checkout:

    baseURL = "https://app-staging.qlub.cloud/qr/ae/dummy-checkout/86/_/_/808b16b149"

    def test_payTheBill1(sel,setup):
        sel.driver = setup
        sel.driver.maximize_window()
        sel.driver.get(sel.baseURL)
        sleep(3)
        sel.driver.delete_all_cookies()
        act_title = sel.driver.title
        if act_title == "Qlub_ | dummy-checkout":
            assert True
        else:
            sel.driver.quit()
            assert False
        sleep(3)
        sel.sp = checkout(sel.driver)
        sel.sp.payTheBill()
        sleep(4)
        sel.driver.quit()


    def test_payTheBill2(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        sleep(5)
        self.driver.delete_all_cookies()
        sleep(3)
        self.sp = checkout(self.driver)
        self.sp.payTheBill()
        sleep(9)
        self.driver.find_element(By.XPATH, "//*[@id='name']").send_keys("Al")
        sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='amount']").send_keys(Keys.BACK_SPACE)
        self.driver.find_element(By.XPATH, "//input[@id='amount']").send_keys(Keys.BACK_SPACE)
        self.driver.find_element(By.XPATH, "//input[@id='amount']").send_keys(Keys.BACK_SPACE)
        sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='amount']").send_keys("30")
        # sleep(4)
        self.driver.find_element(By.CLASS_NAME, "Tips_tipLabel__FJ_Dg").click()
        # sleep(6)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,"//iframe[@id='cardNumber']"))
        self.driver.find_element(By.XPATH, "/html/body/form/input[2]").send_keys("4242424242424242")
        self.driver.switch_to.default_content()
        # sleep(3)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,"//iframe[@id='expiryDate']"))
        self.driver.find_element(By.XPATH, '/html/body/form/input[2]').send_keys("0226")
        self.driver.switch_to.default_content()
        # sleep(3)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,"//iframe[@id='cvv']"))
        self.driver.find_element(By.XPATH, '/html/body/form/input[2]').send_keys("100")
        self.driver.switch_to.default_content()
        sleep(3)
        self.driver.find_element(By.XPATH, "//button[@id='checkout-action-btn']").click()
        sleep(10)
        self.driver.delete_all_cookies()
        self.driver.quit()
        print('Successful Test')
