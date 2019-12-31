# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + ''.join([random.choice(symbols) for i in range (random.randrange(maxlen))])

def random_address(prefix, maxlen):
    symbols = string.ascii_letters + string.punctuation + " "*10 + string.digits
    return prefix + ''.join([random.choice(symbols) for i in range (random.randrange(maxlen))])

def random_mails(maxlen, domen):
    symbols = string.ascii_letters + string.digits
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + domen

def random_phones(prefix, maxlen):
    symbols = string.digits
    return prefix + ''.join([random.choice(symbols) for i in range (random.randrange(maxlen))])


contact_data = [Contact(first_name='Oleg', last_name='Petrov', address='Moscow',
             home_phone='111', work_phone='222', mobile_phone='333', fax='123',
             mail_1='kk@ya.ru', mail_2='ii@ya.by', mail_3='lala@gmail.com')] + \
               [
                   Contact(first_name=random_string("first_name is ", 8), last_name=random_string("last_name is ", 10),
                        address=random_address("address is ", 15), home_phone=random_phones("home_phone is ", 10),
                        work_phone=random_phones("work_phone is ", 10), mobile_phone=random_phones("mobile_phone is ", 10),
                        fax=random_phones("fax is ", 10), mail_1=random_mails(10, "@mail_1.ru;"),
                        mail_2=random_mails(10, "@mail_2.by;", ), mail_3=random_mails(10, "@mail_3.com;")) for i in range(5)]



@pytest.mark.parametrize('contact', contact_data, ids=[repr(x) for x in contact_data])
def test_add_contact(app, contact):
    old_contacts = app.contacts.get_contacts_list()
    app.contacts.New_contact_form()
    app.contacts.Filling_information_form(contact)
    app.contacts.Submit_new_contact_creation()
    app.contacts.Open_home_page()
    assert len(old_contacts) + 1 == app.contacts.Count()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
