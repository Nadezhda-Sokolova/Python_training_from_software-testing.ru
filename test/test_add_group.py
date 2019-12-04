# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application
import pytest

@pytest.fixture
def app (request):
    fixture = Application ()
    request.addfinalizer(fixture.distroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="1 G", header="description", footer="one"))
    app.logout()

def test_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
