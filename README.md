# Tesis Keyler

***This repository contains the source code of the official Keyler Tesis, designed to represent this service in a clear and professional manner.***

### Technologies used

- Django 
<!-- 
### Documentation or local endpoints

#### AUTHENTICATION

##### Auth User

> http://127.0.0.1:8000/auth/jwt/create/

------------



#### Users

##### Users List *( GET )*

> http://127.0.0.1:8000/api/users/

##### User Create *( POST )*

> http://127.0.0.1:8000/api/users/

`Its necessary to send into the following data the field "is_active" in the body of the request`

##### User Detail *( GET )*

> http://127.0.0.1:8000/api/users/uuid_of_the_created_user/

##### User Update *( PUT )*

> http://127.0.0.1:8000/api/users/uuid_of_the_created_user/


##### User Delete *( DELETE )*

> http://127.0.0.1:8000/api/users/uuid_of_the_created_user/

------------ -->

<!-- #### MESSAGES

##### Messages List *( GET )*

> http://127.0.0.1:8000/api/chats/uuid_of_the_created_chat/messages/

##### Messages Create *( POST )*

> http://127.0.0.1:8000/api/chats/uuid_of_the_created_chat/messages/

`{"text_message": "Me puedes decir para que se utilizan las imagenes custom","image": "path_of_the_image.png"}`

- The image is optional

##### Messages Interaction *( POST )*

> http://127.0.0.1:8000/api/chats/uuid_of_the_created_chat/messages/interaction/

`{"message_uid": "dce8e3df-bcd2-4c9e-b51c-0402355e8a55","is_like": "True"}`

------------ -->

### Local installation

1- Clone the repository:

`git clone https://github.com/your-user/your-repository.git`

2- Create a virtual enviroment

`pyhton -m venv venv`

4- Install all dependencies

`pip install -r requirements.txt`


5- Migrate module to module

6- Create super user

`python manage.py createsuperuser` 

7- Run server

`python manage.py runserver`