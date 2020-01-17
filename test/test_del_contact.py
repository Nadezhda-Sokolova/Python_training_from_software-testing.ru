from model.contact import Contact
from random import randrange
import random

#load from db
def test_delete_first_contact(app, db, check_ui):
    if app.contacts.Count() == 0:
        app.contacts.New_contact_form()
        app.contacts.Filling_information_form(Contact(first_name="Delete name", last_name="For deleting name",
                                                      home_phone="567", work_phone="444", mobile_phone="777"))
        app.contacts.Submit_new_contact_creation()
        app.contacts.Open_home_page()
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    app.contacts.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contacts.Count()
    new_contacts = db.get_contacts_list()
    old_contacts.remove(contact)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contacts.get_contacts_list(), key=Contact.id_or_max)


#load from UI
# def test_delete_first_contact(app):
#     if app.contacts.Count() == 0:
#         app.contacts.New_contact_form()
#         app.contacts.Filling_information_form(Contact(first_name="Delete name", last_name="For deleting name",
#                                                       home_phone="567", work_phone="444", mobile_phone="777"))
#         app.contacts.Submit_new_contact_creation()
#         app.contacts.Open_home_page()
#     old_contacts = app.contacts.get_contacts_list()
#     index = randrange(len(old_contacts))
#     app.contacts.delete_contact_by_index(index)
#     assert len(old_contacts) - 1 == app.contacts.Count()
#     new_contacts = app.contacts.get_contacts_list()
#     old_contacts[index:index+1] = []
#     assert old_contacts == new_contacts

