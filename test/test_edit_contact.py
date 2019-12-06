from model.contact import Contact

def test_edit_contact(app):
    app.session.Login(username="admin", password="secret")
    app.contacts.Default_form_after_login()
    app.contacts.edit(Contact(first_name="Edited first name", last_name="Edited last name",
                                  address="Pravdinsk", mail="ss@ya.ru",
                                  day="7", month="May", year="1985"))
    app.session.Logout()