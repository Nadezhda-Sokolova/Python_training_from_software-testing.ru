# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from Data.add_group import constant as testdata

# @pytest.mark.parametrize('group', testdata, ids=[repr(x) for x in testdata])
# def test_add_group(app, group):
#     app.group.open_groups_page()
#     old_groups = app.group.get_group_list()
#     app.group.create()
#     app.group.fill_group_form(group)
#     app.group.submit_group_creation()
#     assert len(old_groups) + 1 == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

# load from UI
# def test_add_group(app, json_groups):
#     group = json_groups
#     app.group.open_groups_page()
#     old_groups = app.group.get_group_list()
#     app.group.create()
#     app.group.fill_group_form(group)
#     app.group.submit_group_creation()
#     assert len(old_groups) + 1 == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

# load from DB
def test_add_group(app, db, json_groups):
    group = json_groups
    app.group.open_groups_page()
    old_groups = db.get_group_list()
    app.group.create()
    app.group.fill_group_form(group)
    app.group.submit_group_creation()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


    # with pytest.allure.step('Given a group list'):
    #     old_groups = db.get_group_list()
    # with pytest.allure.step('When I add the group %s  to the list' % group):
    #     app.group.create()
    #     app.group.fill_group_form(group)
    #     app.group.submit_group_creation()
    # with pytest.allure.step('Then the new group list is equal to the old list with the added group'):
    #     new_groups = db.get_group_list()
    #     old_groups.append(group)
    #     assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)
