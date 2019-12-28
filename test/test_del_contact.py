from model.contact import Contact
from random import randrange

def test_delete_first_contact(app):
    if app.contacts.Count() == 0:
        app.contacts.New_contact_form()
        app.contacts.Filling_information_form(Contact(first_name="Delete name", last_name="For deleting name",
                                                      home_phone="567", work_phone="444", mobile_phone="777"))
        app.contacts.Submit_new_contact_creation()
        app.contacts.Open_home_page()
    old_contacts = app.contacts.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contacts.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contacts.Count()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

