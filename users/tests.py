from django.test import TestCase # noqa

# Create your tests here.

import pytest

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

def test_canGetAllUsers(api_client):
    response = api_client.get('/users/')
    assert response.status_code == 200

def test_canFetchSingleUser(api_client):
    response = api_client.get('/users/?search=shafferowens@pharmex.com')
    assert response.status_code == 200
def test_cannot_get_not_existent(api_client):
    response = api_client.get('/users/?search=manu')
    assert response.status_code == 404

