from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:

    def __init__(self):
        self.driver = self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper (self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def distroy (self):
        self.wd.quit()


#===================

    def Open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/index.php")

    def Login(self, username, password):
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)

    def Default_form_after_login(self):
        driver = self.driver
        driver.find_element_by_id("LoginForm").submit()

    def New_contact_form(self):
        driver = self.driver
        driver.find_element_by_link_text("add new").click()

    def New_contact_creation(self, contact):
        driver = self.driver
        # fill of new contact form
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.first_name)
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.last_name)
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.mail)
        # submit new contact creation
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def Return_to_default_page(self):
        driver = self.driver
        driver.find_element_by_link_text("home page").click()

    def Logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()

    def Distroy (self):
        self.driver.quit()


