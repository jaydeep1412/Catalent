from myapp import views
from django.urls import path, include

app_name = 'myapp'
urlpatterns = [
    path(r'login', views.user_login, name='user_login'),
    path(r'logout', views.user_logout, name='user_logout'),
    path(r'my_analysis', views.my_analysis, name='my_analysis'),
    path(r'register',views.register, name='register'),
    path(r'list_entry',views.list_entries, name='list_entry'),
    path(r'display',views.display, name='display')


]