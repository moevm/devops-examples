from basic_selenium_test import BasicSeleniumTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestPage(BasicSeleniumTest):

    def testPage(self):
        url = self.getUrl('/')
        self.getDriver().get(url)
        wait = WebDriverWait(self.getDriver(), 10)
        time.sleep(5)
        try:
            selector = '.calendar'
            calendar_element = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
            self.assertIsNotNone(calendar_element, f'Element "{selector}" not found on the page!')
        except Exception as e:
            self.fail(f'Test failed: {e}')
