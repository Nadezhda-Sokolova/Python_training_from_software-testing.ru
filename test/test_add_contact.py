# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contacts.New_contact_form()
    app.contacts.Filling_information_form(Contact(first_name="First name", last_name="Last name",
                                  address="Nizhniy Novgorod", mail="nnn@ya.ru",
                                  day="3", month="March", year="1965"))
    app.contacts.Submit_new_contact_creation()


