from . import views
from django.urls import path, include
from django.contrib.auth.views import LoginView



app_name = 'users'
urlpatterns = [
    path(r'login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]






