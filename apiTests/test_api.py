from urllib import response
import pytest
import data

def test_create_new_user(api):
    response = api.create_user(data.user_data)
    assert response.status_code == 200, 'response is not 200'
    
def test_user_login(api):
    response = api.user_login(data.user_login)
    assert response.status_code == 200, 'user is not created'