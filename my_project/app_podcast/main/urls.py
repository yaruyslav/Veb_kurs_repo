from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.entre_page, name='BASE'),
    path('login/', views.login, name='LOGIN'),
    path('register/', views.register, name='REGISTER'),
    path('general/', views.general_page, name='GENERAL'),
    path('search/', views.search_page, name='SEARCH'),
    path('playlists/', views.outset_page, name='PLAYLIST'),
    
    path('test/', views.test_app, name='TEST'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)