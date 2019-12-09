# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create()
    app.group.fill_group_form(Group(name="1 G", header="description", footer="one"))
    app.group.submit_group_creation()
    app.session.logout()

def test_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create()
    app.group.fill_group_form(Group(name="", header="", footer=""))
    app.group.submit_group_creation()
    app.session.logout()
