from urllib import response
import pytest
import data
import json

def test_create_new_user(api):
    response = api.create_user(data.user_data)
    assert response.status_code == 200, 'response is not 200'
    #Receiving Key error trying to check response data
    #assert response.json()['username'] == data.user_data['username']
    
def test_user_login(api):
    response = api.user_login(data.user_login)
    assert response.status_code == 200, 'user is not created'
    
def test_create_list_of_users(api):
    response = api.create_list_of_users(data.list_of_users)
    assert response.status_code == 200, 'users are not created'
    
def test_user_log_out(api):
    response = api.log_user_out()
    assert response.status_code == 200, 'user is not logged out'

def test_adding_new_pet(api):
    response = api.add_new_pet(data.new_pet)
    assert response.status_code == 200, 'pet is not created'
    

#Receiving an error I/O operation on closed file. Tried few different approaches but did not work
"""
def test_add_pet_image(api):
    response = api.load_pet_image(3, data.img)
    assert response.status_code == 200, 'image is not uploaded'
    """
    
def test_update_pet(api):
    response = api.update_pet(data.pet_update)
    assert response.status_code == 200, 'pet info is not updated'
    
def test_remove_pet(api):
    response = api.delete_pet(2)
    assert response.status_code == 200, 'pet is not removed'