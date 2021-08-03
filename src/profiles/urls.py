from django.urls import path
from .views import profiles_home, profiles_login, profiles_logout

urlpatterns = [
    path('', profiles_home, name='profiles-home'),
    path('login/', profiles_login, name='profiles-login'),
    path('logout/', profiles_logout, name='profiles-logout')
]
