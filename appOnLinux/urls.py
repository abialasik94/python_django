from django.urls import path
from . import views
urlpatterns = [
    path('powitanie', views.druga, name="druga"),
    path('pierwsza', views.pierwsza, name="pierwsza"),
]
