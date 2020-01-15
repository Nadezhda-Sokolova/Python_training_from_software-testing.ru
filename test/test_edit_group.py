from model.group import Group
from random import randrange
import random

# load from UI
# def test_edit_group(app):
#     if app.group.count() == 0:
#         app.group.create()
#         app.group.fill_group_form(Group(name='test'))
#         app.group.submit_group_creation()
#     old_groups = app.group.get_group_list()
#     index = randrange(len(old_groups))
#     group = Group(name="Edited", header="edit description", footer="one number")
#     group.id = old_groups[index].id
#     app.group.edit_group_form_by_index(index)
#     app.group.fill_group_form(group)
#     app.group.submit_changes_group()
#     assert len(old_groups) == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups[index] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#load from db
def test_edit_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create()
        app.group.fill_group_form(Group(name='test'))
        app.group.submit_group_creation()
    old_groups = db.get_group_list()
    new_for_group = Group(name="Edited", header="edit description", footer="one number")
    group = random.choice(old_groups)
    app.group.edit_group_form_by_id(group.id)
    app.group.fill_group_form(new_for_group)
    app.group.submit_changes_group()
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
