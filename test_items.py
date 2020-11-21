import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class Test_market_page:
    def test_should_be_add_to_cart_button (self, browser):
            link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
            browser.get(link)
            x = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
            assert x, "Should be a button/Кнопка добавления в корзину не найдена"




