
def test_delete_first_contact(app):
    app.session.Login(username="admin", password="secret")
    app.contacts.Default_form_after_login()
    app.contacts.delete_first_contact()
    app.session.Logout()
