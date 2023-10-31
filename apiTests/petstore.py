import json
from urllib import response
import requests

BASE_URL = 'https://petstore.swagger.io/v2'

class Petstore:
    
    def __init__(self, url) -> None:
        self.base_url = url
        
    def create_user(self, user_data):
        post_user = f"{self.base_url}/user"
        headers = {
          'accept': 'application/json',
          'Content-Type': 'application/json'
        }
        response = requests.post(post_user, data=json.dumps(user_data), headers=headers)
        return response
    
    def user_login(self, user_login):
        get_user_login = f"{self.base_url}/user/login"
        headers = {
          'accept': 'application/json'
        }
        response = requests.get(get_user_login, data=json.dumps(user_login), headers=headers)
        return response
    
    def create_list_of_users(self, list_of_users):
        post_user_list = f"{self.base_url}/user/createWithList"
        headers = {
          'accept': 'application/json',
          'Content-Type': 'application/json'
        }
        response = requests.post(post_user_list, data=json.dumps(list_of_users), headers=headers)
        return response
    
    def log_user_out(self):
        get_log_out = f"{self.base_url}/user/logout"
        headers = {
          'accept': 'application/json'
        }
        response = requests.get(get_log_out, headers=headers)
        return response
    
    def add_new_pet(self, new_pet):
        post_new_pet = f"{self.base_url}/pet"
        headers = {
          'accept': 'application/json',
          'Content-Type': 'application/json'
        }
        response = requests.post(post_new_pet, data=json.dumps(new_pet), headers=headers)
        return response
        

    def load_pet_image(self, petId):
        #image = 'C:\J\download.jpg'
        #with open(image, 'rb') as img:
            #files = {'image': (image, img)}
        post_pet_img = f"{self.base_url}/pet/{petId}/uploadImage"
        headers = {
          'accept': 'application/json',
          'Content-Type': 'multipart/form-data'
        }
        response = requests.post(post_pet_img, files=files)
        return response
    
    def update_pet(self, pet_update):
        put_update_pet = f"{self.base_url}/pet"
        headers = {
          'accept': 'application/json',
          'Content-Type': 'application/json'
        }
        response = requests.put(put_update_pet, data=json.dumps(pet_update), headers=headers)
        return response
    
    def delete_pet(self, petId):
        delete_pet = f"{self.base_url}/pet/{petId}"
        headers = {
          'accept': 'application/json'
        }
        response = requests.delete(delete_pet, headers=headers)
        return response