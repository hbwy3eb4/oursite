from django.urls import path
from . import views

app_name = 'app_dd'

urlpatterns = [
    path('', views.index, name='index'),
]