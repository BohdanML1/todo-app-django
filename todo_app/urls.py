from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),

    # Корінь сайту → редірект на login
    path('', lambda request: redirect('login')),

    # Автентифікація
    path('', include('todo.auth_urls')),  # окремий файл для login/register/logout

    # Завдання
    path('tasks/', include('todo.urls')),  # CRUD завдань
]
