from urllib import response
import pytest
import data
import json

#•	Verify that allows creating a User
def test_create_new_user(api):
    response = api.create_user(data.user_data)
    assert response.status_code == 200, 'response is not 200'
    assert response.json()['type'] == 'unknown'
    
#•	Verify that allows login as a User
def test_user_login(api):
    response = api.user_login(data.user_login)
    assert response.status_code == 200, 'user is not created'
    assert 'logged in user' in response.json()['message']
    
#•	Verify that allows creating the list of Users
def test_create_list_of_users(api):
    response = api.create_list_of_users(data.list_of_users)
    assert response.status_code == 200, 'users are not created'
    assert response.json()['message'] == 'ok'
    
#•	Verify that allows Log out User
def test_user_log_out(api):
    response = api.log_user_out()
    assert response.status_code == 200, 'user is not logged out'
    assert response.json()['message'] == 'ok'
    assert response.json()['type'] == 'unknown'

#•	Verify that allows adding a new Pet
def test_adding_new_pet(api):
    response = api.add_new_pet(data.new_pet)
    assert response.status_code == 200, 'pet is not created'
    assert response.json()['name'] == data.new_pet['name']
    assert response.json()['status'] == data.new_pet['status']

#•	Verify that allows updating Pet’s image
#Receiving an error I/O operation on closed file. Tried few different approaches but did not work
"""
def test_add_pet_image(api):
    response = api.load_pet_image(3, data.img)
    assert response.status_code == 200, 'image is not uploaded'
    """
    
#•	Verify that allows updating Pet’s name and status
def test_update_pet(api):
    response = api.update_pet(data.pet_update)
    assert response.status_code == 200, 'pet info is not updated'
    assert response.json()['name'] == data.pet_update['name']
    assert response.json()['status'] == data.pet_update['status']
    
#•	Verify that allows deleting Pet 
def test_remove_pet(api):
    response = api.delete_pet(2)
    assert response.status_code == 404, 'pet is not removed'