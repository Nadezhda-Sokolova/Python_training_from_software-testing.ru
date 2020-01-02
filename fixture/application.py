from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contacts import ContactHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == 'firefox':
            self.driver = self.wd = webdriver.Firefox()
        elif browser == 'ie':
            self.driver = self.wd = webdriver.IE()
        elif browser == 'chrome':
            self.driver = self.wd = webdriver.Chrome()
        else:
            raise ValueError ("Unrecognized browser %s" % browser)
        self.driver = self.wd = webdriver.Firefox()
        self.session = SessionHelper (self)
        self.group = GroupHelper(self)
        self.contacts = ContactHelper (self)
        self.base_url=base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def distroy(self):
        self.wd.quit()

    # ===================

    def Open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/index.php")

    def Distroy(self):
        self.driver.quit()
