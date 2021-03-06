from model.Manager import Manager
from model.contact import Contact
import re

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
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.last_name)
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(contact.home_phone)
        driver.find_element_by_name("work").click()
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys(contact.work_phone)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        driver.find_element_by_name("fax").click()
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys(contact.fax)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.mail_1)
        driver.find_element_by_name("email2").click()
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys(contact.mail_2)
        driver.find_element_by_name("email3").click()
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys(contact.mail_3)

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
        self.Open_home_page()

    def select_contact_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_id(self, id):
        driver = self.app.driver
        # select contact checkbox
        self.select_contact_by_id(id)
        # press delete button
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        # refresh page
        driver.switch_to_alert().accept()
        # press home link
        driver.find_element_by_link_text("home").click()
        self.contact_cache = None
        self.Open_home_page()

    def select_contact_by_id(self, id):
        driver = self.app.driver
        driver.find_element_by_css_selector("input[value='%s']" % id).click()

    def edit_contact_form(self):
        self.edit_contact_by_index[0]

    def edit_contact_by_index(self, index):
        driver = self.app.driver
        # press pencil for some icon
        driver.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def edit_contact_by_id(self, id):
        driver = self.app.driver
        self.Open_home_page()
        self.select_contact_by_id(id)
        # press pencil for icon
        driver.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()

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

    def count_for_selected_group(self, group_id):
        driver = self.app.driver
        self.app.group.looking_contacts_in_selected_group(group_id)
        return len(driver.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_list_from_web(self):
        driver = self.app.driver
        self.contact_cache = []
        for element in driver.find_elements_by_css_selector("tr[name=entry]"):
            id = element.find_element_by_name("selected[]").get_attribute('value')
            first = element.find_element_by_tag_name("td:nth-of-type(3)").text
            last = element.find_element_by_tag_name("td:nth-of-type(2)").text
            address = element.find_element_by_tag_name("td:nth-of-type(4)").text
            all_phones = element.find_element_by_tag_name("td:nth-of-type(6)").text
            all_emails = element.find_element_by_tag_name("td:nth-of-type(5)").text
            self.contact_cache.append(Contact(id=id, last_name=last, first_name=first, address=address,
                                              all_phones_from_home_page=all_phones,
                                              all_emails_from_home_page=all_emails))
        return list(self.contact_cache)


    def get_contacts_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.Open_home_page()
            self.contact_cache = []
            self.get_list_from_web()
        return list(self.contact_cache)



    def get_contacts_in_selected_group(self, group_id):
        if self.contact_cache is None:
            driver = self.app.driver
            self.app.group.looking_contacts_in_selected_group(group_id)
            self.contact_cache = []
            self.get_list_from_web()
        return list(self.contact_cache)


    def open_contact_view_by_index(self, index):
        driver = self.app.driver
        self.Open_home_page()
        row = driver.find_elements_by_css_selector("tr[name=entry]")[index]
        cell = row.find_element_by_tag_name("td:nth-of-type(7)")
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.Open_home_page()
        self.edit_contact_by_index(index)
        first_name = driver.find_element_by_name("firstname").get_attribute("value")
        last_name = driver.find_element_by_name("lastname").get_attribute("value")
        id = driver.find_element_by_name("id").get_attribute("value")
        address = driver.find_element_by_name("address").text
        home_phone = driver.find_element_by_name("home").get_attribute("value")
        work_phone = driver.find_element_by_name("work").get_attribute("value")
        mobile_phone = driver.find_element_by_name("mobile").get_attribute("value")
        fax = driver.find_element_by_name("fax").get_attribute("value")
        mail_1 = driver.find_element_by_name("email").get_attribute("value")
        mail_2 = driver.find_element_by_name("email2").get_attribute("value")
        mail_3 = driver.find_element_by_name("email3").get_attribute("value")
        return Contact(first_name=first_name, last_name=last_name, id=id, address=address,
                       home_phone=home_phone, work_phone=work_phone, mobile_phone=mobile_phone,
                       fax=fax, mail_1 = mail_1, mail_2=mail_2, mail_3=mail_3)

    def get_contacts_from_view_page(self, index):
        driver = self.app.driver
        self.open_contact_view_by_index(index)
        text = driver.find_element_by_id('content').text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        fax = re.search("F: (.*)", text).group(1)
        return Contact(home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, fax=fax)

