from model.Manager import Manager

class ContactHelper (Manager):

    def Open_home_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/addressbook/") and len(driver.find_elements_by_name('searchstring')) > 0):
            driver.get("http://localhost/addressbook/index.php")

    def Default_form_after_login(self):
        driver = self.app.driver
        driver.find_element_by_id("LoginForm").submit()

    def New_contact_form(self):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()

    def Filling_information_form (self, contact):
        driver = self.app.driver
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

    def Submit_new_contact_creation(self):
        driver = self.app.driver
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

    def edit_contact_form(self):
        driver = self.app.driver
        # select contact checkbox
        driver.find_element_by_name("selected[]").click()
        # press pencil icon
        driver.find_element_by_xpath("//img[@alt='Edit']").click()

    def Submit_updating_form(self):
        driver = self.app.driver
        # submit updating
        driver.find_element_by_name("update").click()
        # press home link
        driver.find_element_by_link_text("home").click()

    def Return_to_default_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home page").click()

    def Count(self):
        driver = self.app.driver
        self.Open_home_page()
        return len(driver.find_elements_by_name("selected[]"))