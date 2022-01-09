# Sample DRF API

This is a sample Rest API created using Django Rest Framework, for CRUD operations of Users of any Application. The database used is MongoDB

## API Endpoints

1) api/users   => get all users (not to be exposed to public)
2) api/user/id=? => get an user by his id
3) api/createuser => post an user to db
4) api/modifyuser/id=? => modify an user using patch
5) api/deleteuser/id=? => delete an user using delete

## Requirements

1) MongoDB
2) Django Rest Framework
3) Vagrant (for dev)
4) Docker (for deployment)
