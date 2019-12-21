from model.contact import Contact

def test_edit_contact(app):
    if app.contacts.Count() == 0:
        app.contacts.New_contact_form()
        app.contacts.Filling_information_form(Contact(first_name="Delete name", last_name="For deleting name"))
        app.contacts.Submit_new_contact_creation()
        app.contacts.Open_home_page()
    old_contacts = app.contacts.get_contacts_list()
    contact = Contact(first_name="Edited first name", last_name="Edited last name")
    contact.id = old_contacts[0].id
    app.contacts.edit_contact_form()
    app.contacts.Filling_information_form(contact)
    app.contacts.Submit_updating_form()
    new_contacts = app.contacts.get_contacts_list()
    assert len(old_contacts) == app.contacts.Count()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
