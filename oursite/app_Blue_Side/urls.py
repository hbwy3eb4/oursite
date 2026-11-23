from django.urls import path
from . import views

app_name = 'app_Blue_Side'

urlpatterns = [
    path('', views.index, name='index'),
]