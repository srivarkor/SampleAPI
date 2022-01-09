from django.urls import path
from UsersApi import views


urlpatterns = [
    path('createuser',views.UserApiView.as_view()),
    path('users',views.UserApiView.as_view()),
    path('user/<int:pk>',views.UserApiView.as_view())
]
