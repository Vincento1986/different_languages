import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test_button_basket():
    def test_button_basket_exist(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        def check_exists():
            return len(browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")) == 1
        browser.get(link)
        time.sleep(3)
        assert check_exists() == True, "Кнопки 'добавить в корзину' нет на странице"
if __name__ == "__main__":
    unittest.main()