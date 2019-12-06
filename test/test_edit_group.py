from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="Edited", header="edit description", footer="one number"))
    app.session.logout()
