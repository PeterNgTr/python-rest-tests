import pytest


@pytest.fixture
def base_endpoint():
	return "https://reqres.in/api"

@pytest.fixture
def user_endpoint(base_endpoint):
    return base_endpoint + '/users/'