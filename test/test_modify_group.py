from model.group import Group
from random import randrange
import random

# load from DB
def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create()
        app.group.fill_group_form(Group(name='test'))
        app.group.submit_group_creation()
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_for_group = Group(name="Modified group")
    app.group.modify_group_by_id(group.id, new_for_group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# load from UI
# def test_modify_group_name(app):
#     if app.group.count() == 0:
#         app.group.create()
#         app.group.fill_group_form(Group(name='test'))
#         app.group.submit_group_creation()
#     old_groups = app.group.get_group_list()
#     index = randrange(len(old_groups))
#     group = Group(name="New group")
#     group.id = old_groups[index].id
#     app.group.modify_group_by_index(index, group)
#     assert len(old_groups) == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups[index] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create()
#         app.group.fill_group_form(Group(name='test'))
#         app.group.submit_group_creation()
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
