from django.urls import path
from UsersApi import views


urlpatterns = [
    path('/user/createuser',views.UserApiView.as_view()),
    path('/user/getuser/<int:pk>',views.UserApiView.as_view()),
    path('/user/updateuser/<int:pk>',views.UserApiView.as_view()),
    path('/user/deleteuser/<int:pk>',views.UserApiView.as_view()),
    path('/admin/createuser',views.UserApiAdminView.as_view()),
    path('/admin/getuser/<int:pk>',views.UserApiAdminView.as_view()),
    path('/admin/updateuser/<int:pk>',views.UserApiAdminView.as_view()),
    path('/admin/deleteuser/<int:pk>',views.UserApiAdminView.as_view()),
    path('/admin/searchuser',views.UserApiAdminSearchUserView.as_view()),
]
