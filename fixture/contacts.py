from model.Manager import Manager

class ContactHelper (Manager):

    def Default_form_after_login(self):
        driver = self.app.driver
        driver.find_element_by_id("LoginForm").submit()

    def New_contact_form(self):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()

    def New_contact_creation(self, contact):
        driver = self.app.driver
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

    def delete_first_contact(self):
        driver = self.app.driver
        # select contact checkbox
        driver.find_element_by_name("selected[]").click()
        # press delete button
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        # refresh page
        driver.switch_to_alert().accept()
        # press home link
        driver.find_element_by_link_text("home").click()

    def Return_to_default_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home page").click()
