# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    group = Group(name="1 G", header="description", footer="one")
    app.group.create()
    app.group.fill_group_form(group)
    app.group.submit_group_creation()
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

# def test_empty_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group.create()
#     app.group.fill_group_form(group)
#     app.group.submit_group_creation()
#     assert len(old_groups) + 1 == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

