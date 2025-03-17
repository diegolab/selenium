import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import booking.constants as const


class Booking(webdriver.Chrome):
    def __init__(
        self,
        driver_path=r"C:\Users\Diego\Desktop\diego_lab\selenium\SeleniumGridFiles\chromedriver.exe",
        teardown=False,
    ):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        super(Booking, self).__init__()

        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None, active=True):
        if not active:
            return  # Sai da função sem executar o código

        currency_element = self.find_element(
            By.CSS_SELECTOR, '[data-testid="header-currency-picker-trigger"]'
        )

        currency_element.click()
        selected_currency_element = self.find_element(
            By.XPATH,
            f'//button[@data-testid="selection-item"][.//div[contains(text(), "{currency}")]]',
        )

        print(selected_currency_element.text)

        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.NAME, "ss")
        search_field.clear()
        search_field.send_keys(place_to_go)

        # first_result = self.find_element(
        #     By.CSS_SELECTOR, "#autocomplete-result-0 > div"
        # )

        # Aguarda a lista dropdown aparecer
        WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#autocomplete-result-0"))
        )

        # Captura todos os itens dentro do dropdown
        items = self.find_elements(By.CSS_SELECTOR, "#autocomplete-result-0 > div")

        # Itera sobre os itens e clica no primeiro
        for item in items:            
            WebDriverWait(self, 10).until(
                EC.visibility_of(item)
            )
            print(item.text)
            # if item.text == place_to_go:
            #     print(item.text)
            #     item.click()
            break


        
        # time.sleep(10)


# autocomplete-result-0 > div
