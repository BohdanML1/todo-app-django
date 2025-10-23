from django.urls import path
from . import auth_views

urlpatterns = [
    path('login/', auth_views.login_user, name='login'),
    path('logout/', auth_views.logout_user, name='logout'),
    path('register/', auth_views.register_user, name='register'),
]
