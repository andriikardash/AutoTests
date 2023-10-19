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