from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create()
        app.group.fill_group_form(Group(name='test'))
        app.group.submit_group_creation()
    app.group.delete_first_group()

