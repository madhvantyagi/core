from django.urls import path
from .views import profiles_home

urlpatterns = [
    path('', profiles_home, name='profiles-home')
]
