from django.urls import path
from . import views

app_name = 'travel_app'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('planes', views.planes, name = 'planes'),
    path('trains', views.trains, name = 'trains'),
    path('automobiles', views.automobiles, name = 'automobiles'),
    path('boats', views.boats, name = 'boats'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('register', views.register, name = 'register'),

]