from model.Manager import Manager
from model.group import Group
import random

class GroupHelper (Manager):

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")


    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name('new')) > 0):
            wd.find_element_by_link_text("groups").click()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()

    def submit_group_creation(self):
        wd = self.app.wd
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.open_groups_page()
        self.group_cache = None


    def delete_first_group(self):
        self.delete_group_by_index(0)


    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_groups_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    def edit_group_from(self):
        self.edit_group_form_by_index[0]


    def edit_group_form_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # press edit button
        wd.find_element_by_name("edit").click()



    def edit_group_form_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # press edit button
        wd.find_element_by_name("edit").click()


    def submit_changes_group(self):
        wd = self.app.wd
        # changes submit
        wd.find_element_by_name("update").click()
        # Group record has been updated
        wd.find_element_by_link_text("group page").click()
        self.open_groups_page()
        self.group_cache = None


    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_name("group page").click()

    def modify_first_group(self):
        self.modify_group_by_index[0]

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.open_groups_page()
        self.group_cache = None

    def modify_group_by_id(self, id, new_for_group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_for_group)
        # submit modification
        wd.find_element_by_name("update").click()
        self.open_groups_page()
        self.group_cache = None

    def distroy (self):
        wd = self.app.wd
        self.app.wd.quit()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute('value')
                self.group_cache.append(Group(name=text, id = id))
        return list(self.group_cache)


    def select_group_adding_contact(self):
        wd = self.app.wd
        group = random.choice(self.get_group_list())
        return group.id



    def adding_contact_to_any_group(self, id):
        wd = self.app.wd
        group_id=self.select_group_adding_contact()
        self.app.contacts.Open_home_page()
        self.app.contacts.select_contact_by_id(id)
        wd.find_element_by_css_selector("[name=to_group]").click()
        wd.find_element_by_xpath("//option[@value = %s]" % group_id).click()
        wd.find_element_by_css_selector("input[value='Add to']").click()


    def looking_contacts_in_selected_group(self, group_id):
        wd = self.app.wd
        self.app.contacts.Open_home_page()
        wd.find_element_by_css_selector("[name=group]").click()
        wd.find_element_by_xpath("//option[@value = %s]" % group_id).click()


    def deleting_contact_from_group(self, group, id):
        wd = self.app.wd
        self.looking_contacts_in_selected_group(group.id)
        self.app.contacts.select_contact_by_id(id)
        wd.find_element_by_css_selector("input[value=Remove from '%s']" % group.name).click()
        self.looking_contacts_in_selected_group(group.id)









