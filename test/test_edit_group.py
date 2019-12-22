from model.group import Group
from random import randrange

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create()
        app.group.fill_group_form(Group(name='test'))
        app.group.submit_group_creation()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Edited", header="edit description", footer="one number")
    group.id = old_groups[index].id
    app.group.edit_group_form_by_index(index)
    app.group.fill_group_form(group)
    app.group.submit_changes_group()
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
