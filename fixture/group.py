from model.Manager import Manager
from model.group import Group

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


    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_group_from(self):
        wd = self.app.wd
        self.open_groups_page()
        # select group
        wd.find_element_by_name("selected[]").click()
        # press edit button
        wd.find_element_by_name("edit").click()


    def submit_changes_group(self):
        wd = self.app.wd
        # changes submit
        wd.find_element_by_name("update").click()
        # Group record has been updated
        wd.find_element_by_link_text("group page").click()
        self.open_groups_page()


    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_name("group page").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.open_groups_page()

    def distroy (self):
        wd = self.app.wd
        self.app.wd.quit()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        wd = self.app.wd
        self.open_groups_page()
        groups = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute('value')
            groups.append(Group(name=text, id = id))
        return groups