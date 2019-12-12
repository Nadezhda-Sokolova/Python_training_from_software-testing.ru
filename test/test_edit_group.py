from model.group import Group

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create()
        app.group.fill_group_form(Group(name='test'))
        app.group.submit_group_creation()
    app.group.edit_group_from()
    app.group.fill_group_form(Group(name="Edited", header="edit description", footer="one number"))
    app.group.submit_changes_group()
