from model.contact import Contact
import re
from random import randrange


#load from db
def test_fields_on_home_page(app, db):
    app.contacts.Open_home_page()
    if app.contacts.Count() == 0:
        app.contacts.New_contact_form()
        app.contacts.Filling_information_form(Contact(first_name="checking name", last_name="For checking", address="Novgorod",
                                                      home_phone="21323", work_phone="2393", mobile_phone = "24234324", fax = '7777',
                                                      mail_1="ddd@ya.by", mail_2='fff@wer.us', mail_3="kol@gmail.com"))
        app.contacts.Submit_new_contact_creation()
        app.contacts.Open_home_page()
    contacts_from_ui = sorted(app.contacts.get_contacts_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contacts_list(), key=Contact.id_or_max)
    index=0
    while index <= len(contacts_from_ui):
        assert contacts_from_ui[index].first_name == contacts_from_db[index].first_name
        assert contacts_from_ui[index].last_name == contacts_from_db[index].last_name
        assert contacts_from_ui[index].address == contacts_from_db[index].address
        contact = contacts_from_db[index]
        assert contacts_from_ui[index].all_phones_from_home_page == merge_phones_like_on_home_page(contact)
        assert contacts_from_ui[index].all_emails_from_home_page == merge_all_emails_from_home_page(contact)
        index=index+1
        return index
    pass




def clear(s):
    return re.sub("[(), , -]", "", s)


def merge_all_emails_from_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.mail_1, contact.mail_2, contact.mail_3]))))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone]))))