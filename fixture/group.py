from model.Manager import Manager

class GroupHelper (Manager):

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")


    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def filling_group_information(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

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
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_groups_page()

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


    def distroy (self):
        self.app.wd.quit()

