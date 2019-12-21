# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contacts.get_contacts_list()
    contact = Contact(first_name="First name", last_name="Last name")
    app.contacts.New_contact_form()
    app.contacts.Filling_information_form(contact)
    app.contacts.Submit_new_contact_creation()
    app.contacts.Open_home_page()
    assert len(old_contacts) + 1 == app.contacts.Count()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
