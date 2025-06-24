from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='LOGIN'),
    path('register/', views.register, name='REGISTER'),
    path('base/', views.general_page, name='GENERAL'),
    
    path('test/', views.test_app, name='TEST'),
]