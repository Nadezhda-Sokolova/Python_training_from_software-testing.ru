
def test_delete_first_contact(app):
    app.Open_home_page()
    app.contacts.delete_first_contact()
