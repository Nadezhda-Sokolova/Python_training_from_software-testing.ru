from model.group import Group
from random import randrange
import random

# load from UI
# def test_delete_some_group(app):
#     app.group.open_groups_page()
#     if app.group.count() == 0:
#         app.group.create()
#         app.group.fill_group_form(Group(name='test'))
#         app.group.submit_group_creation()
#     app.group.open_groups_page()
#     old_groups = app.group.get_group_list()
#     index = randrange(len(old_groups))
#     app.group.delete_group_by_index(index)
#     assert len(old_groups) - 1 == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups[index:index+1] = []
#     assert old_groups == new_groups

# load from DB
def test_delete_some_group(app, db, check_ui):
    app.group.open_groups_page()
    if len(db.get_group_list()) == 0:
        app.group.create()
        app.group.fill_group_form(Group(name='test'))
        app.group.submit_group_creation()
    app.group.open_groups_page()
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



