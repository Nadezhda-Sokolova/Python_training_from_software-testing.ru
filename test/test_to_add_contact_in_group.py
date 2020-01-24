import random
from model.contact import Contact
from model.group import Group

def test_to_add_contact_in_group(app, db, check_ui):
    app.group.open_groups_page()
    if len(db.get_group_list()) == 0:
        app.group.create()
        app.group.fill_group_form(Group(name='group for adding of contact'))
        app.group.submit_group_creation()
    app.group.open_groups_page()
    app.contacts.Open_home_page()
    if app.contacts.Count() == 0:
        app.contacts.New_contact_form()
        app.contacts.Filling_information_form(Contact(first_name="For adding in any group", last_name="For deleting name",
                                                      home_phone="567", work_phone="444", mobile_phone="777"))
        app.contacts.Submit_new_contact_creation()
        app.contacts.Open_home_page()
    old_contacts = app.contacts.get_contacts_list()
    contact = random.choice(old_contacts)
    id = int(contact.id)
    #index.id = old_contacts[index].id
    app.group.adding_contact_to_any_group(id)





