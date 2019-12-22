from model.contact import Contact
from random import randrange

def test_edit_contact(app):
    if app.contacts.Count() == 0:
        app.contacts.New_contact_form()
        app.contacts.Filling_information_form(Contact(first_name="Delete name", last_name="For deleting name"))
        app.contacts.Submit_new_contact_creation()
        app.contacts.Open_home_page()
    old_contacts = app.contacts.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="Edited first name", last_name="Edited last name")
    contact.id = old_contacts[index].id
    app.contacts.edit_contact_by_index(index)
    app.contacts.Filling_information_form(contact)
    app.contacts.Submit_updating_form()
    app.contacts.Open_home_page()
    assert len(old_contacts) == app.contacts.Count()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts[index] = contact
    app.contacts.Open_home_page()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
