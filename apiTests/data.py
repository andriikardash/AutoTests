user_data = {
  "id": 2,
  "username": "and",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 1
 }

user_login = {
    "username": "Andrii",
    "password": "Welcome1"
    }

list_of_users = [
  {
    "id": 0,
    "username": "Petro",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
  },


  {
    "id": 1,
    "username": "Ivan",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 1
  }
]
    

new_pet = {
    "id": 0,
  "category": {
    "id": 0,
    "name": "dog"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
    }

img_path = "C:\J\download.jpg"
with open(img_path, "rb") as img:
    files = {'file': ('download.jpg', img)}

pet_update = {
    "id": 0,
    "name": "Mukha",
  "status": "sold"
    }