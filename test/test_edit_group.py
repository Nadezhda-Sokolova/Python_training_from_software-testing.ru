from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group_from()
    app.group.filling_group_information(Group(name="Edited", header="edit description", footer="one number"))
    app.group.submit_changes_group()
    app.session.logout()
