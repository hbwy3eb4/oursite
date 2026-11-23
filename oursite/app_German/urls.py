from django.urls import path
from . import views

app_name = 'app_German'

urlpatterns = [
    path('', views.index, name='index'),
]