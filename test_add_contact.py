# -*- coding: utf-8 -*-
from contact import Contact
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.distroy)
    return fixture


def test_add_contact(app):
    app.Open_home_page()
    app.Login(username="admin", password="secret")
    app.Default_form_after_login()
    app.New_contact_form()
    app.New_contact_creation(Contact(first_name="First name", last_name="Last name",
                                  address="Nizhniy Novgorod", mail="nnn@ya.ru",
                                  day="3", month="March", year="1965"))
    app.Return_to_default_page()
    app.Logout()

