from django.contrib import admin
from django.urls import path,include
from pybo import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/',include(urls)),
]
