import re
from random import randrange


#load from UI
def test_fields_on_home_page(app):
    old_contacts = app.contacts.get_contacts_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contacts.get_contacts_list()[index]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_all_emails_from_home_page(contact_from_edit_page)

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
