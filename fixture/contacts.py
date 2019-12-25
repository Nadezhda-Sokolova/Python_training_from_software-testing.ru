from model.Manager import Manager
from model.contact import Contact

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
        # driver.find_element_by_name("address").click()
        # driver.find_element_by_name("address").clear()
        # driver.find_element_by_name("address").send_keys(contact.address)
        # driver.find_element_by_name("email").click()
        # driver.find_element_by_name("email").clear()
        # driver.find_element_by_name("email").send_keys(contact.mail)

    def Submit_new_contact_creation(self):
        driver = self.app.driver
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index[0]

    def delete_contact_by_index(self, index):
        driver = self.app.driver
        # select contact checkbox
        self.select_contact_by_index(index)
        # press delete button
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        # refresh page
        driver.switch_to_alert().accept()
        # press home link
        driver.find_element_by_link_text("home").click()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_name("selected[]")[index].click()

    def edit_contact_form(self):
        self.edit_contact_by_index[0]

    def edit_contact_by_index(self, index):
        driver = self.app.driver
        # press pencil for some icon
        driver.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def Submit_updating_form(self):
        driver = self.app.driver
        # submit updating
        driver.find_element_by_name("update").click()
        # press home link
        driver.find_element_by_link_text("home").click()
        self.contact_cache = None

    def Return_to_default_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home page").click()

    def Count(self):
        driver = self.app.driver
        self.Open_home_page()
        return len(driver.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.Open_home_page()
            self.contact_cache = []
            for element in driver.find_elements_by_css_selector("tr[name=entry]"):
                id = element.find_element_by_name("selected[]").get_attribute('value')
                first = element.find_element_by_tag_name("td:nth-of-type(3)").text
                last = element.find_element_by_tag_name("td:nth-of-type(2)").text
                all_phones = element.find_element_by_tag_name("td:nth-of-type(6)").text.splitlines()
                self.contact_cache.append(Contact(id=id, last_name=last, first_name=first, home_phone=all_phones))
                                                  # home_phone=all_phones[0], mobile_phone=all_phones[1],
                                                  # work_phone=all_phones[2]))
            return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        driver = self.app.driver
        self.Open_home_page()
        row = driver.find_elements_by_name("selected[]")[index].click()
        cell = row.find_element_by_tag_name("td:nth-of-type(7)")
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.edit_contact_by_index(index)
        first_name = driver.find_element_by_name("firstname").get_attribute("value")
        last_name = driver.find_element_by_name("lastname").get_attribute("value")
        id = driver.find_element_by_name("id").get_attribute("value")
        home_phone = driver.find_element_by_name("home").get_attribute("value")
        work_phone = driver.find_element_by_name("work").get_attribute("value")
        mobile_phone = driver.find_element_by_name("mobile").get_attribute("value")
        secondary_phone = driver.find_element_by_name("fax").get_attribute("value")
        return Contact (first_name=first_name, last_name=last_name, id=id,
                        home_phone=home_phone, work_phone=work_phone,
                        mobile_phone=mobile_phone)
