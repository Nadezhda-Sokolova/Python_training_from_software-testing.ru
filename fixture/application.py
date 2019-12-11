from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contacts import ContactHelper


class Application:

    def __init__(self):
        self.driver = self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.driver.implicitly_wait(30)
        self.session = SessionHelper (self)
        self.group = GroupHelper(self)
        self.contacts = ContactHelper (self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def distroy(self):
        self.wd.quit()

    # ===================

    def Open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/index.php")

    def Distroy(self):
        self.driver.quit()
