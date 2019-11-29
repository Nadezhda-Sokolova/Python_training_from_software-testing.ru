# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def Open_home_page(self, driver):
        driver.get("http://localhost/addressbook/index.php")

    def Login(self, driver, username, password):
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)

    def Default_form_after_login(self, driver):
        driver.find_element_by_id("LoginForm").submit()

    def New_contact_form(self, driver):
        driver.find_element_by_link_text("add new").click()

    def new_contact_creation(self, driver, first_name="First name"):
        # fill of new contact form
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(first_name)
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("Last name")
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("Nizhniy Novgorod")
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("nnn@ya.ru")
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text("3")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[5]").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("March")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[37]").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1965")
        # submit new contact creation
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def Return_to_default_page(self, driver):
        driver.find_element_by_link_text("home page").click()

    def Logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        driver = self.driver
        self.Open_home_page(driver)
        self.Login(driver, username="admin", password="secret")
        self.Default_form_after_login(driver)
        self.New_contact_form(driver)
        self.new_contact_creation(driver)
        self.Return_to_default_page(driver)
        self.Logout(driver)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
