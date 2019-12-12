from model.contact import Contact

def test_delete_first_contact(app):
    if app.contacts.Count() == 0:
        app.contacts.New_contact_form()
        app.contacts.Filling_information_form(Contact(first_name="Delete name", last_name="For deleting name",
                                                      address="Nizhniy Novgorod", mail="nnn@ya.ru",
                                                      day="3", month="may", year="1934"))
        app.contacts.Submit_new_contact_creation()
        app.contacts.Open_home_page()
    app.contacts.delete_first_contact()
