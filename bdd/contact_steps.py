from pytest_bdd import given, when, then
from model.contact import Contact
import random

@given('a contact list')
def contact_list(db):
    return db.get_contacts_list()

@given('a contact with <first_name>, <last_name>, <address>, <home_phone>, <work_phone>, <mobile_phone>, <fax>, <mail_1>, <mail_2> and <mail_3>')
def new_contact(first_name, last_name, address, home_phone, work_phone, mobile_phone, fax, mail_1, mail_2, mail_3):
    return Contact(first_name=first_name, last_name=last_name, address=address,
                                 home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, fax=fax, mail_1=mail_1, mail_2=mail_2, mail_3=mail_3 )

@when('I add a new contact to the list')
def add_new_contact(app, new_contact):
    app.contacts.New_contact_form()
    app.contacts.Filling_information_form(new_contact)
    app.contacts.Submit_new_contact_creation()
    app.contacts.Open_home_page()


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact, app):
    assert len(contact_list) + 1 == app.contacts.Count()
    new_contacts = db.get_contacts_list()
    contact_list.append(new_contact)
    assert sorted(contact_list, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contacts_list()) == 0:
        app.contacts.New_contact_form()
        app.contacts.Filling_information_form(Contact(first_name="Edited first name", last_name="Edited last name", address="Nizhny_Novgorod",
                      home_phone="111", work_phone="222", mobile_phone="333", fax = "0000",
                      mail_1="ddd@ya.by", mail_2='fff@wer.us', mail_3="kol@gmail.com"))
        app.contacts.Submit_new_contact_creation()
    return db.get_contacts_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from list')
def delete_contact(app, random_contact):
    app.contacts.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old list without the delete contact')
def verify_contact_delete(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    assert len(old_contacts) - 1 == app.contacts.Count()
    new_contacts = db.get_contacts_list()
    old_contacts.remove(random_contact)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contacts.get_contacts_list(),
                                                                     key=Contact.id_or_max)


@when('I modify the contact from list')
def contact_list_modification(app, random_contact):
    new_for_contact = Contact(first_name="Modify first name", last_name="Edited last name", address="Nizhny_Novgorod",
                              home_phone="111", work_phone="222", mobile_phone="333", fax="0000",
                              mail_1="ddd@ya.by", mail_2='fff@wer.us', mail_3="kol@gmail.com")
    app.contacts.edit_contact_by_id(random_contact.id)
    app.contacts.Filling_information_form(new_for_contact)
    app.contacts.Submit_updating_form()


@then('the new contact list is equal to the old list')
def verification_list_groups_are_the_same(db, non_empty_contact_list, check_ui, app):
    new_contacts = db.get_contacts_list()
    assert len(non_empty_contact_list) == app.contacts.Count()
    app.contacts.Open_home_page()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contacts.get_contacts_list(),
                                                                     key=Contact.id_or_max)

