from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('ArtemR/', include('app_ArtemR.urls')),
    path('BlueSide/', include('app_Blue_Side.urls')),
    path('dd/', include('app_dd.urls')),
    path('German/', include('app_German.urls')),
    path('Islam/', include('app_Islam.urls')),
    path('KirTarasov/', include('app_Kir_Tarasov.urls')),
    path('Vica/', include('app_Vica.urls')),
    path('Vyacheslav/', include('app_Vyacheslav.urls')),
]
