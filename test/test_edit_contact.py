from model.contact import Contact
from random import randrange
import random

# load from db
def test_edit_contact(app, db, check_ui):
    if app.contacts.Count() == 0:
        app.contacts.New_contact_form()
        app.contacts.Filling_information_form(Contact(first_name="Delete name", last_name="For deleting name", address="Novgorod",
                                                      home_phone="21323", work_phone="2393", mobile_phone = "24234324", fax = '7777',
                                                      mail_1="ddd@ya.by", mail_2='fff@wer.us', mail_3="kol@gmail.com"))
        app.contacts.Submit_new_contact_creation()
        app.contacts.Open_home_page()
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    new_for_contact = Contact(first_name="Edited first name", last_name="Edited last name", address="Nizhny_Novgorod",
                      home_phone="111", work_phone="222", mobile_phone="333", fax = "0000",
                      mail_1="ddd@ya.by", mail_2='fff@wer.us', mail_3="kol@gmail.com")
    app.contacts.edit_contact_by_id(contact.id)
    app.contacts.Filling_information_form(new_for_contact)
    app.contacts.Submit_updating_form()
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) == app.contacts.Count()
    app.contacts.Open_home_page()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contacts.get_contacts_list(), key=Contact.id_or_max)


# load from UI
# def test_edit_contact(app):
#     if app.contacts.Count() == 0:
#         app.contacts.New_contact_form()
#         app.contacts.Filling_information_form(Contact(first_name="Delete name", last_name="For deleting name", address="Novgorod",
#                                                       home_phone="21323", work_phone="2393", mobile_phone = "24234324", fax = '7777',
#                                                       mail_1="ddd@ya.by", mail_2='fff@wer.us', mail_3="kol@gmail.com"))
#         app.contacts.Submit_new_contact_creation()
#         app.contacts.Open_home_page()
#     old_contacts = app.contacts.get_contacts_list()
#     index = randrange(len(old_contacts))
#     contact = Contact(first_name="Edited first name", last_name="Edited last name", address="Nizhny_Novgorod",
#                       home_phone="111", work_phone="222", mobile_phone="333", fax = "0000",
#                       mail_1="ddd@ya.by", mail_2='fff@wer.us', mail_3="kol@gmail.com")
#     contact.id = old_contacts[index].id
#     app.contacts.edit_contact_by_index(index)
#     app.contacts.Filling_information_form(contact)
#     app.contacts.Submit_updating_form()
#     new_contacts = app.contacts.get_contacts_list()
#     assert len(old_contacts) == app.contacts.Count()
#     old_contacts[index] = contact
#     app.contacts.Open_home_page()
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
