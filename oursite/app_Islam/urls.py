from django.urls import path
from . import views

app_name = 'app_Islam'

urlpatterns = [
    path('', views.index, name='index'),
]