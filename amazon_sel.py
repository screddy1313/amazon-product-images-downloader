from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Amazon:
    def __init__(self):
        self.item = None
        self.base_url = 'https://www.amazon.in'
        self.browser = webdriver.Chrome()

    def search_text(self, item):
        '''
        Given an item name, selenium opens amazon home page and searches for the product.

        Returns the html content of product page. This is used by beautiful soup.

        '''

        self.item = item
        self.browser.get(self.base_url)
        search_bar = 'input#twotabsearchtextbox'

        self.browser.find_element(By.CSS_SELECTOR, search_bar).send_keys(
            self.item + Keys.RETURN)

        page_src = self.browser.page_source

        return page_src

    def next_page(self):

        # if there is next page, click on the next page and return page content
        try:
            element = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text() = 'Next']")))

            element.click()

            # just waiting page to be loaded !!. No clicking
            element = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text() = 'Next']")))

            return self.browser.page_source

        except:
            print('All Pages Traversed !!! ')
            # close the browser instance
            self.browser.quit()
            return -1
