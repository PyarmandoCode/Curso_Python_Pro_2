from django.urls import path
from .views import index,detalles,acerca

urlpatterns = [
    path('', index),
    path('detalles/',detalles),
    path('acerca/',acerca)
]