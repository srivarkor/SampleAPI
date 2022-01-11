# Sample DRF API

This is a sample Rest API created using Django Rest Framework, for CRUD operations of Users of any Application. The database used is MongoDB

## API Endpoints

1) api/usersapi/user/createuser => Create an User (Signup functionality)
2) api/usersapi/user/getuser/<int:pk> => Get all the user details 
3) api/usersapi/user/updateuser/<int:pk => Edit user details (Edit profile functionality)
4) api/usersapi/user/deleteuser/<int:pk> => Remove user (Delete your profile functionality)
5) api/usersapi/admin/createuser => Create an user (Create an user by admin)
6) api/usersapi/admin/getuser/<int:pk> => Get all the user details
7) api/usersapi/admin/updateuser/<int:pk> => Update user details (Admin can change extra props)
8) api/usersapi/admin/deleteuser/<int:pk> => Delete user (Delete an user)
9) api/usersapi/admin/searchuser?<querystring> => Search for any user (Returns all the user details matching the criteria)

## Requirements

1) MongoDB
2) Django Rest Framework
3) Vagrant (for dev)
4) Docker (for deployment)
