
from fixture.application import Application
import pytest

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    fixture.session.ensure_Login(username="admin", password="secret")

    return fixture


@pytest.fixture (scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.distroy()
    request.addfinalizer(fin)
    return fixture

@pytest.fixture (scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_Logout()
        fixture.Distroy()
    request.addfinalizer(fin)
    return fixture