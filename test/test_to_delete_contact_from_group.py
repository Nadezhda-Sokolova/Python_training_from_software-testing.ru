import random
from model.contact import Contact
from model.group import Group

def test_to_delete_contact_from_group(app, db ,check_ui):
    app.group.open_groups_page()
    if len(db.get_group_list()) == 0:
        app.group.create()
        app.group.fill_group_form(Group(name='group for adding of contact'))
        app.group.submit_group_creation()
    app.group.open_groups_page()
    group_list = app.group.get_group_list()
    group = random.choice(group_list)
    group_id = int(group.id)
    contacts_in_group = app.group.looking_contacts_in_selected_group(group_id)
    if contacts_in_group is None:
        main_contacts_list = app.contacts.get_contacts_list()
        if main_contacts_list is None:
            if app.contacts.Count() == 0:
                app.contacts.New_contact_form()
                app.contacts.Filling_information_form(
                    Contact(first_name="checking name", last_name="For checking", address="Novgorod",
                            home_phone="21323", work_phone="2393", mobile_phone="24234324", fax='7777',
                            mail_1="ddd@ya.by", mail_2='fff@wer.us', mail_3="kol@gmail.com"))
                app.contacts.Submit_new_contact_creation()
                app.contacts.Open_home_page()
            return main_contacts_list
        contact=random.choice(main_contacts_list)
        id = int(contact.id)
        app.group.adding_contact_to_any_group(id)
        return contacts_in_group
    contacts_in_group = app.group.looking_contacts_in_selected_group(group_id)
    contact_in_group = random.choice(contacts_in_group)
    id = contact_in_group.id
    app.group.deleting_contact_from_group(group, id)
    new_contact_list_in_selected_group = app.contacts.get_contacts_in_selected_group(group_id)
    assert len(contacts_in_group) - 1 == len(new_contact_list_in_selected_group)
    assert contact_in_group not in new_contact_list_in_selected_group
    bd_contacts_for_selected_group = db.get_contacts_list_for_selected_group(group_id)
    if check_ui:
        assert sorted(new_contact_list_in_selected_group, key=Contact.id_or_max) == \
               sorted(app.contacts.get_contacts_in_selected_group(group_id),
                      key=Contact.id_or_max)
        assert sorted(new_contact_list_in_selected_group, key=Contact.id_or_max) == \
               sorted(bd_contacts_for_selected_group, key=Contact.id_or_max)
