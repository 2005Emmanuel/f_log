from django.urls import path
from .import views
urlpatterns = [
    path('', views.User_details_save, name='User_details_save'),
]