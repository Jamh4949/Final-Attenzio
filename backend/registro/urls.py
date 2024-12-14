from django.urls import path
from .views import registrar_profesor

urlpatterns = [
    path('registro/', registrar_profesor, name='registrar_profesor'),
]
