from basic_selenium_test import BasicSeleniumTest


class TestPage(BasicSeleniumTest):

    def testPage(self):
        URL = self.getUrl('/')
        self.getDriver().get(URL)
        self.getDriver().implicitly_wait(30)
        obj = self.getDriver().find_element_by_css_selector(".calendar")
        self.assertNotEquals(obj, None)
