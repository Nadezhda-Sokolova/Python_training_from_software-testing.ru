from model.contact import Contact

def test_edit_contact(app):
    app.Open_home_page()
    app.contacts.edit_contact_form()
    app.contacts.Filling_information_form(Contact(first_name="Edited first name", last_name="Edited last name",
                                           address="Pravdinsk", mail="ss@ya.ru",
                                           day="7", month="May", year="1985"))
    app.contacts.Submit_updating_form()